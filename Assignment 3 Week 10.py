# {Train_name: {Compartment: No. of passengers}}

station_dict = {}
n = int(input("How many trains stop at the station?: "))

for i in range(n):
    train_name = input("Enter the {} train name: ".format(i+1))
    station_dict[train_name]={}
    m = int(input("Enter the number of compartments in {}: ".format(train_name)))
    for j in range(m):
        comp_name = input("Enter the name of the compartment no. {}: ".format(j+1))
        passenger = int(input("Enter the number of passengers in {}: ".format(comp_name)))
        station_dict[train_name][comp_name] = passenger

print(station_dict)