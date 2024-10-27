# mortgage.py

principal = 500000.0
rate = 0.05
base_payment = 2684.11
total_paid = 0.0
counter = 0

while principal > 0:
    extra = 1000 if counter < 12 else 0
    payment = base_payment + extra
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + base_payment + extra
    print(f'{counter:3d} {total_paid:10.2f} {principal:10.2f} {payment} ')
    counter += 1

print(f'Total paid = {total_paid:.2f}')