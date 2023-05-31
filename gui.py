from modules import functions
import PySimpleGUI as sg
from modules import functions

todos = functions.read_file()

text = sg.Text('Enter in your todo:')
btn = sg.Btn('Add')
todo_input = sg.InputText(tooltip='Enter in your todo.', key='todo')

list_box = sg.Listbox(values=[todo.strip('\n') for todo in todos], key='todos',
                      enable_events=True, size=(45, 10))
edit_btn = sg.Button('Edit')
complete_btn = sg.Button('Complete')
exit_btn = sg.Button('Exit')

window = sg.Window('Py do\'s',
                   layout=[[text],
                           [todo_input, btn],
                           [list_box, edit_btn, complete_btn],
                           [exit_btn]],
                   font=("Helvetica", 20))

while True:
    event, values = window.read()
    print(values)

    match event:
        case 'Add':
            if values['todo'] == '':
                sg.popup('Woah there! You are trying to add nothing to your list, please type something.',
                         title="Hold up!", custom_text="Alright...", grab_anywhere=True,
                         background_color='red', text_color='black', button_color=('red', 'black'),
                         keep_on_top=True, font=('Helvetica', 20))
            else:
                todos.append(values['todo'].strip() + '\n')
                functions.write_file(todos)
                functions.load_ui(window, 'todos', todos)
                functions.clear_ui(window, 'todo')
        case 'Edit':
            if not values['todos']:
                sg.popup('Ehh bud! Select the todo you want to edit, thanks.',
                         title="Hold up!", custom_text="Alright...", grab_anywhere=True,
                         background_color='red', text_color='black', button_color=('red', 'black'),
                         keep_on_top=True, font=('Helvetica', 20))
            else:
                todo_to_be_edited = values['todos'][0]
                index = todos.index(todo_to_be_edited + '\n')
                edited_todo = values['todo'] + '\n'
                todos[index] = edited_todo

                functions.write_file(todos)
                functions.load_ui(window, 'todos', todos)
                functions.clear_ui(window, 'todo')
        case 'Complete':
            todo_to_be_completed = values['todos'][0] + '\n'
            todos.remove(todo_to_be_completed)
            functions.write_file(todos)
            functions.load_ui(window, 'todos', todos, values)
            functions.clear_ui(window, 'todo')
        case 'Exit':
            break
        case 'todos':
            functions.load_ui(window, 'todo', todos, values, 'y')
        case sg.WIN_CLOSED:
            break

window.close()
