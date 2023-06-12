print("Welcome to my quiz game!!")

playing = input("Do you want to play the game?")
if playing != "yes":
    quit()
print("Lets play !! ")
userInfo = input("Please enter your name")

score = 0
answer1 = input("What is the current year?")
if answer1 == "2023":
    print("correct!")
    score +=1
else:
    print("incorrect")

answer2 = input("What is our country name?")
if answer2 == "India":
    print("correct!")
    score +=1
else:
    print("incorrect")

answer3 = input("What is the full form of Esc key?")
if answer3 == "Escape":
    print("correct!")
    score +=1
else:
    print("incorrect")

answer4 = input("What is the current month?")
if answer4 == "June":
    print("correct!")
    score +=1
else:
    print("incorrect")

answer5 = input("Which date is the women's day?")
if answer5 == "8March":
    print("correct!")
    score +=1
else:
    print("incorrect")


print(userInfo, " your final score is", end=" ")
print(score, "answer corrected!")
