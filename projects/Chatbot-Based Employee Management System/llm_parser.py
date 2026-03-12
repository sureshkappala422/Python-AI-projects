def parse_user_input(message):

    parts = message.split(",")

    name = parts[0].strip()
    department = parts[1].strip()
    skills = parts[2].strip()

    return {
        "name": name,
        "department": department,
        "skills": skills
    }