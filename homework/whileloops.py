acceptable_coins = [25,10,5]
balance=0
while True:
    print("Choose an option or write 'q' to exit:")
    print("0 - 25")
    print("1 - 10")
    print("2 - 5")
    Insert_Coin = input()
    if Insert_Coin == "q":
        print ("bye")
        break
    if Insert_Coin == "0":
        print(f"balance is: {balance+25} SAR")
        
    elif Insert_Coin == "1":
        print(f"balance is: {balance+10} SAR")
    elif Insert_Coin == "2":
        print(f"balance is: {balance+5} SAR")
    else:
        print("bad coin")
        continue