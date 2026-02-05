def strip_string(b_function):
    def wrapper():
        func = b_function()
        stripped = func.strip('-')
        return stripped
    return wrapper

def uppercase_decorator(some_function):
    def a_wrapper():
        func = some_function()
        make_uppercase = func.upper()
        return make_uppercase
    return a_wrapper

def clli_code():
    print('The Florida router clli code is', end = ' ')
    return '---tpaflxacg19---'

clli_code = uppercase_decorator(strip_string(clli_code))

print(clli_code())