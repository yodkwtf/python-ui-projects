import PySimpleGUI as sg

layout = [
    [sg.Text("Enter your name:"), sg.InputText()],
    [sg.Button("Submit"), sg.Button("Cancel")],
]

window = sg.Window("Simple GUI", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "Cancel":
        break

    if event == "Submit":
        sg.popup(f"Hello, {values[0]}!")

window.close()
