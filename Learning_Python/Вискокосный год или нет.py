year = int(input("Введите год, который хотите ровериеть: "))

# if year % 4 == 0:
#     print("%d високосный" %year)
# elif year % 100 == 0:
#     print("%d не високосный" %year)
# elif year % 400 == 0:
#     print("%d високосный" %year)
# else:
#     print("%d не високосный" %year)
    

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")