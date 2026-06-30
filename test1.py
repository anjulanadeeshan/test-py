N = int(input())

list = []

for i in range(N):
    command_data = input().split()
    command = command_data[0]

    if command == 'insert':
        list.insert(int(command_data[1]),int(command_data[2]))
    elif command == 'print':
        print(list)
    elif command == 'remove':
        list.remove(int(command_data[1]))
    elif command == 'append':
        list.append(int(command_data[1]))
    elif command == 'sort':
        list.sort()
    elif command == 'pop':
        list.pop()
    elif command == 'reverse':
        list.reverse()
    

