def get_entity_query(id, database):
    cursor = database.cursor()
    cursor.execute("SELECT id FROM table WHERE id = %s", [str(id)])
    records = cursor.fetchall()
    cursor.close()
    record = records[0] if len(records) > 0 else None
    if record is not None:
        print(f"Fetched {len(records)} records")
        return record
    else:
        print(f"Couldn't find {id}")
        return None
