card = ['A','J','Q','K']
path = []

def kfc(x):
    global cont
    if x == 5:
        print(path)
        if count_three():
            cont += 1
        return

    for i in range(4):
        path.append(card[i])
        kfc(x+1)
        path.pop()

def count_three():
    if path[0] == path[1] == path[2]:
        return True
    elif path[1] == path[2] == path[3]:
        return True
    elif path[2] == path[3] == path[4]:
        return True
    else:
        return False

cont = 0
kfc(0)
print(cont)