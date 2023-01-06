from datetime import *

from application.db.people import *
from application.salary import *

if __name__ == '__main__':
    date = datetime.date(datetime.today())

    get_empoyees('Jeff Lebowski')
    calculate_salary('The Dude', 7, 40)

    print(f'\nThe current date: {date}')