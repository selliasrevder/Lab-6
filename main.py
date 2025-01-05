class Employee:
    def __init__(self, hours_worked, rate, bonus_coefficient):
        if hours_worked < 0 or rate < 0 or bonus_coefficient < 0:
            raise ValueError("All values must be non-negative.")
        self.hours_worked = hours_worked
        self.rate = rate
        self.bonus_coefficient = bonus_coefficient

    def calculate_bonus(self):
        return self.hours_worked * self.rate * self.bonus_coefficient

    def salary_per_hour(self):
        if self.hours_worked == 0:
            return 0 
        return (self.hours_worked * self.rate + self.calculate_bonus()) / self.hours_worked


class SeniorEmployee(Employee):

    def __init__(self, hours_worked, rate, bonus_coefficient, seniority_years):
        super().__init__(hours_worked, rate, bonus_coefficient)
        self.seniority_years = seniority_years


    def calculate_bonus(self):
        return super().calculate_bonus() * (1 + self.seniority_years * 0.05)


class Director(Employee):

    def __init__(self, hours_worked, rate, bonus_coefficient, department_size):
        super().__init__(hours_worked, rate, bonus_coefficient)
        self.department_size = department_size 

    def calculate_bonus(self):
        return super().calculate_bonus() * (1 + self.department_size * 0.01) 


    def salary_per_hour(self):
      base_salary = self.hours_worked * self.rate
      total_bonus = self.calculate_bonus()
      return (base_salary + total_bonus) / self.hours_worked if self.hours_worked >0 else 0


employee = Employee(160, 100, 0.1)
print(f"Зарплата сотрудника: {employee.hours_worked * employee.rate + employee.calculate_bonus()}")
print(f"Премия сотрудника: {employee.calculate_bonus()}")
print(f"Соотношение зарплата/час сотрудника: {employee.salary_per_hour()}")

senior_employee = SeniorEmployee(176, 120, 0.15, 5) 
print(f"Зарплата старшего сотрудника: {senior_employee.hours_worked * senior_employee.rate + senior_employee.calculate_bonus()}")
print(f"Премия старшего сотрудника: {senior_employee.calculate_bonus()}")
print(f"Соотношение зарплата/час старшего сотрудника: {senior_employee.salary_per_hour()}")

director = Director(160, 200, 0.2, 10)
print(f"Зарплата директора: {director.hours_worked * director.rate + director.calculate_bonus()}")
print(f"Премия директора: {director.calculate_bonus()}")
print(f"Соотношение зарплата/час директора: {director.salary_per_hour()}")