num = int(input("Enter the number = "))
hour = num//3600
hour1 = num%3600
minute = hour1//60
second = hour1%60
print(hour, "hours", minute, "minutes", second, 'seconds')
seconds1 = 10000
hours = 2
minutes = 46
seconds2 = 40
text = f"""В {seconds1} секунд {hours} часа, {minutes} минут, {seconds2} секунд."""
print(text)

