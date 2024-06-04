# Take the number of elements and store it in variable.
size = int(input("Enter the number of variables: "))

# Take the element of each list one by one.
my_list = []
for i in range(size):
    my_list.append(int(input(f"Enter element {i}: ")))


# Use for loop to transverse through the elements of the list and check if the element is odd or even.
# If the element is even, append into a separate list and if it is odd append it to a different one
print(my_list)
print("")
even = []
odd = []
for i in range(size):
    if my_list[i]%2==0:
        even.append(my_list[i])
    elif my_list[i]%2==1:
        odd.append(my_list[i])
print(even)
print(odd)
print("")


# Use elif loop merge the two list and also sort the element into in it.
f_list = []
for i in range(len(even)):
    f_list.append(even[i])
for i in range(len(odd)):
    f_list.append(odd[i])
f_list.sort()
print("")
print(f_list)
print("")


# Accept the elements in the form of tuple like student roll no., Student Name and three subject marks
roll_no = int(input("Enter student roll number: "))
name = input("Enter student name: ")
marks_str = input("Enter student marks separated by space: ")
marks = list(map(int, marks_str.split()))


# Use for loop to transverse through the elements of the tuple find average and sum.
total = sum(marks)
average = total/len(marks)
print("")
print("Total marks: ", total)
print("Average marks: ", average)


print("")


# Use of elif loop for check whether the string python is present in it or not
string1 = input("Enter a long string: ")
if 'python' in string1.lower():
    print(f"Python was found in string '{string1}'")
else:
    print(f"Python was not found in string '{string1}'")


# For sort the tuple use sorted function. Using sorting function data is sorted by names
print("")
student_tuples = [(22, 'Aryan', 97), (35, 'Apeksha', 85), (16, 'Amruta', 90)]
print(student_tuples)
student_tuples = sorted(student_tuples, key=lambda x: x[1])
print(student_tuples)


print("")


# Create a Dictionary in python and print it.
my_dict = {"brand": "Ford",
            "model": "Mustang",
            "year": 1964}
print("Dictionary: ", my_dict)