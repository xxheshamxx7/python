acceptable_coins = [25,10,5]
balance=0
while True:
    if balance==50 or balance>=50:
        print("YOU GOT COLA")
        balance -= 50
    print(f"balance is: {balance} SAR")
    print("Choose an option or write 'q' to exit:")
    print("0 - 25")
    print("1 - 10")
    print("2 - 5")
    Insert_Coin = input()
    if Insert_Coin == "q":
        print ("bye")
        break
    if Insert_Coin == "0":
        balance += 25
    elif Insert_Coin == "1":
        
        balance += 10
    elif Insert_Coin == "2":
        
        balance += 5
    else:
        print("bad coin")
        continue