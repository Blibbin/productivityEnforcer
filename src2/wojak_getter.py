import os

def get_wojak(number):
    return f'./WojakFolder/wojak{number}.jpg'

# print(os.path.exists(get_wojak(1)))

# for i in range(0,49):
#     print(i, os.path.exists(get_wojak(i)))