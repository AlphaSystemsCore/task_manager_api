import psycopg2
from psycopg2 import pool
from contextlib import contextmanager
from app.core.db_configuration import load_config

config = load_config()

db_pool = psycopg2.pool.SimpleConnectionPool(
    minconn=1,
    maxconn=20,
    **config
)
@contextmanager
def get_conn():
    conn = db_pool.getconn()
    try:
        yield conn
    except Exception as e:
        print("error: ",e)
        raise
    finally:
        db_pool.putconn(conn)

@contextmanager
def get_cur():
    with get_conn() as conn:
        cur = conn.cursor()
        try:
            yield cur 
            conn.commit()
        except Exception as e:
            print("Error: ",e)
            conn.rollback()
            raise
        finally:
            cur.close()
            