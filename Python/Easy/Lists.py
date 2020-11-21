#def insert():
    

if __name__ == '__main__':
    N = int(input())
    new = []
    for i in range(N):
        command = input()
        command = command.split()
        if command[0] == "insert":
            new.insert(int(command[1]), int(command[2]))
        elif command[0] == "print":
            print(new)
        elif command[0] == "remove":
            new.remove(int(command[1]))
        elif command[0] == "append":
            new.append(int(command[1]))
        elif command[0] == "sort":
            new.sort()
        elif command[0] == "pop":
            new.pop(-1)
        elif command[0] == "reverse":
            new.reverse()
