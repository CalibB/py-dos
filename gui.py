from modules import functions
import PySimpleGUI as sg

text = sg.Text('Enter in your todo:')
btn = sg.Btn('Add')
todo_input = sg.InputText(tooltip='Enter in your todo.')

window = sg.Window('Py do\'s', layout=[[text], [todo_input, btn]])
window.read()
window.close()
