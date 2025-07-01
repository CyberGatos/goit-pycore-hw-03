from datetime import timedelta, datetime # пишу цей код 01.07

users = [
    {"name": "Andriy", "birthday": "1995.07.24"}, # ДН який ще буде, але не найближчі 7 днів
    {"name": "Anton", "birthday": "1992.07.04"}, # який буде у будній день найближчі 7 днів
    {"name": "Igor", "birthday": "1993.07.06"}, # який буде у вихідний найближчі 7 днів
    {"name": "Brandon", "birthday": "1993.06.15"} # який був
    ]

def get_upcoming_birthdays(users): # оголошую функцію
    today = datetime.today().date() # задаю сьогоднішню дату у змінну
    bday_soon = [] # створбб пустий список для виведення
    
    for user in users: # проходжуся по кожному словнику у списку
        bday = datetime.strptime(user["birthday"], "%Y.%m.%d").date() # форматую рядок з датою у datetime
        bday_at_thisyear = bday.replace(year=today.year) # отримую дату дня народження у цьому році

        if bday_at_thisyear < today: # якшо ДН в цьому році вже був
           bday_at_thisyear = bday_at_thisyear.replace(year=today.year + 1) # ставлю актуальну дату майбутнього ДН

        days_until_bday = (bday_at_thisyear - today).days # створюю змінну у якій зберігається скільки днів до ДН
        weekday = bday_at_thisyear.weekday() # створюю змінну у якій зберігається день тижня для ДН

        if 0 <= days_until_bday <= 7: # якщо ДН у наступні 7 днів
            user_copy = user.copy() # створюю копію, шоб не змінити список users
            
            if weekday == 5: # якщо ДН у суботу
                bday_at_thisyear = bday_at_thisyear + timedelta(days=2) # виправляю дату на 2 дні вперед
            if weekday == 6: # якщо ДН у неділю
                bday_at_thisyear = bday_at_thisyear + timedelta(days=1) # виправляю дату на 1 день вперед
            
            user_copy["birthday"] = bday_at_thisyear.strftime("%Y.%m.%d") # форматую значення ключа з datetime на рядок
            user_copy["congratulation_date"] = user_copy.pop("birthday") # змінюю назву ключа перед занесенням у список 
            bday_soon.append(user_copy) # заношу результат (словник) у список

    return bday_soon # повертаю список словників

congrat_day = get_upcoming_birthdays(users)
print(congrat_day)





