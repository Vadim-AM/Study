import argparse
from math import ceil, log


def head():
    parser = argparse.ArgumentParser(description='Loan Calculator')
    parser.add_argument('--type', choices=['annuity', 'diff'], help="choose the type of payments")
    parser.add_argument('--principal', type=float, help="input principal")
    parser.add_argument('--periods', type=int, help="input a number of periods")
    parser.add_argument('--interest', type=float, help="without a percent sign, a point-value accepted")
    parser.add_argument('--payment', type=float, help="input monthly payment")
    args = parser.parse_args()
    check(args)


def check(args):
    if args.interest is None:
        return print('Incorrect parameters')
    elif args.type == 'diff' and args.payment is not None:
        return print('Incorrect parameters')
    body(args)


def credit_time(rate, principal, pay):
    months_num = ceil(log((pay / (pay - rate * principal)), (1 + rate)))
    overpayment = int(pay * months_num - principal)
    if months_num == 1:
        print(f'It will take 1 month to repay this loan!')
    elif 1 < months_num < 12:
        print(f'It will take {months_num} months to repay this loan!')
    elif months_num == 12:
        print(f'It will take 1 year to repay this loan!')
    elif months_num % 12 == 0 and months_num / 12 > 1:
        print(f'It will take {int(months_num / 12)} years to repay this loan!')
    else:
        print(f'It will take {months_num // 12} years and {months_num % 12} months to repay this loan!')
    print(f'Overpayment = {overpayment}')


def annuity_payment(rate, principal, periods):
    payment = ceil(principal * ((rate * (1 + rate) ** periods) / ((1 + rate) ** periods - 1)))
    overpayment = int(payment * periods - principal)
    print(f'Your monthly payment = {payment}!')
    print(f'Overpayment = {overpayment}')


def diff_payment(rate, principal, periods):
    total = 0
    for month in range(1, periods + 1):
        payment = ceil(principal / periods + rate * (principal - principal * (month - 1) / periods))
        print(f'Month {month}: payment is {payment}')
        total += payment
    overpayment = int(total - principal)
    print(f'Overpayment = {overpayment}')


def loan_principal(rate, payment, periods):
    principal = round(payment / ((rate * (1 + rate) ** periods) / ((1 + rate) ** periods - 1)))
    print(f'Your loan principal = {principal}!')


def body(args):
    rate = args.interest / 12 * 0.01
    match None:
        case args.payment:
            match args.type:
                case 'annuity':
                    annuity_payment(rate, args.principal, args.periods)
                case 'diff':
                    diff_payment(rate, args.principal, args.periods)
                case _:
                    return print('Incorrect parameters')
        case args.periods:
            credit_time(rate, args.principal, args.payment)
        case args.principal:
            loan_principal(rate, args.payment, args.periods)


if __name__ == '__main__':
    head()
