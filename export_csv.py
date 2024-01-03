import csv
import psycopg2

username = 'postgres'
password = 'postgres'
database = 'db_lab3'
host = 'localhost'
port = '5432'

output_file = '{}.csv'

tables = [
    'champions',
    'match',
    'participants',
]


conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
    cur = conn.cursor()

    for table_name in tables:
        cur.execute(f'SELECT * FROM {table_name}')
        fieldnames = [desc[0] for desc in cur.description]

        with open(output_file.format(table_name), 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(fieldnames)
            for row in cur:
                writer.writerow(row)

conn.close()
