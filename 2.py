import random

nums = ()

def get_numbers_ticket(min, max, quantity):
    while len(nums) < quantity:
        nums.add(random.randint(min, max))

get_numbers_ticket(1,10,3)
print(nums)




