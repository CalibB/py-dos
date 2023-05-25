from modules import functions
import time

while True:
    print(f"It is {time.strftime('%b %d, %Y %H:%M:%S')}")
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    todos = functions.read_file()

    if user_action.startswith('add'):
        todo = user_action[3:].strip() + '\n'
        todos.append(todo)

        functions.write_file(todos)

    elif user_action.startswith('show'):
        for index, todo in enumerate(todos):
            todo = todo.strip('\n')
            print(f"{index + 1}. {todo}")

    elif user_action.startswith('edit'):
        try:
            chosen_todo = int(user_action[4:].strip())
            edited_todo = input('Enter your new todo: ')

            todos[chosen_todo - 1] = edited_todo + "\n"

            functions.write_file(todos)

        except ValueError:
            print('Please enter the number of the todo you want to edit!')
            continue
        except IndexError:
            print("The selected todo doesn't exist.")
            continue

    elif user_action.startswith('complete'):
        try:
            ex_todo = int(user_action[8:].strip())
            index = ex_todo - 1
            todo_to_be_removed = todos[index].strip('\n')
            todos.pop(index)

            functions.write_file(todos)

            print(f"The todo: '{todo_to_be_removed}' has been removed.")

        except ValueError:
            print('Please enter the number of the todo you want to complete!')
            continue
        except IndexError:
            print("The todo doesn't exist.")
            continue

    elif user_action.startswith('exit'):
        print("Byeee!")
        break
    else:
        print("Unknown command... please enter the stated commands!")
