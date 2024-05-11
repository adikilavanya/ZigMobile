# Sample database structure
database = {
    "colleges": {
        "Sri Chaitanya": {
            "Telangana": {
                "Hyderabad": {
                    "KPHB": {
                        "A": {
                            "students": [
                                {"id": 1, "name": "John", "section": "A", "marks": {"Math": 90, "Science": 85}},
                                {"id": 2, "name": "Alice", "section": "A", "marks": {"Math": 85, "Science": 80}}
                            ]
                        },
                        "B": {
                            "students": [
                                {"id": 3, "name": "Bob", "section": "B", "marks": {"Math": 95, "Science": 88}},
                                {"id": 4, "name": "Carol", "section": "B", "marks": {"Math": 88, "Science": 82}}
                            ]
                        }
                    }
                }
            }
        }
    }
}

# Sample authentication function
def authenticate(username, password):
    # You can implement authentication logic here
    # For simplicity, I'm just checking if username and password match
    return username == "admin" and password == "admin"

# Sample authorization function
def authorize(role, college, state=None, city=None, campus=None, section=None):
    # Role-based access control logic
    if role == "Super admin":
        return True
    elif role == "Admin" and college in database["colleges"]:
        return True
    elif role == "Teacher" and college in database["colleges"] and section is not None:
        return True
    elif role == "Student" and college in database["colleges"] and section is not None:
        return True
    return False

# Function to update data
def update_data(username, password, role, college, section, student_id, updated_data):
    if authenticate(username, password):
        if role == "Super admin" or (role == "Admin" and college in database["colleges"]):
            # Update data in the database based on the role and permissions
            # Here, 'updated_data' should contain the updated student details
            # Update the database accordingly
            for student in database["colleges"][college]["Telangana"]["Hyderabad"]["KPHB"][section]["students"]:
                if student["id"] == student_id:
                    student.update(updated_data)
                    return "Data updated successfully"
            return "Student not found"
        else:
            return "Unauthorized"
    else:
        return "Authentication failed"

# Function to delete data
def delete_data(username, password, role, college, section, student_id):
    if authenticate(username, password):
        if role == "Super admin" or (role == "Admin" and college in database["colleges"]):
            # Delete data from the database based on the role and permissions
            # Here, 'student_id' is the ID of the student to be deleted
            # Update the database accordingly
            students = database["colleges"][college]["Telangana"]["Hyderabad"]["KPHB"][section]["students"]
            for i, student in enumerate(students):
                if student["id"] == student_id:
                    del students[i]
                    return "Data deleted successfully"
            return "Student not found"
        else:
            return "Unauthorized"
    else:
        return "Authentication failed"

# Sample usage
username = input("Enter username: ")
password = input("Enter password: ")
role = input("Enter role: ")
college = input("Enter college: ")
section = input("Enter section: ")
student_id = int(input("Enter student ID to update/delete: "))

# Update data
if input("Do you want to update data? (yes/no): ").lower() == "yes":
    updated_data = {
        "name": input("Enter updated name: "),
        "section": input("Enter updated section: "),
        "marks": {"Math": int(input("Enter updated math marks: ")), "Science": int(input("Enter updated science marks: "))}
    }
    result = update_data(username, password, role, college, section, student_id, updated_data)
    print(result)

# Delete data
if input("Do you want to delete data? (yes/no): ").lower() == "yes":
    result = delete_data(username, password, role, college, section, student_id)
    print(result)
