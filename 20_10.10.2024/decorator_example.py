import time

# def decorator_f(func, sleep):
#     time.sleep(sleep)
#     # func = kwargs.get('func')
#     def wrapper(*args):
#         # nonlocal func
#         print('***********')
#         # result = func(*args, **kwargs)
#         result = func(*args)
#         # print(result)
#         # result = args[0]
#         print('**************')
#         return result
#     return wrapper

# @decorator_f(any,sleep=1)
# def my_func(name):
#     print(name)
#     return name
# # result = decorator_f(my_func, sleep=1)
# # decorator_f(my_func, sleep = 1)
# # my_func('salam')(sleep=1)
# # print(my_func)
# # result('salam')
# decorator_f(sleep=1)(my_func('salam'))

def decorator_frame(*args, **kwargs):
    time.sleep(args[0])
    def decorator(func):
        def wrapper(*args,**kwargs):
            print('Start')
            result = func(*args, **kwargs)
            print('End')
            return result
        return wrapper
    return decorator

@decorator_frame(1)
def greeting(name):
    print(f'Hello {name}')
    return name

result = greeting('salam')
print(f'result: {result}')