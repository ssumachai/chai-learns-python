command = ""
started = False

while True:
    command = input('> ').lower()
    if command == 'help':
        print("""
start - to start the car
stop - top stop the car
quit - to exit
        """)
    elif command == 'start':
        if started:
            print('Car started...Ready to go!')
            started = True
        else:
            print('Car is already started!')
    elif command == 'stop':
        if started:
            print('Car Stopped.')
            started = False
        else:
            print('Car is already stopped!')
    elif command == 'quit':
        break
    else:
        print("I don't understand that")
