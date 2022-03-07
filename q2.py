import psycopg2
import xlsxwriter

workbook = None
cur = None
conn = None

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
    cur.execute("select e1.ename, e1.empno, dept.dname, "
                "(extract(year from age(enddate, startdate))*12 + extract(month from age(enddate, startdate)))*e1.sal "
                "as Total_compensation, "
                "(extract(year from age(enddate, startdate))*12 + extract(month from age(enddate, startdate))) "
                "as Months "
                "from emp e1 join jobhist on e1.empno = jobhist.empno join dept on dept.deptno = jobhist.deptno;")
    results = cur.fetchall()

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

except:
    print("Database is not connected")

finally:
    workbook.close()
    cur.close()
    conn.close()