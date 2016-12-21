# def main():
#     incomes = []
#     months = int(input("How many months? "))
#     for month in range(1, months+1):
#         monthly_income = float(input("Enter monthly_income for month " + str(month) + ": "))
#         incomes.append(monthly_income)
#     print("\nIncome Report\n-------------")
#     total = 0
#     for month in range(1, months + 1):
#         monthly_income = incomes[month - 1]
#         total += monthly_income
#         print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, monthly_income, total))
# main()


def main():
    income=[]
    month=int(input("Enter a month"))
    for month in range(1,month + 1):
        month_income=float(input("Enter monthly income for month"+ str(month)+ ":"))
        income.append(month_income)
    print("Income")
    total=0
    for month in range(1 , month + 1):
        month_income=income[month -1]
        total+=month_income
        print("Month{:2}-Income:${:10.2f}Total:${:10}".format(month , month_income , total))


main()


def main():
    income=[]
    month=int(input("Enter a month"))
    for month in range(1,month+1):
        month_income=float(input("Enter a month income for month"+str(month)+":"))
        income.append(month_income)
    print("income")
    total=0
    for month in range(1,month+1):
        month_income=month[month-1]
        total+=month_income
        print("asjkfhhfkf")
main()