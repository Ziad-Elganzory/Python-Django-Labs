from employee import Employee
from db import get_database_connection

class Manager(Employee):
    def __init__(self, id, first_name, last_name, age, department, salary, managed_department):
        """Initializes a new manager and sets their managed department."""
        super().__init__(id, first_name, last_name, age, department, salary)
        self.managed_department = managed_department
        self.update_managed_department()

    def update_managed_department(self):
        """Updates the managed department of the manager in the database."""
        connection = get_database_connection()
        if connection is not None:
            cur = connection.cursor()
            cur.execute(
                "UPDATE employee SET managed_department = %s WHERE id = %s",
                (self.managed_department, self.id),
            )
            connection.commit()
            connection.close()

    def show(self):
        """Prints the manager's details, hiding their salary."""
        print(f"ID: {self.id}, Name: {self.first_name} {self.last_name}, Age: {self.age}, Department: {self.department}, Salary: confidential, Managed Department: {self.managed_department}")
