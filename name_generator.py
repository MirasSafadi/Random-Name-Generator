import PySimpleGUI as sg
import random

def generate_random_name(employees:set):
    if len(employees) == 0:
        return 'No more names to generate'
    name = random.choice(employees)
    employees.remove(name)
    return name


employees = ['Zohar','Shadi','Ali','Nataliya','Miras','Anita','Or','Kfir','Liron','Vadim','Dotan','Gil']
sg.theme('Light Blue')

layout = [[sg.Text('Click \'Generate\' to generate a random team member name')],
        [sg.Button('Generate',bind_return_key=True),sg.Button('Cancel')],
        [sg.Text(size=(40,5),key='-OUTPUT-')]] #size=(width,height)


window = sg.Window('BMC Random Name Generator', layout, icon='C:\\Users\\Pc\\Documents\\pyInstaller demo\\bmc.ico')
while True:
    # generated_name = generate_random_name(employee_set)
    name = ''
    if len(employees) == 0:
        name = 'No more names to generate'
    else:
        name = random.choice(employees)
        employees.remove(name)

    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':	# if user closes window or clicks cancel
        break
    if event == 'Generate':
        text_output = name
        window['-OUTPUT-'].update(text_output)

window.close()