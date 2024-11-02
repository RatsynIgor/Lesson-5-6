print('Lesson 6: TryCatch')

#exception ZeroDevision
# print(10/0)

numbers = [1, 2, 5, 8]
#exception OutOfRange
# print(numbers[4])

#exception InvalidValue
# value_int = int('23a')
# print(value_int)

# a: int = 10
# b: int = 0
#
# try:
#     result = a/b
#     print(f'{a} / {b} = {result}')
# except ZeroDivisionError as error:
#     print(f'error info {error}')
# finally:
#     print('operation is completed')


def get_int(num_input: str) -> int: #Функція
    num_int: int
    isInt: bool

    try:
        num_int = int(num_input) #Надання значень
        isInt = True    #Надання значень
    except:
        print('error')
        isInt = False
        num_int = None
    finally:
        if isInt == True:
            print("Ми присвоїли тип даних INTENGER")   ##Якщо вдалося перетворити в Intenger
        else:
            print('МИ не присвоїли тип даних INTENGER') #Якщо не вдалося перетворити в Intenger

    return num_int #Повернення значення користовачу


num_input = input("Введіть число:")
number = get_int(num_input) #Присвоєння number значення яке надає користувач
styp = number #Присвоєння styp значення number
print(styp **2) # Піднесення в квадрат змінної styp