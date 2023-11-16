def read_last(lines, file):
    if lines > 0 :
        with open(file, encoding='utf-8') as text:
            file_lines = text.readlines()[-lines:]
        for line in file_lines:
            print(line.strip())
    else:
            print('Строк нет')

read_last(2, '123.txt')