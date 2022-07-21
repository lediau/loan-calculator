import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--type", choices=["diff", "annuity"], help='Incorrect parameters.')
parser.add_argument("-i1", "--principal")
parser.add_argument("-i2", "--periods")
parser.add_argument("-i3", "--interest")
parser.add_argument("-i4", "--payment")

args = parser.parse_args()

payment = None if args.payment is None else float(args.payment)
rate = None if args.interest is None else float(args.interest) / 1200
num = None if args.periods is None else int(args.periods)
principal = None if args.principal is None else float(args.principal)

if args.type == 'annuity':

    if (payment is None) + (rate is None) + (num is None) + (principal is None) > 1:
        print('Incorrect parameters.')
    else:
        if principal is None:
            principal = math.ceil(payment / ((rate * (1 + rate) ** num) / ((1 + rate) ** num - 1)))
            print(f'Your loan principal = {principal}!')
        elif payment is None:
            payment = math.ceil(principal * rate * (1 + rate) ** num / ((1 + rate) ** num - 1))
            print(f'Your monthly payment = {payment}!')
        elif num is None:
            num = math.ceil(math.log(payment / (payment - rate * principal), 1 + rate))
            year = num // 12
            month = num - year * 12
            print(f'It will take {year} years and {month} months to repay this loan!')
            print(f'Overpayment = {payment * num - principal}')

elif args.type == 'diff':

    if payment is None:
        over = 0
        for i in range(num):
            d = math.ceil(principal / num + rate * (principal - principal * i / num))
            over += d
            print(f'Month {i + 1}: payment is {d}')
        print(f'Overpayment = {over - principal}')
    else:
        print('Incorrect parameters.')
