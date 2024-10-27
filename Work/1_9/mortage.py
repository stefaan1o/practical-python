# mortgage.py

principal = 500000.0
rate = 0.05
base_payment = 2684.11
total_paid = 0.0
counter = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    if counter >= extra_payment_start_month and counter <= extra_payment_end_month:
        extra = extra_payment
    else:
        extra = 0
    payment = base_payment + extra
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + base_payment + extra
    print(f'{counter:3d} {total_paid:10.2f} {principal:10.2f} {payment} ')
    counter += 1

print(f'Total paid = {total_paid:.2f}')