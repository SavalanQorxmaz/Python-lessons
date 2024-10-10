def average_f(*numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count

numbers_lst = [1, 5, 7, 19, 23, 37]

average_numbers = average_f(*numbers_lst)
print(average_numbers)