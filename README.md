# employee-management-system-how-to-use-python-syntax-appropriately

This program implements a simple Employee Management System using Object-Oriented Programming (OOP) principles such as encapsulation, attributes, and instance methods. It allows users to manage employee details, including adding, removing, displaying, finding, and updating employee information.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Class Structure](#class-structure)
- [Usage](#usage)
- [Example](#example)
- [Conclusion](#conclusion)

## Overview
An entity is typically represented by a class. Attributes store or keep track of specific information about an entity and describe it. Encapsulation is the practice of bundling data (attributes) and methods (actions) that operate on that data into a single unit, typically a class.

- **Entity**: Employee
- **Attributes**: (e.g., an employee's name or salary)
- **Encapsulation**: Data (Attributes) + Behavior (Methods)
- **Instance Variable**: Stores unique data for an instance (e.g., `self.name`, `self.salary`)
- **Instance Method**: Functions inside a class that operate on instance variables (e.g., `def update_salary(self, new_salary):`)

## Features
1. Add Employee
2. Remove Employee
3. Display All Employees
4. Find Employee by ID
5. Update Salary
6. Change Department
7. Exit

## Class Structure

### `class Employee`
- **Attributes**:
  - `emp_id`
  - `name`
  - `age`
  - `department`
  - `salary`
- **Methods**:
  - `display_details(self)`
  - `update_salary(self, new_salary)`

### `class EmployeeManager`
- **Attributes**:
  - `employees` (list of `Employee` instances)
- **Methods**:
  - `add_employee(self, emp_id, name, age, department, salary)`
  - `remove_employee(self, emp_id)`
  - `display_all_employees(self)`
  - `find_employee(self, emp_id)`
  - `update_employee_salary(self, emp_id, new_salary)`

## Usage
1. Run the `main()` function to start the Employee Management System.
2. Follow the on-screen prompts to add, remove, display, find, or update employees.

## Example
```python
if __name__ == "__main__":
    main()
