#викликаю потрібні модулі
from datetime import timedelta, datetime

#оголошую функцію
def get_days_from_today(date):
    try:
        date_objct = datetime.strptime(date, "%Y-%m-%d") #форматую str to datetime
        date_now = datetime.today()
        delta = date_now - date_objct
        return delta.days #повертаю у днях
    except ValueError:
        return None #обробляю можливу помилку

date = input("Введіть дату у форматі YYYY-MM-DD>>> ") #оголошую змінну, яка після вводу стане параметром функції
result = get_days_from_today(date) # записую результат функції у змінну

while result is None: # зациклюю можливість введення правильного формату у випадку ValueError
    date = input("У ФОРМАТІ YYYY-MM-DD>>> ") # тут пропоную юзеру ввести нормально
    result = get_days_from_today(date) # знову викликаю функцію, щоб перевірити чи вона не повернула None

print(result) #так чи інакше приходимо на результат

#була ідея вшити цикл всередені функції на except, але тоді функція викликала б сама себе і мені здалося це тільки ускладнить