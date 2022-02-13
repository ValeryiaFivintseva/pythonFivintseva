revenue = int(input("Enter the number = "))
costs = int(input("Enter the number = "))
result = revenue - costs
if result > 0:
    print('компания работает с прибылью')
if result < 0:
    print('компания работает в убыток')