import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--type")  # тип кредита diff or annuity
parser.add_argument("-pr", "--principal", type=int)  # p полная сумма
parser.add_argument("-p", "--periods", type=int)  # n количество платежей
parser.add_argument("-i", "--interest", type=float)  # i процент
parser.add_argument("-py", "--payment", type=int)  # d ежемесячный платеж

args = parser.parse_args()

if args.type == "diff" and args.principal and args.periods and args.interest:
    n = abs(args.periods)
    p = abs(args.principal)
    i = abs(args.interest / (12 * 100))
    m = 0
    t = 0
    for m in range(0, n):
        m += 1
        d = math.ceil((p / n) + i * (p - ((p * (m - 1))/n)))
        t += d
        print(f"Month {m}: payment is {d}")
    print("Overpayment = ", t - p)
elif args.type == "annuity" and args.principal and args.periods and args.interest:
    p = args.principal
    n = args.periods
    i = args.interest / (12 * 100)
    d = math.ceil(p * ((i * pow((1 + i), n)) / ((pow((1 + i), n)) - 1)))
    print(f"Your annuity payment = {d}!")
    print("Overpayment = ", d * n - p)
elif args.type == "annuity" and args.payment and args.periods and args.interest:
    d = args.payment
    n = args.periods
    i = args.interest / (12 * 100)
    p = math.floor(d / ((i * pow((1 + i), n)) / ((pow((1 + i), n)) - 1)))
    print(f"Your loan principal = {p}!")
    print("Overpayment = ", d * n - p)

elif args.type == "annuity" and args.principal and args.payment and args.interest:
    p = args.principal
    d = args.payment
    i = args.interest / (12 * 100)
    n = math.ceil(math.log((d / (d - (i * p))), (1 + i)))
    m = n % 12  # это остаток месяца
    y = n // 12  # это год
    if m == 0:
        print(f"It will take {y} years to repay this loan!")
        print("Overpayment = ", d * n - p)
    elif y == 0:
        print(f"It will take {m} months to repay this loan!")
        print("Overpayment = ", d * n - p)
    else:
        print(f"It will take {y} years and {m} months to repay this loan!")
        print("Overpayment = ", d * n - p)

else:
    print("Incorrect parameters")

