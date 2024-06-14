import PySimpleGUI as sg

control_col = sg.Column(
    [
        [
            sg.Frame(
                "Contrast",
                layout=[[sg.Slider((0, 10), orientation="h", key="-BRIGHTNESS-")]],
            )
        ],
        [
            sg.Checkbox("Emboss", key="-EMBOSS-"),
            sg.Checkbox("Contour", key="-CONTOUR-"),
        ],
        [sg.Checkbox("Flip x", key="-FLIPX-"), sg.Checkbox("Flip y", key="-FLIPY-")],
        [sg.Button("Save Image", key="-SAVE-")],
    ]
)
image_col = []

layout = [[control_col, image_col]]

window = sg.Window("Image Editor", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

window.close()
