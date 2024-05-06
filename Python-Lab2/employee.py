from db import get_database_connection

class Employee:
    __employees = []

    def __init__(self, id, first_name, last_name, age, department, salary):
        """Initializes a new employee and inserts their data into the database."""
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.department = department
        self.salary = salary
        self.__class__.__employees.append(self)
        
        self.insert_into_db()

    def insert_into_db(self):
        """Inserts the employee's data into the database."""
        connection = get_database_connection()
        if connection is not None:
            cur = connection.cursor()
            cur.execute(
                "INSERT INTO employee (id, first_name, last_name, age, department, salary) VALUES (%s, %s, %s, %s, %s, %s)",
                (self.id, self.first_name, self.last_name, self.age, self.department, self.salary),
            )
            connection.commit()
            connection.close()

    def transfer(self, department):
        """Updates the employee's department in the database."""
        self.department = department
        connection = get_database_connection()
        if connection is not None:
            cur = connection.cursor()
            cur.execute(
                "UPDATE employee SET department = %s WHERE id = %s",
                (self.department, self.id),
            )
            connection.commit()
            connection.close()

    def fire(self):
        """Removes the employee from the list and deletes their data from the database."""
        self.__class__.__employees.remove(self)
        connection = get_database_connection()
        if connection is not None:
            cur = connection.cursor()
            cur.execute(
                "DELETE FROM employee WHERE id = %s",
                (self.id,),
            )
            connection.commit()
            connection.close()

    def show(self):
        """Prints the employee's details."""
        print(f"ID: {self.id}, Name: {self.first_name} {self.last_name}, Age: {self.age}, Department: {self.department}, Salary: {self.salary}")

    @classmethod
    def list_employees(cls):
        """Fetches and prints all employees from the database."""
        connection = get_database_connection()
        if connection is not None:
            cur = connection.cursor()
            cur.execute("SELECT * FROM employee")
            employees_data = cur.fetchall()
            for data in employees_data:
                print(f"ID: {data[0]}, Name: {data[1]} {data[2]}, Age: {data[3]}, Department: {data[4]}, Salary: {data[5]}")
            connection.close()

    @classmethod
    def get_employees(cls):
        """Returns the list of all employee objects."""
        return cls.__employees

    @classmethod
    def get_employee_count(cls):
        """Returns the count of current employees."""
        return len(cls.__employees)

    @classmethod
    def get_employee_by_id(cls, emp_id):
        """Finds an employee by their ID."""
        for emp in cls.__employees:
            if emp.id == emp_id:
                return emp
        return None