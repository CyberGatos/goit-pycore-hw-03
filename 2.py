import random

def get_numbers_ticket(min, max, quantity):
    nums = set() # створюю set для унікальності чисел
    if min > 0 and max <= 1000 and quantity <= max - min + 1: # перевіряю вхідні параметри
        while len(nums) < quantity: # цикл, що додає елементи, поки не = quantity
            nums.add(random.randint(min, max)) # додавання рандомних елементів до set nums
    return sorted(nums) # функція повертає відсортований список з елементів сету


lucky_ticket = get_numbers_ticket(1,1000,3)
print(lucky_ticket)


# хотів зробити таку обробку на випадок, якщо вписати у параметри функції букву, але не зміг(
    #except NameError or ValueError:
    #    print("""
    #        Use only int
    #        Min > 0
    #        Max <= 1000
    #        Quantity <= max - min + 1
    #    """)
   