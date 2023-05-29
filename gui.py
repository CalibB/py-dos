from modules import functions
import PySimpleGUI as sg
from modules import functions

text = sg.Text('Enter in your todo:')
btn = sg.Btn('Add')
todo_input = sg.InputText(tooltip='Enter in your todo.', key='todo')

window = sg.Window('Py do\'s',
                   layout=[[text], [todo_input, btn]],
                   font=("Helvetica", 20))

while True:
    event, values = window.read()
    todos = functions.read_file()

    match event:
        case 'Add':
            todos.append(values['todo'].strip() + '\n')
            functions.write_file(todos)
        case sg.WIN_CLOSED:
            break

window.close()
