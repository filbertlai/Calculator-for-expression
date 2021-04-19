import math                     # For using calculator
import PySimpleGUI as sg        # For graphical user interface
from datetime import datetime   # For obtaining current time



result_widget=sg.Text('\t\t')

layout=[[sg.Text('Enter your expression below.\nNote that log(8,2) means log 8 in base 2.')]
        ,[sg.Input(key='ex', size=(20,10)), sg.Text('='), result_widget, sg.Button('Clear'), sg.Button('Calculate', bind_return_key=True)]
        ,[sg.Text('Records:')]
        ,[sg.Output(size=(50,10))]]

window=sg.Window('Calculator || Version - 4.0 || Author - Lai Filbert', layout)


while True:
    event, values=window.read()


    if event==sg.WIN_CLOSED:
        break


    if event=='Calculate':
        try:
            expression=values['ex']
            expression=expression.replace("log", "math.log")
            expression=expression.replace("^", "**")
            result_widget(eval(expression))
            print(datetime.now().time(), ' : ', values['ex'], '=', eval(expression))
        except:
            result_widget('Error! Please enter again!')


    if event=='Clear':
        window['ex'].update('')

window.close()
