class Result:
    def __init__(self, message, value=None):
        self.isSuccess = None
        self.message = message
        self.value = value

    def isOk(self):
        return self.isSuccess    

class Ok(Result):
    def __init__(self, message, value=None):
        super().__init__(message, value)
        self.isSuccess = True

class Error(Result):
    def __init__(self, message, value=None):
        super().__init__(message, value)
        self.isSuccess = False        

class BankAccount:
    def __init__(self, balance = 0):
        self.balance = balance

    def deposit(self, amount):
        """Money verification """
        self.balance += amount

    def tryWithdraw(self, amount):
        if(self.balance >= amount):
            self.balance -= amount
            return Ok("withdraw completed", amount)
        
        return Error("Not enough money...", amount)

    def __str__(self):
        return str(self.balance)