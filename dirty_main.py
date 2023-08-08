from application.db.people import *
from application.salary import *

new_emp = Employee("Tom", 19)
print(new_emp.get_employees())
print(calculate_salary(1,12))