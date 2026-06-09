from app.db.db_connection import get_cur
from app.models.table_creation_statement import tables

def creating_tables(tables):
    i = 0
    with get_cur() as cur:
        
        for table in tables:
            cur.execute(table)
            i +=1
            print(f"Executing....{i}")

if __name__ == "__main__":
    creating_tables(tables)