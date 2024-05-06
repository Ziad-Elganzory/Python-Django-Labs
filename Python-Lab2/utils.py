from db import get_database_connection

def get_employee_by_id(emp_id):
    """Fetches an employee by their ID from the database."""
    connection = get_database_connection()
    if connection is not None:
        cur = connection.cursor()
        cur.execute("SELECT * FROM employee WHERE id = %s", (emp_id,))
        emp = cur.fetchone()
        cur.close()
        connection.close()
        return emp
    else:
        return None

def list_all_employees():
    """Fetches and prints all employees from the database."""
    connection = get_database_connection()
    if connection is not None:
        cur = connection.cursor()
        cur.execute("SELECT * FROM employee")
        employees = cur.fetchall()
        cur.close()
        connection.close()
        for emp in employees:
            print(f"ID: {emp[0]}, Name: {emp[1]} {emp[2]}, Age: {emp[3]}, Department: {emp[4]}, Salary: {emp[5]}, Managed Department: {emp[6] if emp[6] else 'None'}")
        return employees
    else:
        print("Could not retrieve employees.")

def add_employee(role):
    """Prompts the user to enter employee details and creates an employee or manager based on the role."""
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    age = int(input("Age: "))
    department = input("Department: ")
    salary = int(input("Salary: "))

    connection = get_database_connection()
    if connection is not None:
        cur = connection.cursor()
        if role.lower() == 'm':
            managed_department = input("Managed Department: ")
            cur.execute(
                "INSERT INTO employee (first_name, last_name, age, department, salary, managed_department) VALUES (%s, %s, %s, %s, %s, %s)",
                (first_name, last_name, age, department, salary, managed_department)
            )
        else:
            cur.execute(
                "INSERT INTO employee (first_name, last_name, age, department, salary) VALUES (%s, %s, %s, %s, %s)",
                (first_name, last_name, age, department, salary)
            )
        connection.commit()
        cur.close()
        connection.close()
        print("Employee added successfully.")

def transfer():
    """Transfers an employee to a new department based on user input."""
    employees = list_all_employees()
    id = int(input("Enter the ID of the employee to transfer: "))
    emp = get_employee_by_id(id)
    if emp:
        new_department = input("Enter the new department: ")
        connection = get_database_connection()
        if connection is not None:
            cur = connection.cursor()
            cur.execute(
                "UPDATE employee SET department = %s WHERE id = %s",
                (new_department, id)
            )
            connection.commit()
            cur.close()
            connection.close()
            print("Employee transferred successfully.")
    else:
        print("Employee not found.")

def fire():
    """Fires an employee based on their ID."""
    employees = list_all_employees()
    id = int(input("Enter the ID of the employee to fire: "))
    emp = get_employee_by_id(id)
    if emp:
        connection = get_database_connection()
        if connection is not None:
            cur = connection.cursor()
            cur.execute("DELETE FROM employee WHERE id = %s", (id,))
            connection.commit()
            cur.close()
            connection.close()
            print("Employee fired successfully.")
    else:
        print("Employee not found.")

def show():
    """Displays the details of an employee by their ID."""
    id = int(input("Enter the ID of the employee to show: "))
    emp = get_employee_by_id(id)
    if emp:
        print(f"ID: {emp[0]}, Name: {emp[1]} {emp[2]}, Age: {emp[3]}, Department: {emp[4]}, Salary: {emp[5]}, Managed Department: {emp[6] if emp[6] else 'None'}")
    else:
        print("Employee not found.")