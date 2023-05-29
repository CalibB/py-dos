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

window = sg.Window('Py do\'s',
                   layout=[[text], [todo_input, btn], [list_box, edit_btn]],
                   font=("Helvetica", 20))

while True:
    event, values = window.read()

    match event:
        case 'Add':
            todos.append(values['todo'].strip() + '\n')
            functions.write_file(todos)
            window['todos'].update(values=[todo.strip('\n') for todo in todos])
        case 'Edit':
            todo_to_be_edited = values['todos'][0]
            index = todos.index(todo_to_be_edited + '\n')
            edited_todo = values['todo'] + '\n'
            todos[index] = edited_todo

            functions.write_file(todos)
            window['todos'].update(values=[todo.strip('\n') for todo in todos])
        case 'todos':
            window['todo'].update(value=values['todos'][0].strip('\n'))
        case sg.WIN_CLOSED:
            break

window.close()
