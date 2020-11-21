def printit(n):
    new = []
    for i in range(1, n+1):
        new.append(str(i))
    print("".join(new))
    return
        
    
if __name__ == '__main__':
    n = int(input())
    printit(n)
