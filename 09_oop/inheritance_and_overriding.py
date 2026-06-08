# Inheritance and Method Overriding Example

class Employee:

    def __init__(self, full_name="---", national_id="---"):
        self.full_name = full_name
        self.national_id = national_id

    def employee_info(self):
        print(
            "Employee Information:",
            self.full_name,
            "ID:",
            self.national_id
        )


employee1 = Employee("Erdinc", "125478")
employee1.employee_info()


class Manager(Employee):

    extra_salary = 0

    def __init__(
        self,
        full_name="---",
        national_id="---",
        position="Not Assigned"
    ):
        self.full_name = full_name
        self.national_id = national_id
        self.position = position

    # Method Overriding
    def employee_info(self):
        print(
            "Manager Information:",
            self.full_name,
            "ID:",
            self.national_id,
            "Position:",
            self.position
        )


employee2 = Employee("Mustafa", "789456")
employee2.employee_info()

manager1 = Manager()
manager1.employee_info()

manager2 = Manager("Mehmet", "159874", "Director")
manager2.employee_info()
