import re

phone_number = ["    +38(050)123-32-34",
"     0503451234",
"+050 (459) 52-3333"
"(050)8889900",
"38050-111-22-22",
"38050 111 22 11   ",
"8Oo(96) 32-2199",]

def normalize_phone(phone_number): # оголошую функцію
    pre_edit = phone_number.lower() # обробляю випадок, у якому замість 0 гіу додумався поставти літеру о
    pre_edit = pre_edit.replace('o', '0').replace('о', '0') # замінюю на 0
    pre_edit = re.sub(r"[^\d+]", "", pre_edit) # видаляю усі символи окрім цифр та +
    
    if pre_edit.startswith("+38") and len(re.sub(r"\D", "", pre_edit)) == 12: # якщо номер співпадає з потрібним форматом
        return pre_edit
    elif pre_edit.startswith("380") and len(pre_edit) == 12: # якщо номер починається з 380
        return "+" + pre_edit # додаю + на початок
    elif pre_edit.startswith("0") and len(pre_edit) == 10: # якщо номер починається з 0
        return "+38" + pre_edit # додаю код +38
    elif pre_edit.startswith("80"): # якщо починається з 80
        return "+3" + pre_edit # додаю +3

ready_to_sanding = [normalize_phone(num) for num in phone_number] # передаю змінній значення результату перебору через функцію всіх номерів у списку
print(ready_to_sanding)

