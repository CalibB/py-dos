import PySimpleGUI as sg
from modules import functions
import time

todos = functions.read_file()

sg.theme("DarkPurple4")

clock = sg.Text('', key='clock')
text = sg.Text('Enter in your todo:')
btn = sg.Btn('Add')
todo_input = sg.InputText(tooltip='Enter in your todo.', key='todo')

list_box = sg.Listbox(values=[todo.strip('\n') for todo in todos], key='todos',
                      enable_events=True, size=(45, 10))
edit_btn = sg.Button('Edit')
complete_btn = sg.Button('Complete')
exit_btn = sg.Button('Exit')

window = sg.Window('Py do\'s',
                   layout=[[clock],
                           [text],
                           [todo_input, btn],
                           [list_box, edit_btn, complete_btn],
                           [exit_btn]],
                   font=("Helvetica", 15))

while True:
    event, values = window.read(timeout=10)
    window['clock'].update(value=time.strftime('%b %d, %Y %H:%M:%S'))

    match event:
        case 'Add':
            if values['todo'] == '':
                functions.display_popup(interface=sg,
                                        msg='Woah there! You are trying to add nothing to your list, '
                                            'please type something.',
                                        btn_msg='Ok')
            elif todos.__contains__(functions.add_newline_char(values['todo'])):
                functions.display_popup(sg, 'This todo already exists...', 'Oops!')
            else:
                todos.append(functions.add_newline_char(values['todo'].strip()))
                functions.write_file(todos)
                functions.load_ui(window, 'todos', todos)
                functions.clear_ui(window, 'todo')
        case 'Edit':
            try:
                if values['todo'] and values['todo'] != values['todos'][0]:
                    todo_to_be_edited = functions.add_newline_char(values['todos'][0])
                    index = todos.index(todo_to_be_edited)
                    edited_todo = functions.add_newline_char(values['todo'])
                    todos[index] = edited_todo

                    functions.write_file(todos)
                    functions.load_ui(window, 'todos', todos)
                    functions.clear_ui(window, 'todo')
                else:
                    functions.display_popup(sg, "It appears that you're trying to edit nothing!",
                                            "I'm sorry!")
            except IndexError:
                functions.display_popup(sg, 'Ehh bud! Select the todo you want to edit, thanks.',
                                        'No problem!')
        case 'Complete':
            try:
                if not values['todo']:
                    functions.display_popup(sg, "Excuse me!? You didn't select a todo to complete!",
                                            'Sorry...')
                else:
                    todo_to_be_completed = functions.add_newline_char(values['todo'])
                    todos.remove(todo_to_be_completed)
                    functions.write_file(todos)
                    functions.load_ui(window, 'todos', todos, values)
                    functions.clear_ui(window, 'todo')
            except IndexError:
                functions.display_popup(sg, "There aren't any todos left...", 'My bad...')
            except ValueError:
                functions.display_popup(sg, "I'm afraid there's no such todo.", 'Sad...')
        case 'Exit':
            break
        case 'todos':
            functions.load_ui(window, 'todo', todos, values, 'y')
        case sg.WIN_CLOSED:
            break

window.close()
