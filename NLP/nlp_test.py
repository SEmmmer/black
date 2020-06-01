def sushu(n):
    if_su = False
    for i in range(n):
        i = i + 2
        if n % i == 0:
            if_su = False
            break
        else:
            if_su = True
    return if_su


print(sushu(17))
