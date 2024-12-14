import psycopg2


def insert_record_query(name, database):
    try:
        cursor = database.cursor()
        cursor.execute("INSERT INTO table (id, name) VALUES (DEFAULT, %s)", [name])

        database.commit()
        cursor.close()
        print('Creation successful')

    except Exception as e:
        print(f"Error creating {url}: {e}")
        database.rollback()
        raise e
