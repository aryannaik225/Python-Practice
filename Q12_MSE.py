#Aryan Naik
mylist = []

size = int(input("Enter the number of elements: "))
for i in range(size):
    mylist.append(int(input("Enter element: ")))

print(mylist)

search = int(input("Enter the element to be searched: "))

for i in range(size):
    if mylist[i] == search:
        print(search, "found at position ",i)
        count = 0
        break
    else:
        count = 1

if count == 1:
    print(search, " not found")


# for i in range(size):
#     if int(mylist[i]) == search:
#         print(search, " found at position ", i)
#         break
# else: 
#     print(search, " not found")