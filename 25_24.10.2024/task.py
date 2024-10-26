import random
import timeit
    

def find_some_nmbers():
    my_list = [random.randint(0,500) for _ in range(100)]
    average = sum(my_list) / len(my_list)
    floor = average * 95 / 100
    new_list = [*filter(lambda x: floor <= x <= average, my_list)]
    print(new_list)
    return new_list



start = timeit.default_timer()
find_some_nmbers()
print(timeit.default_timer() - start)
