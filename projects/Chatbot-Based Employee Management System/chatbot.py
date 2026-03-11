import re

def extract_employee_data(text):

    name = None
    department = None
    skills = None

    name_match = re.search(r'employee\s(\w+)', text, re.IGNORECASE)
    department_match = re.search(r'in\s(\w+)\sdepartment', text, re.IGNORECASE)
    skills_match = re.search(r'skills\s(.+)', text, re.IGNORECASE)

    if name_match:
        name = name_match.group(1)


    if department_match:
        department = department_match.group(1)


    if skills_match:
        skills = skills_match.group(1) 


    return {
        "employee_name": name,
        "department": department,
        "skills": skills

    }       