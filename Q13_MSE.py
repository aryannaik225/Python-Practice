#Aryan Naik
num = input("Enter a big numbers: ")
raghav = []
for i in num:
    raghav.append(i)

sum=0
for i in range(len(raghav)):
    sum+=int(raghav[i])

print("Sum ==>" ,sum)
print("Average ==>" ,(sum/len(raghav)))