#Password_20201104
import random

def runMain(initial_num):
    startnum = 1
    endnum = 100
    inputnum = 0
    print("The PASSWORD for checking: ", initial_num, "\n" + "---"*10)
    while True:
        inputnum = int(input("The PASSWORD is in " + str(startnum) + " - " + str(endnum) + ".\nGuess the PASSWORD: "))
        if (str(inputnum).isdigit() and (inputnum >= startnum and inputnum <= endnum)):
            if (inputnum < initial_num):
                startnum = inputnum
            elif (inputnum > initial_num):
                endnum = inputnum
            elif (inputnum == initial_num):
                print("BINGO! The password is " + str(inputnum) + ".")
                break
            else:
                print("Please input valid number from " + str(startnum) + " to " + str(endnum) + ".")          
                
runMain(random.randint(1, 100))

