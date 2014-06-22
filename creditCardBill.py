__author__ = 'jeredyang'

"""
PROBLEM 1: PAYING THE MINIMUM  (10 points possible)
Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment
required by the credit card company each month.

The following variables contain values as described below:

balance - the outstanding balance on the credit card
annualInterestRate - annual interest rate as a decimal
monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining balance, and print to screen something of
the format:

Month: 1
Minimum monthly payment: 96.0
Remaining balance: 4784.0

Be sure to print out no more than two decimal digits of accuracy - so print

Remaining balance: 813.41
instead of

Remaining balance: 813.4141998135

Finally, print out the total amount paid that year and the remaining balance at the end of the year in the format:

Total paid: 96.0
Remaining balance: 4784.0

A summary of the required math is found below:

Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

Note that the grading script looks for the order in which each value is printed out. We provide sample test cases
below; we suggest you develop your code on your own machine, and make sure your code passes the sample test cases,
before you paste it into the box below.

"""


def monthly_credit_balance(month, mon_balance, annual_interestrate, monthly_paymentrate):
    # balance - the outstanding balance on the credit card

    # annualInterestRate - annual interest rate as a decimal
    monthly_interest_rate = annual_interestrate / 12

    # monthlyPaymentRate - minimum monthly payment rate as a decimal
    minimum_monthly_payment = monthly_paymentrate * mon_balance

    # Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
    monthly_unpaid_balance = mon_balance - minimum_monthly_payment

    # Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
    updated_balance_each_month = monthly_unpaid_balance + monthly_unpaid_balance * monthly_interest_rate

    return month, minimum_monthly_payment, updated_balance_each_month


def yearly_credit_history(remain_balance, annual_interestrate, monthly_paymentrate):
    total_paid = 0

    for each_month in range(1, 13):
        month, minimum_monthly_payment, remain_balance = monthly_credit_balance(each_month, remain_balance,
                                                                                annual_interestrate,
                                                                                monthly_paymentrate)
        print "Month: " + str(month)
        print "Minimum monthly payment: " + str(round(minimum_monthly_payment, 2))
        print "Remaining balance: " + str(round(remain_balance, 2))

        total_paid += minimum_monthly_payment

    print "Total paid: " + str(round(total_paid, 2))
    print "Remaining balance: " + str(round(remain_balance, 2))


# Test Case 1:
# balance = 4213
# annualInterestRate = 0.2
# monthlyPaymentRate = 0.04
#
# yearly_credit_history(balance, annualInterestRate, monthlyPaymentRate)

# Test Case 2:
balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

yearly_credit_history(balance, annualInterestRate, monthlyPaymentRate)