# try:
#     file = open('1test_requirements.txt')
#     print(file.readlines())
#     file.close()
# except FileNotFoundError:
#     print('что-то пошло не так...')
# # finally:


try:
    with open("abc.txt") as f:
        r = f.read(1)
except:
    print("File Not Found")
