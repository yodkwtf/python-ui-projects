import PySimpleGUI as sg

layout = [[sg.Text("time")], [sg.Button("Start"), sg.Button("Stop"), sg.Button("Lap")]]

window = sg.Window("Stopwatch", layout, size=(300, 300), no_titlebar=True)

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, "Stop"):
        break

window.close()
