def my_func(word):
    litin = 'qwertyuiopasdfghjklzxcvbnm'
    return word.title() if not set(word).difference(litin) else False

words = input('введите слова разделяя пробелами ').split()
for w in words:
    result = my_func(w)
    if result:
        print(my_func(w), '')

