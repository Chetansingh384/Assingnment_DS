name = input("plz enter your name:- ")

print("helo",name)

message = """"

how may i help you 

Please select any of them option,
Type 1 >>>> CHECK BALANCE.
Type 2 >>>> DEPOSIT.
Type 3 >>>> WITHDRAWL."""

print(message)

task = int(input("plz enter your task:- "))
av_amount = 5000
if task >=1 and  task <=3:
    print("weclome to atm")
    if task == 1:
        print("your amount is :", av_amount)
    elif task == 2:
        dep_amount = int(input("plz enter amount:- "))
        if dep_amount > 500:
            total = dep_amount + av_amount
            total == av_amount
            print("your update amount is:-",total)
            print("your amount is :", total)
        else:
            print("please bring more amount:- ")
    else:
        wid_amount = int(input("plz enter amount:- "))
        if av_amount < wid_amount:
            print("you can not withdrae your balance is low", av_amount)
        else:
            av_amount = av_amount-wid_amount
            print("your amount is debet")
            print("your avli balcnce is :-", av_amount)    
else:
    print("please select in betweent 1 to 3")    