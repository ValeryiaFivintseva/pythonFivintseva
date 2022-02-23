my_list = list(map(int, input('my_list: ').split()))
new_list = [my_list[i] for i in range(len(my_list)) if my_list[i] > my_list[i - 1]]
print(f"Исходный список: {my_list}")
print(f"Новый список: {new_list}")