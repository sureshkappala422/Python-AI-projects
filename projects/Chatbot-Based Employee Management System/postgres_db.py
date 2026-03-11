import psycopg2

def get_connection():

    return psycopg2.connect(
        database="employee_db",
        user="postgres",
        password="password",
        host="localhost",
        port="5432"
    )


def insert_employee(emp):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO employees(employee_id, employee_name, department, skill_set)
    VALUES(%s,%s,%s,%s)
    """

    cursor.execute(query,(
        emp["employee_id"],
        emp["employee_name"],
        emp["department"],
        emp["skills"]
    ))

    conn.commit()
    cursor.close()
    conn.close()