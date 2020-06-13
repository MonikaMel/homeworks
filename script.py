language=input('Enter your language { hy, ru ,en}:')
if language == 'hy':
    with open('hy.txt') as f:
        print(f)
elif language == 'en':
    with open('en.txt') as f:
        print(f)
elif language == 'ru':
    with open('ru.txt') as f:
        print(f)
else:
    print('Try again')