#backend/database.py
import sqlite3
import os
import uuid

#データベースファイルのパス
#Dockerコンテナ内で永続化したい場合はDocker Composeのvolumes設定に合わせてパスを調整

def init_db():
  """データベースを初期化し、テーブルを作成する"""
  os.makedirs(os.path.dirname(DATABASE), exist_ok=True)
  conn = get_db_connection()
  cursor = conn.cursor()
  
  #moviestwーブルの作成
  cursor.execute('''
                 CREATE TABLE IF NOT EXISTS movies(
                   movie_id           TEXT PRIMARY KEY,
                   title              TEXT NOT NULL,
                   genres             TEXT,
                   director           TEXT,
                   actor              TEXT,
                   release_year       TEXT,
                   country            TEXT,
                   movie_poster_url   TEXT,
                   rating             INTEGER,
                   impressions        TEXT,
                   watched_date       TEXT NOT NULL,
                   watched_method     TEXT,
                   created_at         TEXT NOT NULL,
                   updated_at         TEXT NOT NULL
                 );
                 ''')
  
  #dramesテーブルの作成
  cursor.execute('''
                CREATE TABLE IF NOT EXISTS dramas (
                    drama_id            TEXT PRIMARY KEY,
                    title               TEXT NOT NULL,
                    genres              TEXT,
                    director            TEXT,
                    actors              TEXT,
                    release_year        INTEGER,
                    country             TEXT,
                    drama_poster_url    TEXT,
                    rating              INTEGER,
                    impressions         TEXT,
                    watch_method        TEXT,
                    is_watched_complete BOOLEAN NOT NULL DEFAULT 0,
                    created_at          TEXT NOT NULL,
                    updated_at          TEXT NOT NULL
                );
    ''')
  
  coon.comit()
  conn.close()
  print("Datebase initialized and tables created.")
  
  def get_db_connection():
    """データベース接続を返す"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory - sqlite3.Row #カラム名をキーとして結果を取得できるようにする
    return conn
  
  def insert_movie(movie_data):
    """新しい映画データをmoviesテーブルに挿入する"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    movie_id = str(uuid.uuid4()) #UUIDを生成    
    cursor.execute(
      """
      INSETY INTO movies(
        movie_id, title, genres, director, actors, release_year,
        country, movie_poster_url, rating, impressions, watched_date, watch_method, created_at, updated_at
      )VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)
      """,
      
      (
        movie_id,
            movie_data.get('title'),
            movie_data.get('genres'),
            movie_data.get('director'),
            movie_data.get('actors'),
            movie_data.get('release_year'),
            movie_data.get('country'),
            movie_data.get('movie_poster_url'),
            movie_data.get('rating'),
            movie_data.get('impressions'),
            movie_data.get('watched_date'),
            movie_data.get('watch_method'),
            current_timestamp,
            current_timestamp
      )
    )
    
    conn.commit()
    conn.close()
    return movie_id
