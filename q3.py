import psycopg2
import pandas as pd


def question3():
    """ Insert the data from question 2 into new_table """
    # Reading data from excel file
    df = pd.read_excel("/Users/shashankdey/PycharmProjects/pythonProject1/postgresql_assignment/q2.xlsx")
    conn = None
    cur = None

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

    # Writing SQL query
    def query(cur):
        insert = """insert into new_table (employee_name, employee_no, department_name, total_comp, months) 
                values (%s,%s,%s,%s,%s);"""

        data = []
        for row in df.iterrows():
            # Creating tuples from dataframe
            record_to_insert = (row[1]['Employee Name'], row[1]['Employee No.'], row[1]['Department Name'],
                                row[1]['Total compensation'], row[1]['Total months'])
            data.append(record_to_insert)

        # Inserting data into the table
        cur.executemany(insert, data)
        conn.commit()

    try:
        cur, conn = connect()
        query(cur)

    except:
        print("Database is not connected")

    finally:
        conn.close()
        cur.close()


if __name__ == '__main__':
    question3()
