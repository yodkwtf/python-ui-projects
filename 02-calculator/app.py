import PySimpleGUI as sg

sg.theme("LightGrey1")
sg.set_options(font=("Helvetica", 14), button_element_size=(6, 3))

button_size = (6, 3)
large_button_size = (14, 3)

layout = [
    [sg.Text("Output", font="Franklin 26")],
    [
        sg.Button("Clear", expand_x=True),
        sg.Button("Enter", expand_x=True),
    ],
    [
        sg.Button("7", size=button_size),
        sg.Button("8", size=button_size),
        sg.Button("9", size=button_size),
        sg.Button("÷", size=button_size),
    ],
    [
        sg.Button("4", size=button_size),
        sg.Button("5", size=button_size),
        sg.Button("6", size=button_size),
        sg.Button("x", size=button_size),
    ],
    [
        sg.Button("1", size=button_size),
        sg.Button("2", size=button_size),
        sg.Button("3", size=button_size),
        sg.Button("-", size=button_size),
    ],
    [
        sg.Button("0", expand_x=True),
        sg.Button(".", size=button_size),
        sg.Button("+", size=button_size),
    ],
]


window = sg.Window("Calculator", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

window.close()
