def search(key, mylist, size):
    count = 0
    for i in range(size):
        if(mylist[i] == key):
            count=count+1
    if (count>=1):
        print(key, ' found')

size = int(input('Enter size of list: '))
mylist = []
sat = 0

for i in range(size):
    temp = input('Enter element: ')
    mylist.append(temp)

while(sat!=1): 
    key = input('Enter element to be seacrhed: ')
    search(key, mylist, size)
    sat = int(input('Are you satisfied? 1 or 0: '))