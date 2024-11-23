import time


lst = [1, 2, 3, 4, 5, 6]
i = 0
while True:
    print(lst[i])
    i = (i +1) % len(lst)
    time.sleep(1)