n = int(input())

contacts = {}

for _ in range(n):
    command = input().split()

    if command[0] == "ADD":
        contacts[command[1]] = command[2]

    elif command[0] == "REMOVE":
        if command[1] in contacts:
            del contacts[command[1]]

    elif command[0] == "DISPLAY":
        if not contacts:
            print("No contacts")
        else:
            for name in sorted(contacts):
                print(f"{name}: {contacts[name]}")
