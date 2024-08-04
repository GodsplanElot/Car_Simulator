command = ""
started = False

while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("The car has started")
    elif command == "stop":
        if not started:
            print("car is already Stopped!")
        else:
            started = False
            print("the car has stoped")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit
        """)
    elif command == "quit":
        break
    else:
        print("I dont understand the command, enter 'help' to see the instruction list")


print ("***** car turned off Done*******")