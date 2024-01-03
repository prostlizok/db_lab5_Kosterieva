import json
import psycopg2

# Database connection parameters
username = 'postgres'
password = 'postgres'
database = 'db_lab3'
host = 'localhost'
port = '5432'

output_file = '{}.json'

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
        rows = cur.fetchall()

        data = [dict(zip(fieldnames, row)) for row in rows]

        with open(output_file.format(table_name), 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, ensure_ascii=False, indent=4)

conn.close()
