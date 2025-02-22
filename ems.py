# An entity is typically represented by a class
# Attributes store or keep track specific information about an entity and describe.
# Encapsulation is the practice of bundling data (attributes) and methods (actions) that operate on that data into a single unit, typically a class. 


# Entity -> Empoloyee
# Attributes -> (e.g., an employee's name or salary).
# Encapsulation = Data (Attributes) + Behavior (Methods) 
# Instance Variable =  (Parameter) right
# Instance Method = (Function) inside a class that operates on instance variables.

"""
Instance (Object)	A real object based on the class	emp1 = Employee("Alice", 50000)
Instance Variable	Stores unique data for an instance	self.name, self.salary
Instance Method	Operates on instance variables	def update_salary(self, new_salary):
"""
class Employee:
    def __init__(self, emp_id, name, age, department, salary):
        self.emp_id = emp_id  # Attribute, 
        self.name = name
        self.age = age
        self.department = department
        self.salary = salary

    def display_details(self):
        print(f" Employee ID: {self.emp_id}, Name: {self.name}, Age: {self.age}, Department: {self.department}, Salary: ${self.salary} ")

    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"Salary for {self.name} updated to ${self.salary}\n")


# EmployeeManager class
class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp_id, name, age, department, salary):
        # When add_employee() is called , it creates an instance of the Employee class 
        # create an instance (object) of the Employee class
        new_employee = Employee(emp_id, name, age, department, salary) 
        self.employees.append(new_employee)
        print(f"Employee {name} added successfully.\n")

    def remove_employee(self, emp_id):
        for emp in self.employees:
            # (emp.emp_id) matches the emp_id
            if emp.emp_id == emp_id:
                # emp is a reference to the individual employee object in each iteration of the loop.
                self.employees.remove(emp)
                print(f"Employee ID {emp_id} removed successfully.\n")
                return
        print(f"Employee ID {emp_id} not found.\n")

    def display_all_employees(self):
        if not self.employees:
            print("No employees in the system.\n")
        else:
            print("Current Employees:\n")
            for emp in self.employees:
                emp.display_details()

    def find_employee(self, emp_id):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                print(f"Details of Employee ID {emp_id}:")
                emp.display_details()
                return emp
        print(f"Employee ID {emp_id} not found.\n")
        return None

    def update_employee_salary(self, emp_id, new_salary):
        for e in self.employees:
            if e.id == id: 
                e.update_salary(new_salary)
                print(f"Salary for {e.name} updated to ${new_salary}")
                return
            else:
                print(f"Employee with ID {id} not found.")


# Main function
def main():
    manager = EmployeeManager()  # Creates an instance of the EmployeeManager

    while True:
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. Display All Employees")
        print("4. Find Employee by ID")
        print("5. Update Salary")
        print("6. Change Department")
        print("7. Exit")

        try:
            choice = int(input("\nEnter your choice (1-7): "))

            if choice == 1:
                emp_id = int(input("Enter Employee ID: "))
                name = input("Enter Employee Name: ")
                age = int(input("Enter Employee Age: "))
                department = input("Enter Employee Department: ")
                salary = float(input("Enter Employee Salary: "))
                manager.add_employee(emp_id, name, age, department, salary)

            elif choice == 2:
                emp_id = int(input("Enter Employee ID to remove: "))
                manager.remove_employee(emp_id)

            elif choice == 3:
                manager.display_all_employees()

            elif choice == 4:
                emp_id = int(input("Enter Employee ID to find: "))
                manager.find_employee(emp_id)

            elif choice == 5:
                emp_id = int(input("Enter Employee ID to update salary: "))
                new_salary = float(input("Enter the new salary: "))
                manager.update_employee_salary(emp_id, new_salary)

            elif choice == 7:
                print("Exiting Employee Management System.")
                break

            else:
                print("Invalid choice. Please choose between 1 and 7.\n")

        except ValueError:
            print("Invalid input! Please enter a number.\n")

        except Exception as e:
            print(f"An error occurred: {e}\n")


if __name__ == "__main__":
    main()
