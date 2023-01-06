from datetime import datetime

from application.db.people import get_empoyees
from application.salary import calculate_salary

if __name__ == '__main__':
    date = datetime.date(datetime.today())

    get_empoyees('Jeff Lebowski')
    calculate_salary('The Dude', 7, 40)

    print(f'\nThe current date: {date}')