# 2. Написать декоратор на Python

# Декорируемая функция (ее нельзя изменять) с декоратором:

# @print_num_gt(3)
# def print_num(x: int):
#    print(x)

# При вызове функции `print_num` в консоль должен быть выведен аргумент `x`, 
# если он больше параметра, передаваемого в `print_num_gt`, иначе — «error».

from functools import wraps


def print_num_gt(param: int):
    def _print_num_gt(func):
        @wraps(func)
        def inner(x):
            if x > param:
                func(x)
            else:
                print("error")
        return inner
    return _print_num_gt


@print_num_gt(3)
def print_num(x: int):
    print(x)


print_num(5)  # 5
print_num(1)  # error
