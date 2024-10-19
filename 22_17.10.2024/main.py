# # functional programming
# """
#    *
#  * **
# ** ***
# """
# def create_left_side(rows):
#     formula = rows
#     pass

# def create_right_side(rows):
#     formula = rows + 1
#     pass

# def create_pyramid():
#     create_left_side()
#     create_right_side()

# if __name__ == "__main__":
#     create_pyramid()


x = 2
y = 2
z = 3
n = 3

result = [[i, j, k]  for i in range(x) for j in range(y) for k in range(z) if i+j+k != n ]
print(result)