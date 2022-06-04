from application.salary import calculate_salary as salary
from application.db.people import get_employees
from datetime import datetime as dt

if __name__ == '__main__':
    salary()
    get_employees()
    print(dt.now())
