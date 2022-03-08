import psycopg2
import xlsxwriter


def question_4():
    """ Find department name, department no. and sum of total compensation """
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
        cur.execute("select nt.department_name, d.deptno, sum(nt.total_comp) from new_table nt, dept d "
                    "where d.dname = nt.department_name group by nt.department_name, d.deptno;")
        return cur.fetchall()

    # Creating worksheet
    def create_worksheet(results):
        # Creating xlsx file
        workbook = xlsxwriter.Workbook("q4.xlsx")
        worksheet = workbook.add_worksheet()

        # Adding column names
        worksheet.write("A1", "Department Name")
        worksheet.write("B1", "Department No.")
        worksheet.write("C1", "Total compensation")

        row = 1
        for dname, deptno, tcomp in results:
            worksheet.write(row, 0, dname)
            worksheet.write(row, 1, deptno)
            worksheet.write(row, 2, tcomp)
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
    question_4()
