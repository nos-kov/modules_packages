from application.db.people import Employee
from application.salary import calculate_salary
from datetime import datetime
import requests

if __name__ == "__main__":
    new_emp = Employee("Tom", 19)
    print(datetime.today())
    print(new_emp.get_employees())
    print(calculate_salary(1,12))

    x = requests.get('https://netology.ru/')
    print(x.content[0])

