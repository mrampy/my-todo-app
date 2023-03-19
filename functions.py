FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """Read a text file and return the list of
    to-do items."""
    with open(filepath, 'r') as keyfile:
        current_items = keyfile.readlines()
    return current_items


def write_todos(todos_arg, filepath=FILEPATH):
    """Write the to-do list in the text file."""
    with open(filepath, 'w') as content:
        content.writelines(todos_arg)


if __name__ == '__main__':
    # To execute commands only in this file
    print(get_todos())
