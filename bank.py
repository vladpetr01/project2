# The program is designed for users interested in
# the calculation of credit conditions.
# Once the user has selected the purpose of the loan,
# the amount and term. The program calculates the monthly
# payment amount and the overpayment amount(in USD).

print('Какова ваша цель кредита?\nВыберите один из предложенный'
      ' вариантов:\n1.Учёба\n2.Покупка авто\n3.Ипотека')
aim = int(input())
print('Какую сумму вы хотите взять в кредит?')
money = int(input())
print('На какой срок?(месяца)')
month = int(input())

if money < 300_000:
    study = money / month * 2
    car = money / month * 2.5
    mortgage = money / month * 3

elif 300_000 < money < 1_000_000:
    study = money / month * 1.5
    car = money / month * 2
    mortgage = money / month * 2.5

else:
    study = money / month * 1.2
    car = money / month * 1.7
    mortgage = money / month * 2.2

if aim == 1:
    print('Ежемесячный платёж:', study, 'USD')
    print('Заплаченые в итоге проценты:', study * month - money, 'USD')

elif aim == 2:
    print('Ежемесячный платёж:', car, 'USD')
    print('Заплаченые в итоге проценты:', car * month - money, 'USD')

else:
    print('Ежемесячный платёж:', mortgage, 'USD')
    print('Заплаченые в итоге проценты:', mortgage * month - money, 'USD')