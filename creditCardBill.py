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
# balance = 4842
# annualInterestRate = 0.2
# monthlyPaymentRate = 0.04
#
# yearly_credit_history(balance, annualInterestRate, monthlyPaymentRate)

"""
PROBLEM 2: PAYING DEBT OFF IN A YEAR  (15 points possible)
Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance
within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead
is a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year,
for example:

Lowest Payment: 180

Assume that the interest is compounded monthly according to the balance at the end of the month (after the payment
for that month is made). The monthly payment must be a multiple of $10 and is the same for all months. Notice that it
is possible for the balance to become negative using this payment scheme, which is okay. A summary of the required
math is found below:

Monthly interest rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

"""


def monthly_balance(remain_balance, monthly_interest_rate, minimum_monthly_payment):
    monthly_unpaid_balance = remain_balance - minimum_monthly_payment
    updated_monthly_balance = monthly_unpaid_balance + monthly_interest_rate * monthly_unpaid_balance

    return updated_monthly_balance


def yearly_balance(initial_balance, annual_interest_rate, minimum_monthly_payment):
    remain_balance = initial_balance
    monthly_rate = annual_interest_rate / 12
    for each_month in range(1, 13):
        remain_balance = monthly_balance(remain_balance, monthly_rate, minimum_monthly_payment)

    return remain_balance


def find_lowest_payment(initial_balance, annual_interest_rate):
    # define precision
    eps = 0.001

    monthly_lowest_payment = 0
    # when total paid is less than balance
    while monthly_lowest_payment < initial_balance:
        remain_balance = initial_balance
        monthly_lowest_payment += 10
        remain_balance = yearly_balance(remain_balance, annual_interest_rate, monthly_lowest_payment)
        if remain_balance < eps:
            break

    return monthly_lowest_payment


# Test Case 1:
# balance = 3329
# annualInterestRate = 0.2

# Test Case 2:
# balance = 4773
# annualInterestRate = 0.2

# # Test Case 3:
# balance = 3926
# annualInterestRate = 0.2

#print "Lowest Payment: " + str(find_lowest_payment(balance, annualInterestRate))

"""
PROBLEM 3: USING BISECTION SEARCH TO MAKE THE PROGRAM FASTER (25 points possible)
You'll notice that in Problem 2, your monthly payment had to be a multiple of $10. Why did we make it that way?
You can try running your code locally so that the payment can be any dollar and cent amount (in other words, the
monthly payment is a multiple of $0.01). Does your code still work? It should, but you may notice that your code
runs more slowly, especially in cases with very large balances and interest rates. (Note: when your code is running
on our servers, there are limits on the amount of computing time each submission is allowed, so your observations
from running this experiment on the grading system might be limited to an error message complaining about too
much time taken.)

Well then, how can we calculate a more accurate fixed monthly payment than we did in Problem 2 without running into
the problem of slow code? We can make this program run faster using a technique introduced in lecture - bisection
search!

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

To recap the problem: we are searching for the smallest monthly payment such that we can pay off the entire balance
within a year. What is a reasonable lower bound for this payment value? $0 is the obvious answer, but you can do
better than that. If there was no interest, the debt can be paid off by monthly payments of one-twelfth of the
original balance, so we must pay at least this much every month. One-twelfth of the original balance is a good lower
bound.

What is a good upper bound? Imagine that instead of paying monthly, we paid off the entire balance at the end of the
year. What we ultimately pay must be greater than what we would've paid in monthly installments, because the interest
was compounded on the balance we didn't pay off each month. So a good upper bound for the monthly payment would be
one-twelfth of the balance, after having its interest compounded monthly for an entire year.

In short:

Monthly interest rate = (Annual interest rate) / 12.0
Monthly payment lower bound = Balance / 12
Monthly payment upper bound = (Balance x (1 + Monthly interest rate)^12) / 12.0

Write a program that uses these bounds and bisection search (for more info check out the Wikipedia page on bisection
search) to find the smallest monthly payment to the cent (no more multiples of $10) such that we can pay off the debt
within a year. Try it out with large inputs, and notice how fast it is (try the same large inputs in your solution to
Problem 2 to compare!). Produce the same return value as you did in Problem 2.

Note that if you do not use bisection search, your code will not run - your code only has 30 seconds to run on our
servers.

"""


def get_monthly_lowest_payment(monthly_lowest_payment_low_limit, monthly_lowest_payment_up_limit):
    result = (monthly_lowest_payment_up_limit + monthly_lowest_payment_low_limit) / 2
    return result


def find_lowest_payment_bisec(initial_balance, annual_interest_rate):
    # define precision
    eps = 0.001

    # set initial limits
    monthly_lowest_payment_low_limit = initial_balance / 12
    monthly_lowest_payment_up_limit = initial_balance * (1 + annual_interest_rate / 12) ** 12 / 12

    monthly_lowest_payment_initial_up_limit = monthly_lowest_payment_up_limit
    monthly_lowest_payment = 0

    # when total paid is less than balance
    while monthly_lowest_payment < monthly_lowest_payment_initial_up_limit:
        remain_balance = initial_balance
        monthly_lowest_payment = get_monthly_lowest_payment(monthly_lowest_payment_low_limit,
                                                            monthly_lowest_payment_up_limit)
        remain_balance = yearly_balance(remain_balance, annual_interest_rate, monthly_lowest_payment)
        if 0 < remain_balance < eps:
            break
        elif remain_balance < 0:
            # paid too much each month
            monthly_lowest_payment_up_limit = monthly_lowest_payment
        else:
            # paid too little
            monthly_lowest_payment_low_limit = monthly_lowest_payment

    return monthly_lowest_payment


# Test Case 1:
# balance = 320000
# annualInterestRate = 0.2

# Test Case 2:
# balance = 999999
# annualInterestRate = 0.18

print "Lowest Payment: " + str(round(find_lowest_payment_bisec(balance, annualInterestRate), 2))