

def remain_balance(balance,annualInterestRate,monthlyPaymentRate):
    for i in range(12):
        monthlyInterestRate = annualInterestRate / 12.0
        minimumMonthlyPayment = monthlyPaymentRate * balance
        monthlyUnpaidBalance = balance - minimumMonthlyPayment
        balance = monthlyUnpaidBalance + (monthlyInterestRate*monthlyUnpaidBalance)
        print("Remaining balance: %.2f"%balance)    



balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04


remain_balance(balance, annualInterestRate,monthlyPaymentRate )
