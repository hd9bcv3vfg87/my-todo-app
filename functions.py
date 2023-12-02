FILEPATH = 'todos.txt'


def get_todos(file_path=FILEPATH):
    with open(file_path, 'r') as file:
        return file.readlines()


def write_todos(todos_to_write, file_path=FILEPATH):
    with open(file_path, 'w') as file:
        file.writelines(todos_to_write)


if __name__ == '__main__':
    print('I was called directly')
