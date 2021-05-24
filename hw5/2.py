with open('file for 2 task.txt', 'r') as my_file:
    lines = 0
    letter = 0
    for line in my_file:
        lines += line.count(line)
        letter = len(line) - 1
        print(f'{letter} символов в строке')
    print(f'количество строк общее - {lines}')
