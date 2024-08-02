import mysql.connector
from mysql.connector import Error
import pandas as pd

def connect():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='cricbuzz',
            user='root',
            password='1234'
        )
        if connection.is_connected():
            print("Connected to MySQL Server")
            return connection
    except Error as e:
        print("Error while connecting to MySQL", e)
        return None

def create_table(cursor):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS topOdiPlayers (
        `rank` INT,
        `name` VARCHAR(200),
        `country` VARCHAR(200),
        `points` INT
    )
    """
    cursor.execute(create_table_query)

def insert_data_from_csv(cursor, connection, csv_file_path):
    df = pd.read_csv(csv_file_path)
    
    for i, row in df.iterrows():
        sql = "INSERT INTO topOdiPlayers (`rank`, `name`, `country`, `points`) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, tuple(row))
    
    connection.commit()

def main():
    connection = connect()
    if connection:
        cursor = connection.cursor()
        create_table(cursor)
        csv_file_path = r'D:\GitHub\DataAnalytics\batsmen_rankings.csv'
        insert_data_from_csv(cursor, connection, csv_file_path)
        
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

main()
