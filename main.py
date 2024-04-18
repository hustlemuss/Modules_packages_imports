from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime

def main():
    print("Текущая дата:", datetime.now())
    print("Вызываем функцию get_employees():")
    employees = get_employees()
    print("Список сотрудников:", employees)

    print("\nВызываем функцию calculate_salary() для каждого сотрудника:")
    for employee in employees:
        employee_id = employee[0]
        salary = calculate_salary(employee_id)
        print(f"Зарплата сотрудника {employee_id}: {salary}")

if __name__ == '__main__':
    main()
