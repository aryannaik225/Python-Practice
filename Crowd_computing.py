# you have a jar of lets say x numb of gems
# you go around and ask the crowd to estimate the number of gems in the jar
# we have to note down all the responses and then write a program to 
# trim the minimum and maximum 10% of the responses, 
# and then find the mean of the remaining responses to get our estimated number of gems in the jar
from statistics import mean

estimated_list = [150, 200, 180, 220, 160, 190, 205, 175, 210, 195, 185, 225, 170, 240, 155, 230, 245, 165, 235, 215, 250, 140, 270, 130, 260, 120, 280, 110, 290, 100, 300, 90, 310, 80, 320, 70, 330, 60, 340, 50, 350, 40, 360, 30, 370, 20, 380, 10, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650]

#got 75 responses from the crowd

estimated_list.sort()

trim = int(0.1*len(estimated_list))
estimated_list = estimated_list[trim:len(estimated_list)-trim]

print("The estimated number of gems in the jar is",mean(estimated_list))