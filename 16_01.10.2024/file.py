import os

# f = open('test.txt', 'w')
# f.write('Hello World')
# f.close()

# f = open('test.txt', 'r')
# print(f.read())
# f.close()

# f = open('test.txt', 'a')
# f.write('\nHello again')
# f.close()

# f = open('test.txt', 'r')
# print(f.read())
# f.close()

# f = open('D:\\testfile.txt', 'a')
# f.write('Hello disk D')
# f.close()

# f = open('D:\\testfile.txt', 'r')
# print(f.read())
# f.close()

# x = os.listdir('test')
# print(x)
# # os.rmdir('test')
# for i in x:
#     os.remove(f'test\{i}')
#     continue
# print(x)

# try:
#     os.remove('test.txt')
#     print(os.listdir())
# except FileNotFoundError:
#     print('File not found')

# z = os.mkdir('test2')
# print(z)

# y = open('D:\\3.txt', 'a')
# y.write('nested file')
# y.close()

# y = open('D:\\3.txt', 'r')
# print(y.read())
# y.close()
# os.remove('D:\\3.txt')
# print(os.listdir('D:\\'))
objects = os.listdir('test')
for object in objects:
    print(object)
    # print(os.listdir(f'test\{object}' ))
    # x = open(f'test\{object}', 'r')
    print(os.remove(f'test\{object}'))
    # print(x.read())
    