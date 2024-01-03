import psycopg2
import matplotlib.pyplot as plt

username = 'postgres'
password = 'postgres'
database = 'db_lab3'
host = 'localhost'
port = '5432'

query_1 = '''
CREATE view ten_champs AS
SELECT 
    C.champion_name,
    COUNT(*) AS use_count
FROM 
    Participants P
JOIN 
    Champions C ON P.championID = C.championID
GROUP BY 
    C.champion_name
ORDER BY 
    use_count DESC;
'''

query_2 = '''
CREATE view all_roles AS
SELECT 
    P.role,
    COUNT(*) AS role_count
FROM 
    Participants P
GROUP BY 
    P.role;
'''

query_3 = '''
CREATE view bot_champs AS
SELECT 
    P.position,
    COUNT(DISTINCT P.role) AS unique_roles_count
FROM 
    Participants P
GROUP BY 
    P.position;
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
    cur = conn.cursor()
    plt.figure(figsize=(12, 7))

    # запит 1
    cur.execute('DROP VIEW IF EXISTS ten_champs')
    cur.execute(query_1)
    cur.execute('SELECT * FROM ten_champs')
    #cur.execute(query_1)
    champions, use_counts = zip(*cur.fetchall())

    bar_ax = plt.subplot(1, 3, 1)
    bar_ax.bar(champions, use_counts)
    bar_ax.set_xticklabels(champions, rotation=45, ha='right')
    bar_ax.set_title('Кількість використань чемпіонів')
    bar_ax.set_ylabel('Кількість використань')
    bar_ax.set_xlabel('Чемпіони')

    # запит 2
    cur.execute('DROP VIEW IF EXISTS all_roles')
    cur.execute(query_2)
    cur.execute('SELECT * FROM all_roles')
    roles, role_counts = zip(*cur.fetchall())

    pie_ax = plt.subplot(1, 3, 2)
    pie_ax.pie(role_counts, labels=roles, autopct='%1.1f%%')
    pie_ax.set_title('Розподіл ролей серед учасників')

    # запит 3
    cur.execute('DROP VIEW IF EXISTS bot_champs')
    cur.execute(query_3)
    cur.execute('SELECT * FROM bot_champs')
    positions, unique_roles_counts = zip(*cur.fetchall())

    bar2_ax = plt.subplot(1, 3, 3)
    bar2_ax.bar(positions, unique_roles_counts)
    bar2_ax.set_title('Кількість унікальних ролей \nна позицію')
    bar2_ax.set_xlabel('Позиції')
    bar2_ax.set_ylabel('Кількість унікальних ролей')

    plt.tight_layout()
    plt.show()
