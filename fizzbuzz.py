for num in range(1, 1000):
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBazz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Bazz')
    else:
        print(num)