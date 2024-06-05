import PySimpleGUI as sg

layout = [
    [
        sg.Input(key="-INPUT-"),
        sg.Spin(["Km to Miles", "Kg to lbs", "Sec to Min"], key="-UNITS-"),
        sg.Button("Convert", key="-CONVERT-"),
    ],
    [sg.Text("Result: ", key="-OUTPUT-")],
]

window = sg.Window("Converter", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "-CONVERT-":
        input_value = values["-INPUT-"]
        unit = values["-UNITS-"]

        if input_value.isnumeric() == False or input_value == "":
            window["-OUTPUT-"].update("Please enter a valid number")
            continue

        if unit == "Km to Miles":
            result = float(input_value) * 0.621371
        elif unit == "Kg to lbs":
            result = float(input_value) * 2.20462
        elif unit == "Sec to Min":
            result = float(input_value) / 60

        window["-OUTPUT-"].update(f"Result: {round(result, 2)}")

window.close()
