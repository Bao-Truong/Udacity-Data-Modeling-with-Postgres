# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (
    songplay_id SERIAL PRIMARY KEY,
    start_time TIMESTAMP NOT NULL,
    user_id INT NOT NULL, 
    level TEXT, 
    song_id TEXT, 
    artist_id TEXT, 
    session_id INT, 
    location TEXT, 
    user_agent TEXT
);
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (
    user_id INT  PRIMARY KEY, 
    first_name TEXT, 
    last_name TEXT, 
    gender TEXT, 
    level TEXT
);
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (
    song_id TEXT  PRIMARY KEY, 
    title TEXT NOT NULL, 
    artist_id TEXT NOT NULL, 
    year INT, 
    duration FLOAT(8) NOT NULL
);
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (
    artist_id TEXT PRIMARY KEY, 
    name TEXT NOT NULL, 
    location TEXT, 
    latitude DOUBLE PRECISION, 
    longitude DOUBLE PRECISION
);
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (
    start_time TIMESTAMP, 
    hour SMALLINT, 
    day SMALLINT, 
    week SMALLINT, 
    month SMALLINT, 
    year SMALLINT, 
    weekday SMALLINT
);
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays ( start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) 
VALUES( %s, %s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (songplay_id)
DO NOTHING
""")

user_table_insert = ("""
INSERT INTO users (user_id, first_name, last_name, gender, level) 
VALUES(%s, %s, %s, %s, %s)
ON CONFLICT (user_id)
DO NOTHING
""")

song_table_insert = ("""
INSERT INTO songs (song_id, title, artist_id, year, duration) 
VALUES(%s, %s, %s, %s, %s)
ON CONFLICT (song_id)
DO NOTHING
""")

artist_table_insert = ("""
INSERT INTO artists (artist_id, name, location, latitude, longitude) 
VALUES(%s, %s, %s, %s, %s)
ON CONFLICT (artist_id)
DO NOTHING
""")


time_table_insert = ("""
INSERT INTO time (start_time, hour, day, week, month, year, weekday) 
VALUES(%s, %s, %s, %s, %s, %s, %s)
""")

# FIND SONGS
# - Implement the `song_select` query in `sql_queries.py` to find
# the song ID and artist ID based on the title, artist name, and duration of a song
song_select = ("""
SELECT song_id, artists.artist_id
FROM songs
JOIN artists
ON songs.artist_id=artists.artist_id
WHERE songs.title=%s AND artists.name= %s AND songs.duration= %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create,
                        song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop,
                      song_table_drop, artist_table_drop, time_table_drop]
xxx = [song_select]