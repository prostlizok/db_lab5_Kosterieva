import csv
import psycopg2

username = 'postgres'
password = 'postgres'
database = 'db_lab3'
host = 'localhost'
port = '5432'
INPUT_CSV_FILE1 = 'champs.csv'
INPUT_CSV_FILE2 = 'matches.csv'
INPUT_CSV_FILE3 = 'participants.csv'

delete_champions = 'DELETE FROM champions'
delete_match = 'DELETE FROM match'
delete_participants = 'DELETE FROM participants'

insert_match = '''
INSERT INTO match (id, duration, platformid, seasonid) VALUES (%s, %s, %s, %s)
'''

insert_participants = '''
INSERT INTO participants (ID, matchID, player, championID, role, position) VALUES (%s, %s, %s, %s, %s, %s)
'''

insert_champions = '''
INSERT INTO champions (championID, champion_name) VALUES (%s, %s)
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
    cur = conn.cursor()
    cur.execute(delete_champions)
    cur.execute(delete_match)
    cur.execute(delete_participants)

    with open(INPUT_CSV_FILE1, 'r') as file:
        reader = csv.DictReader(file)
        count = 0  # Initialize counter
        for row in reader:
            if count < 10:  # Check if less than 10 rows have been processed
                cur.execute(insert_champions, (row['id'], row['name']))
                count += 1  # Increment counter
            else:
                break  # Exit the loop after 10 rows

    with open(INPUT_CSV_FILE2, 'r') as file:
        reader = csv.DictReader(file)
        count = 0  # Reset counter for next file
        for row in reader:
            if count < 10:
                cur.execute(insert_match, (row['id'], row['duration'], row['platformid'], row['seasonid']))
                count += 1
            else:
                break

    with open(INPUT_CSV_FILE3, 'r') as file:
        reader = csv.DictReader(file)
        count = 0  # Reset counter for next file
        for row in reader:
            if count < 10:
                cur.execute(insert_participants, (
                    row['id'], row['matchid'], row['player'], row['championid'], row['role'], row['position']))
                count += 1
            else:
                break

    conn.commit()

conn.close()
