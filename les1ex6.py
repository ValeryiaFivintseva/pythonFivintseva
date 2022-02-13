revenue = int(input("Enter the number = "))
costs = int(input("Enter the number = "))
result = revenue - costs
print(result)
if result > 0:
    print('компания работает с прибылью')
if result < 0:
    print('компания работает в убыток')
rent = (result // revenue) * 100
print(rent)
pers = int(input("Enter the number = "))
pers1 = result // pers
print(pers1)