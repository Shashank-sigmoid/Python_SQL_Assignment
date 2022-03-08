import psycopg2


def db_connection():
    """ Connect to the PostgresSQL database server """
    cur = None
    conn = None

    def connect():
        # DB variables
        db_host = "localhost"
        db_name = "company"
        db_user = "postgres"
        db_pass = "SDstrange"

        # Connecting with the local server database
        print("Connecting to the PostgresSQL database...")
        conn = psycopg2.connect(dbname=db_name, user=db_user, password=db_pass, host=db_host)
        cur = conn.cursor()
        return cur, conn

    # To check database connectivity
    def check(cur):
        print("PostgresSQL database version:")
        cur.execute("select version();")

        # Displaying the data fetched
        db_version = cur.fetchone()
        print(db_version)

    try:
        cur, conn = connect()
        check(cur)

    except:
        print("Database is not connected")

    finally:
        cur.close()
        conn.close()


if __name__ == '__main__':
    db_connection()
