from pathlib import Path


def read_file_folder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f'{i + 1}, {items}')
    return items


def create_file():
    try:
        files = read_file_folder()
        print(files)
        name = input('Please tell me your file name:- ')
        p = Path(name)
        if not p.exists() and p.is_file():
            with open(p, 'w') as file_save:
                data = input('What you want to write in this file:- ')
                file_save.write(data)
            print("file created successfully")
        else:
            print('This file is already exist')
    except Exception as err:
        print(f'An error occurs {err}')


def read_file():
    try:
        read_file_folder()
        name = input('which file you want to read:- ')
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p, 'r') as file_reader:
                data = file_reader.read()
                print(data)
            print('Read successfully')
        else:
            print('File is not exist')
    except Exception as err:
        print(f'An error occur as {err}')


print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for deleting a file")

check = int(input("Please tell me your response:- "))

if check == 1:
    create_file()
if check == 2:
    read_file()
