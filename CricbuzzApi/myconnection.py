import mysql.connector
import pandas as pd

connection = mysql.connector.connect(
            host='localhost',
            database='cricbuzz',
            user='root',
            password='1234'
        )
cursor = connection.cursor()

create_table_query = """
    CREATE TABLE IF NOT EXISTS topOdiPlayers (
        `rank` INT,
        `name` VARCHAR(200),
        `country` VARCHAR(200),
        `points` INT
    )
    """
cursor.execute(create_table_query)



csv_file_path = r'D:\GitHub\DataAnalytics\batsmen_rankings.csv'
df = pd.read_csv(csv_file_path)
for i, row in df.iterrows():
    sql = "INSERT INTO topOdiPlayers (`rank`, `name`, `country`, `points`) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, tuple(row))
connection.commit()

        
cursor.close()
connection.close()
print("MySQL connection is closed")
