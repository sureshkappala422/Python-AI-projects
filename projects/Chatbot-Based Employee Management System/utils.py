def generate_employee_id(last_id):

    if last_id is None:
        return "EMP1001"
    
    num = int(last_id.replace("EMP",""))+1
    return f"EMP{num}"