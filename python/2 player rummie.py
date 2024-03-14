def fun():
    j=input("count:")
    return int(j)
def check(count):
    print (count)
    if count>200:
        return False
    else:
        return True

x=True
y=True
sum1=0
sum2=0
while x and y:
    print("player1")
    input1=fun()
    print("player2")
    input2=fun()
    sum1+=input1
    sum2+=input2
    x=check(sum1)
    y=check(sum2)
    if y==False and x:
        print("player1 wins")
    elif x==False and y:
        print("player2 wins")
    else:
        continue





