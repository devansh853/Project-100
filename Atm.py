class Atm:
    def __init__(self,cardNumber,pin):
        self.cardnumber = cardNumber
        self.pin = pin
    def check_balance(self):
        print("Your balance 46000")
    def withdraw(self,amount):
       new_amount = 46000-amount
       print("you have withdrawn amount "+str(amount) +". Your remaining balance is "+ str(new_amount))
def main():
    card_number = input("inset your card number:-")
    pin_number = input("enter your pin number:->")
    new_user = Atm(card_number,pin_number)
    print("chose your activity")
    print("1.balance enqury : 2.withdraw ")
    activity = int(input("enter activity number:-"))
    if (activity == 1):
        new_user.check_balance() 
    elif (activity == 2):
        amount = int(input("enter the amount:- ")) 
        new_user.withdrawl(amount) 
    else:
        print("enter a valid number") 
if __name__ == "__main__":
   main()