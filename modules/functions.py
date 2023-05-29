FILEPATH = 'files/todos.txt'


def read_file(filename=FILEPATH):
    """
    Reads content of a file and puts it into
    a list and returns that list.
    """
    with open(filename, 'r') as file:
        content = file.readlines()

    return content


def write_file(items, filename=FILEPATH):
    """
    Writes the specified items into a file of
    your choice.
    """
    with open(filename, 'w') as file:
        file.writelines(items)


# var __name__ used to denote origin of script
# Commonly used to separate code from other modules


def load_ui(parent, child, list_name, var=None, singular='n'):
    if singular == 'y':
        parent[child].update(value=var['todos'][0])
    else:
        parent[child].update(values=[todo.strip('\n') for todo in list_name])

