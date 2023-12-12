
factorial_number = int(input("Number: "))
fac = 1

if factorial_number < 0:
    print("Negative")
elif factorial_number ==0:
    print("1")
else:
    for num in range(1,factorial_number+1):
        fac = fac*num
    print('Answer: ',fac)
    
