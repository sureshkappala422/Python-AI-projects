import random
from database_mongo import save_employee_mongo
from database_postgres import save_employee_postgres
from logger_config import logger


def generate_employee_id():

    return "EMP" + str(random.randint(1000, 9999))


def create_employee(name, department, skills):

    emp_id = generate_employee_id()

    employee = {
        "Employee_ID": emp_id,
        "Employee_Name": name,
        "Department": department,
        "Skill_Set": skills
    }

    save_employee_mongo(employee)

    try:
        save_employee_postgres(employee)
    except Exception as e:
        logger.error("Postgres insert failed")

    logger.info(f"Employee Created | {employee}")

    return employee