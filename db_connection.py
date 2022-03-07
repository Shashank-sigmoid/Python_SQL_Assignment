import psycopg2

try:
    # DB variables
    db_host = "localhost"
    db_name = "company"
    db_user = "postgres"
    db_pass = "SDstrange"

    # Connecting with the local server database
    conn = psycopg2.connect(dbname=db_name, user=db_user, password=db_pass, host=db_host)
    cur = conn.cursor()

    # To check database connectivity
    cur.execute("select * from dept;")

    # Displaying the data fetched
    results = cur.fetchall()
    for result in results:
        print(result)

except:
    print("Database is not connected")

finally:
    cur.close()
    conn.close()