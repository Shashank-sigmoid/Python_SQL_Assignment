import psycopg2
import xlsxwriter


def question_1():
    """ Find employee no., employee name and manager name """
    workbook = None
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
        cur.execute("select e1.empno, e1.ename, e2.ename from emp e1, emp e2 where e1.mgr = e2.empno;")
        return cur.fetchall()

    # Creating worksheet
    def create_worksheet(results):
        # Creating xlsx file
        workbook = xlsxwriter.Workbook("q1.xlsx")
        worksheet = workbook.add_worksheet()

        # Adding column names
        worksheet.write("A1", "Employee No.")
        worksheet.write("B1", "Employee Name")
        worksheet.write("C1", "Manager Name")

        row = 1
        for empno, ename, mgrname in results:
            worksheet.write(row, 0, empno)
            worksheet.write(row, 1, ename)
            worksheet.write(row, 2, mgrname)
            row += 1
        return workbook

    try:
        cur, conn = connect()
        results = query(cur)
        workbook = create_worksheet(results)

    except:
        print("Database is not connected")

    finally:
        workbook.close()
        cur.close()
        conn.close()


if __name__ == '__main__':
    question_1()
