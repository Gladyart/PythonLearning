# StartStop Engine

engineStatus = False

while True:
    command = input("> ").lower()

    if command == "start": 
        if engineStatus == True:
            print("Engine already started..")
        else:
            print("Engine started..")
            engineStatus = True

    elif command == "stop":
        if engineStatus == True:
            print("Engine stopped..")
            engineStatus = False
        else:
            print("Engine alredy stopped..")

    elif command == "quit":
        print("Program stopped..")
        break
    else:
        print("Invalid command..")
