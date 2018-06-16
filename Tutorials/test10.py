#addInterest3.py
def addInterest(amounts,rate):
    for i in range(len(amounts)):
        amounts[i]=amounts[i]*(1+rate)
def test():
    amounts=[1000,1323,124,124,124]
    rate=0.05
    addInterest(amounts,rate)
    print(amounts)
test()