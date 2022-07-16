# Project: Data Modeling with Postgres

## Introduction

A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

They'd like a data engineer to create a Postgres database with tables designed to optimize queries on song play analysis, and bring you on the project. Your role is to create a database schema and ETL pipeline for this analysis. You'll be able to test your database and ETL pipeline by running queries given to you by the analytics team from Sparkify and compare your results with their expected results.

## Data set
Data set source can be downloaded from here: http://millionsongdataset.com/.

In this project, i only use a subset of data from http://millionsongdataset.com/, you can find it in `./data` folder.

## How To Run

**Pre-requirements**

- Python 3.8 (Recommeded)
- Postgres Database (Tested on version 12.11)
- Manully create Database with name `sparkifydb` and a User `student` have access to that DB (update these info in database connection code in `etl.py`, `etl.ipynb`,...)
- Default:
  - Database: `sparkifydb`
  - Username: `student`
  - Password: `student`

**Create Database Tables**

> python3 create_tables.py

**Run ETL/Load Data into Database**

> python3 etl.py

## Outputs
![Artist Table](/screenshot/val_artists.png "Artist Table")
![Songs Table](/screenshot/val_songs.png "Songs Table")

## Fact Table

### **songplays** - records in log data associated with song plays i.e. records with page NextSong

| Columns     | Type      | PRIMARY KEY | NOT NULL |
|-------------|-----------|-------------|----------|
| songplay_id | SERIAL    |      O      |     O    |
| start_time  | TIMESTAMP |             |     O    |
| user_id     | INT       |             |          |
| level       | TEXT      |             |          |
| song_id     | TEXT      |             |          |
| artist_id   | TEXT      |             |          |
| session_id  | INT       |             |          |
| location    | TEXT      |             |          |
| user_agent  | TEXT      |             |          |
![Table](/screenshot/tab_songplays.png "Songplays Table")


## Dimension Tables

### **users** - users in the app

| Columns    | Type | PRIMARY KEY | NOT NULL |
|------------|------|-------------|----------|
| user_id    | INT  | O           | O        |
| first_name | TEXT |             |          |
| last_name  | TEXT |             |          |
| gender     | TEXT |             |          |
| level      | TEXT |             |          |
![Table](/screenshot/tab_users.png "Users Table")

### **songs** - songs in music database

| Columns   | Type     | PRIMARY KEY | NOT NULL |
|-----------|----------|-------------|----------|
| song_id   | TEXT     | O           | O        |
| title     | TEXT     |             | O        |
| artist_id | TEXT     |             | O        |
| year      | INT      |             |          |
| duration  | FLOAT(8) |             | O        |
![Table](/screenshot/tab_songs.png "Songs Table")

### **artists** - artists in music database

| Columns   | Type             | PRIMARY KEY | NOT NULL |
|-----------|------------------|-------------|----------|
| artist_id | TEXT             | O           | O        |
| name      | TEXT             |             | O        |
| location  | TEXT             |             |          |
| latitude  | DOUBLE PRECISION |             |          |
| longitude | DOUBLE PRECISION |             |          |
![Table](/screenshot/tab_artists.png "Artists Table")

### **time** - timestamps of records in songplays broken down into specific units

| Columns    | Type      | PRIMARY KEY | NOT NULL |
|------------|-----------|-------------|----------|
| start_time | TIMESTAMP |             |          |
| hour       | SMALLINT  |             |          |
| day        | SMALLINT  |             |          |
| week       | SMALLINT  |             |          |
| month      | SMALLINT  |             |          |
| year       | SMALLINT  |             |          |
| weekday    | SMALLINT  |             |          |
![Table](/screenshot/tab_times.png "Times Table")
