# a = int(input('Enter a number'))
#
# try:
#     print(10 / a)
# except Exception as e:
#     print(f'Sorry there is an error as {e}')
# else:
#     print('there is no exception')
# finally:
#     print('I will work no matter what')

age = int(input('Enter your age'))

try:
    if age < 10 or age > 18:
        raise ValueError('Your age must be between 10 to 18')
    else:
        print('Welcome the club')
except Exception as err:
    print(f'an error occur {err}')

print('the club starts soon')
