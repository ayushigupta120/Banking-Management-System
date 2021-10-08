from abc import ABC,abstractmethod
from random import randint
class bank(ABC):
    @abstractmethod
    def create_account(self):
         pass

    @abstractmethod
    def login(self):
         pass

    @abstractmethod
    def display_balance(self):
        pass

    @abstractmethod
    def deposit_amount(self,amount):
        pass

    @abstractmethod
    def withdraw_amount(self,amount):
        pass

    @abstractmethod
    def transfer_amount(self,name,account_no,amount):
        pass
    

class customer(bank):

    def __init__(self):
        self.customer_detail=[]
        self.balance=0


    def create_account(self,name,phone_no,deposit_amount):
        condition=True
        if len(str(phone_no))>10 and len(str(phone_no))<10 :
            print("Invalid phone number ! please enter 10 digit number")
            condition=False

        if condition==True:
            self.account_no=randint(100000,999999)
            self.balance=deposit_amount
            self.customer_detail=[name,phone_no,deposit_amount,self.account_no]
            print("Account created successfully")
            print("Your account number is ",self.account_no)
            with open (f'{name}.txt','w') as fp:
                for details in self.customer_detail:
                    fp.write(str(details) + "\n" )

    def login(self,name,account_no):
        with open (f'{name}.txt','r') as fp:
            details=fp.read()
            self.customer_detail=details.split('\n')
            if name in self.customer_detail:
                if self.customer_detail[3] == str(account_no):
                    print('Login is successful!')
                    self.name=name
                    self.balance=self.customer_detail[2]
                    return True
                else:
                    print('Login failed!1234')
                    return False
            else:
                print('Login failed!')
                
                return False
        

    def display_balance(self):
        with open (f'{self.name}.txt','r') as fp:
            details=fp.read()
            self.customer_detail=details.split('\n')
            print('Balance in a/c:', self.customer_detail[2])


    def deposit_amount(self, amount):
        with open (f'{self.name}.txt','r') as fp:
            details=fp.read()
            self.customer_detail=details.split('\n')

        with open (f'{self.name}.txt','w') as fp: 
            new_balance=int(self.customer_detail[2]) + amount
            fp.write(details.replace(str(self.customer_detail[2]),str(new_balance)))
            print('Deposit was successful')
        self.display_balance()


    def withdraw_amount(self, amount):
        with open (f'{self.name}.txt','r') as fp:
            details=fp.read()
            self.customer_detail=details.split('\n')
        with open (f'{self.name}.txt','w') as fp:
            if amount <  int(self.customer_detail[2]):
                left_balance=int(self.customer_detail[2]) - amount
                fp.write(details.replace(str(self.customer_detail[2]),str(left_balance)))
                print('Withdraw successful')
                print('Balance in a/c ',left_balance)
            
            
            else:
                print('Insufficient Balance')


    def transfer_amount(self, name, account_no, amount):
        self.transfer_cash=False
        self.total_balance=False
        with open (f'{self.name}.txt','r') as fp:
            details=fp.read()
            self.customer_detail=details.split('\n')

        with open (f'{self.name}.txt','w') as fp:
            if amount <  int(self.customer_detail[2]):
                self.total_balance=True
                left_balance=int(self.customer_detail[2]) - amount
                fp.write(details.replace(str(self.customer_detail[2]),str(left_balance)))

            else:
                print('Insufficient Balance') 

        if self.total_balance == True:   
            with open (f'{name}.txt','r') as fp:
                details=fp.read()
                self.customer_detail=details.split('\n')
                if account_no == self.customer_detail[3]:
                    self.transfer_cash=True

            if self.transfer_cash == True:
                with open (f'{name}.txt','w') as fp: 
                    new_balance=int(self.customer_detail[2]) + amount
                    fp.write(details.replace(str(self.customer_detail[2]),str(new_balance)))
                    print('Transferred Successfully')
        self.display_balance()
        

customer_obj=customer()
while True:
    print('Welcome to Bank')
    print('Enter 1 to create account')
    print('Enter 2 to login account')
    print('Enter 3 to quit')
    choice=int(input())

    if choice==1:
        name=input('Enter your name ')
        phone_no=int(input('Enter your phone no '))
        deposit_amount=int(input('Enter the deposit amount '))
        customer_obj.create_account(name,phone_no,deposit_amount)

    elif choice==2:
        name=input('enter your name ')
        account_no=int(input('enter your account no '))
        login_status=customer_obj.login(name,account_no)
        loginin=True

        while loginin==True:
            if login_status==True:
                print('Enter 1 to check the balance ')
                print('Enter 2 to deposit the amount ')
                print('Enter 3 to withdraw the amount ')
                print('Enter 4 to transfer the cash')
                print('Enter 5 to logout')
                choice1=int(input())

                if choice1==1:
                    customer_obj.display_balance()

                elif choice1==2:
                    amount=int(input('Enter the amount to deposit '))
                    customer_obj.deposit_amount(amount)

                elif choice1==3:
                    amount=int(input('Enter the amount to withdraw '))
                    customer_obj.withdraw_amount(amount)

                elif choice1==4:
                    name=input('Enter the name of the accountholder on which money is to be transfered')
                    account_no=input('Enter the account number in which you want to transfer money')
                    amount=int(input('Enter the amount to be transfered'))
                    customer_obj.transfer_amount(name,account_no,amount)

                elif choice1==5:
                    loginin=False

            else:
                print('Try Again')

    elif choice==3:
        quit()



