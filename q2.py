import psycopg2
import xlsxwriter


def question_2():
    workbook = None
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

    # Writing SQL query
    def query(cur):
        cur.execute("select e1.ename, e1.empno, dept.dname, "
                    "(extract(year from age(enddate, startdate))*12 + extract(month from age(enddate, startdate)))*e1.sal "
                    "as Total_compensation, "
                    "(extract(year from age(enddate, startdate))*12 + extract(month from age(enddate, startdate))) "
                    "as Months "
                    "from emp e1 join jobhist on e1.empno = jobhist.empno join dept on dept.deptno = jobhist.deptno;")
        return cur.fetchall()

    # Creating worksheet
    def create_worksheet(results):
        # Creating xlsx file
        workbook = xlsxwriter.Workbook("q2.xlsx")
        worksheet = workbook.add_worksheet()

        # Adding column names
        worksheet.write("A1", "Employee Name")
        worksheet.write("B1", "Employee No.")
        worksheet.write("C1", "Department Name")
        worksheet.write("D1", "Total compensation")
        worksheet.write("E1", "Total months")

        row = 1
        for ename, empno, dname, comp, months in results:
            worksheet.write(row, 0, ename)
            worksheet.write(row, 1, empno)
            worksheet.write(row, 2, dname)
            worksheet.write(row, 3, comp)
            worksheet.write(row, 4, months)
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
    question_2()
