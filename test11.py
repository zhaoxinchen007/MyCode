def add(test):
    for i in range(len(test)):
        test[i] = test[i]+1
    return test

y = [1, 2, 3]
z = add(y)
print(z)
