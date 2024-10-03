name = input("What is your name?: ")

introduction = f"{name}, when you got on the flight back from your holiday in Borneo you thought you'd just snooze the whole way and wake up in the airport. "
introduction2 = f"The next thing you know you're hearing shouts of MAYDAY MAYDAY and suddenly the seat your sleeping on gets a lot less comfy as it's ripped out of the plane"
introduction3 = f"and you start to rapidly fall. Oh no! You're in a plane crash and are currently falling from 20 kilometres"

valid_answers = ["A","B","C"]

options_1 = ["Wait on the seat and hope that you don't die when you hit the ground",
             "Take off your jacket and use it as a parachute",
             "Pull out the inbuilt parachute in your chair and try to get it working"]
print(introduction, introduction2, introduction3)
count = 0
while count < len(options_1):
    print(f"Do you {valid_answers[count]}: {options_1[count]}")
    count = count +1
    
answer = ""
while not answer in valid_answers:
    answer = input("Choose A, B, or C")
    
if answer == "A":
    print("You cling tightly to your seat and really really hope it's enough of a cushion. It's not. You die. The End.")

elif answer == "B":
    options_2 = ["New option A",
             "New option B",
             "New option C"]
    print("That works")
    count = 0
    while count < len(options_1):
        print(f"Do you {valid_answers[count]}: {options_2[count]}")
        count = count +1
    answer = ""
    while not answer in valid_answers:
        answer = input("Choose A, B, or C")
    if answer == "A":
        print("you chose A, here's what happens!")
        
        options_3 = ["New option A",
                 "New option B",
                 "New option C"]
        print("That works")
        count = 0
        while count < len(options_1):
            print(f"Do you {valid_answers[count]}: {options_3[count]}")
            count = count +1
        answer = ""
        while not answer in valid_answers:
            answer = input("Choose A, B, or C")
        if answer == "A":
            print("you chose A, here's what happens!")
        elif answer == "B":
            print("you chose B, here's what happens!")
        elif answer == "C":
            print("you chose C, here's what happens!")

        
        
    elif answer == "B":
        print("you chose B, here's what happens!")
    elif answer == "C":
        print("you chose C, here's what happens!")

elif answer == "C":
    print("You try to get the parachute working, but sadly, you've never really had training in parachuting and this definietly wasn't covered by the flight attendent when she was talking about emergency exits. When you hit the ground you're still fumbling with the packaging.You die. The End.")