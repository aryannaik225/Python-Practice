input_string = input()
n = int(input())
numbers = [int(num) for num in input_string.split(',')]
for i in range(n):
    temp = numbers[-1]
    for j in range(len(numbers)-1,0,-1):
        numbers[j] = numbers[j-1]
    numbers[j-1] = temp

i = 0
while i!=(len(numbers)-1):
    print(f"{numbers[i]},",end="")
    i+=1
print(numbers[i])