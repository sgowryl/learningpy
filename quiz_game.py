print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()


print("okay lets play")

answer = input("what does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("You are corrrect")
else:
    print('Incorrect')