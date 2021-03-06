import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *
import datetime


def process_song_file(cur, filepath):
    """
    For each file in ./data/song_data, process it and upload the data into table songs and artisists

    Args:
        cur (cursor): connected postgres database cursor
        filepath (str): path to the json file to be processed
    """
    # open song file
    df = pd.read_json(filepath, lines=True)

    # insert song record
    song_datas = list(
        df[['song_id', 'title', 'artist_id', 'year', 'duration']].values)
    for song_data in song_datas:
        cur.execute(song_table_insert, song_data)

    # insert artist record
    artist_datas = list(df[['artist_id', 'artist_name', 'artist_location',
                        'artist_latitude', 'artist_longitude']].values)
    for artist_data in artist_datas:
        cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    """For each file in ./data/log_data, process it and upload the data into table Time, Users and Songplays

    Args:
        cur (cursor): connected postgres database cursor
        filepath (str): path to the json file to be processed
    """
    # open log file
    df = pd.read_json(filepath, lines=True)

    # filter by NextSong action
    df = df.query("page == 'NextSong'")

    # convert timestamp column to datetime
    t = pd.to_datetime(df["ts"], unit="ms")

    # insert time data records
    time_data = list(map(list, zip(
        t.tolist(),
        t.dt.hour.tolist(),
        t.dt.day.tolist(),
        t.dt.weekofyear.tolist(),
        t.dt.month.tolist(),
        t.dt.year.tolist(),
        t.dt.weekday.tolist()
    )))
    column_labels = ["start_time", "hour", "day",
                     "week", "month", "year", "weekday"]
    time_df = pd.DataFrame(time_data, columns=column_labels)

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df[["userId", "firstName", "lastName", "gender", "level"]]

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():

        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()

        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        start_time = datetime.datetime.utcfromtimestamp(row.ts/1000.0)
        songplay_data = ( start_time, row.userId, row.level, songid,
                         artistid, row.sessionId, row.location, row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    """
    Main ETL pipeline, procecss all the json file inside ./data/log_data, ./data/song_data and
    upload the data the according fact/dim table

    Args:
        cur (cursor): PostgresDB Connection Cursor
        conn (DBconnection): PostgresDB Connection string
        filepath (str): directory to the file data (./data)
        func (func): which function to used based on the filepath
    """
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root, '*.json'))
        for f in files:
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    conn = psycopg2.connect(
        "host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()
