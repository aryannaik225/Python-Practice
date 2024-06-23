# Raghu is a shoe shop owner. His shop has  number of shoes.
# He has a list containing the size of each shoe he has in his shop.
# There are  number of customers who are willing to pay  amount of money only if they get the shoe of their desired size.
# Your task is to compute how much money  earned.

# The first line contains , the number of shoes.
# The second line contains the space separated list of all the shoe sizes in the shop.
# The third line contains , the number of customers.
# The next  lines contain the space separated values of the  desired by the customer and , the price of the shoe.


from collections import Counter

shoes = int(input())
string = input()
sizes = string.split()

total = 0
customers = int(input())
for i in range(customers):
    c_info = input()
    c_list = c_info.split()
    c_size = c_list[0]
    c_cost = c_list[1]
    if c_size in sizes:
        total += int(c_cost)
        sizes.remove(c_size)

print(total)

#input:-
# 10
# 2 3 4 5 6 8 7 6 5 18
# 6
# 6 55
# 6 45
# 6 55
# 4 40
# 18 60
# 10 50

# output:-
# 200
