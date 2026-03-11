from postgres_db import insert_employee
from mongo_db import save_employee
from utils import generate_employee_id

last_id = None

def create_employee(data):

    global last_id

    emp_id = generate_employee_id(last_id)
    last_id = emp_id

    employee = {
        "employee_id": emp_id,
        "employee_name": data["employee_name"],
        "department": data["department"],
        "skills": data["skills"]
    }

    insert_employee(employee)

    save_employee(employee)

    return employee