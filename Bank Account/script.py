from bankaccount import BankAccount

account = BankAccount(1000)

print(" 1 - DEPOSIT", "\n", "2 - WITHDRAWAL")
decision = int(input())

if decision == 1:
    print("Amount to deposit: ")
    amount = int(input())
    account.deposit(amount)

if decision == 2:
    print("Amount to withdrawal: ")
    amount = int(input())
    result = account.tryWithdraw(amount)

    if(result.isOk):
        print(result.message)
    else:
        print(result.message)

print("Your balance is: ", account)    
