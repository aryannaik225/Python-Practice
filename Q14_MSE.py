#Aryan Naik
#14. Wap to create a dictionary with cricket players names
#and scores in matches . also retrieve runs by entering 
#players name

size = int(input("Enter number of players: "))
match = int(input("Enter the number of matches the players played: "))
player_dict = {}
#dict[player_name] = []
#dict[player_name].append(runs)
for i in range(size):
    player_name = input("Player {} name: ".format(i+1))
    player_dict[player_name] = []
    for j in range(match):
        runs = int(input("Enter the number of runs in match {}:".format(j+1)))
        player_dict[player_name].append(runs)

print(player_dict)

search = input("Enter the name of the player to search: ")

if search in player_dict:
    print(player_dict[search])
else:
    print("Player not found!")