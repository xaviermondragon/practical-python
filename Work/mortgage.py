# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months_required = 0
extra_payment_start_month = int(input('Enter extra payment starting month: '))
extra_payment_end_month = int(input('Enter extra payment end month: '))
extra_payment = int(input('Enter extra payment: '))


while principal > 0:
    months_required += 1
    monthly_payment = payment
    principal *= 1 + rate / 12

    if extra_payment_start_month <= months_required <= extra_payment_end_month:
        monthly_payment += extra_payment

    if monthly_payment >= principal:
        print('We\'ve done it!')
        monthly_payment = principal

    principal -= monthly_payment
    total_paid += monthly_payment

    print(months_required, total_paid, principal)


print('Total paid', total_paid)
print('Months required', months_required)
