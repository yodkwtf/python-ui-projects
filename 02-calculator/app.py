import PySimpleGUI as sg


def create_window(theme):
    sg.theme(theme)
    sg.set_options(font=("Helvetica", 14), button_element_size=(6, 3))

    button_size = (6, 3)

    layout = [
        [
            sg.Text(
                "0",
                font="Franklin 26",
                justification="right",
                expand_x=True,
                pad=(10, 20),
                right_click_menu=theme_menu,
                key="-OUTPUT-",
            )
        ],
        [
            sg.Button("Clear", expand_x=True),
            sg.Button("Enter", expand_x=True),
        ],
        [
            sg.Button("7", size=button_size),
            sg.Button("8", size=button_size),
            sg.Button("9", size=button_size),
            sg.Button("÷", key="/", size=button_size),
        ],
        [
            sg.Button("4", size=button_size),
            sg.Button("5", size=button_size),
            sg.Button("6", size=button_size),
            sg.Button("x", key="*", size=button_size),
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

    return sg.Window("Calculator", layout)


# theme options
theme_options = [
    "DarkAmber",
    "DarkBlack",
    "DarkBlue",
    "DarkBlue3",
    "DarkBrown",
    "DarkGreen",
    "DarkGrey",
    "DarkKhaki",
    "DarkLightGreen",
    "DarkRed",
    "DarkTeal",
    "DarkViolet",
    "LightBrown",
    "LightGreen",
    "LightGrey",
    "LightPurple",
    "LightYellow",
    "SystemDefault",
]
theme_menu = ["menu", theme_options]

# Call the create_window function with the theme of your choice
window = create_window("DarkBlack")

current_num = ""
calculation = ""

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event in theme_options:
        window.close()
        window = create_window(event)
        current_num = ""
        calculation = ""

    if event in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
        current_num += event
        window["-OUTPUT-"].update(current_num)

    if event in ["+", "-", "*", "/"]:
        calculation += current_num + event
        current_num = ""
        window["-OUTPUT-"].update(calculation)

    if event == "Enter":
        calculation += current_num
        current_num = ""
        window["-OUTPUT-"].update(eval(calculation))

    if event == "Clear":
        current_num = ""
        calculation = ""
        window["-OUTPUT-"].update("")

window.close()
