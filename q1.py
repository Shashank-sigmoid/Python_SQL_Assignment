import psycopg2
import xlsxwriter

workbook = None
conn = None
cur = None

try:
    # DB variables
    db_host = "localhost"
    db_name = "company"
    db_user = "postgres"
    db_pass = "SDstrange"

    # Connecting with the local server database
    conn = psycopg2.connect(dbname=db_name, user=db_user, password=db_pass, host=db_host)
    cur = conn.cursor()

    # Writing SQL query
    cur.execute("select e1.empno, e1.ename, e2.ename from emp e1, emp e2 where e1.mgr = e2.empno;")
    results = cur.fetchall()

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

except:
    print("Database is not connected")

finally:
    workbook.close()
    cur.close()
    conn.close()