# 1234567890123
# ------d------ # 0 -> 6
# ----d-c-d---- # 1 -> 4
# --d-c-b-c-d-- # 2 -> 2

# d-c-b-a-b-c-d # 3 -> 0
# --d-c-b-c-d--
# ----d-c-d----
# ------d------

import string
n = int(input())
start = list(string.ascii_lowercase[:n])
max_len = 4 * n - 3

butun_kodumuz = [ ]
# [a, b, c, d]
# [a, d, c, b] += 1
# #         ^
# [c, b, a, d]

def rotate_order():
    pass
def main():
    for _ in range(n):
        alpha = start[::-1] + start[1:]

        start.pop(0)

        center_pattern = "-".join(alpha)

        center_len = len(center_pattern)

        defis = (max_len - center_len) // 2

        full_path = defis * "-" + center_pattern + defis * "-"

        butun_kodumuz.append(full_path)
    else:
        butun_kodumuz = butun_kodumuz[1:][::-1] + butun_kodumuz
        butun_kodumuz = butun_kodumuz[::-1]
        for ptn in butun_kodumuz[::-1]:
            print(ptn)