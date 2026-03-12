import psycopg2
from config import POSTGRES_CONFIG


def save_employee_postgres(data):

    conn = psycopg2.connect(**POSTGRES_CONFIG)

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO employees (employee_id,name,department,skills) VALUES (%s,%s,%s,%s)",
        (
            data["Employee_ID"],
            data["Employee_Name"],
            data["Department"],
            data["Skill_Set"],
        ),
    )

    conn.commit()

    cursor.close()
    conn.close()