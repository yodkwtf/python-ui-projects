import PySimpleGUI as sg
import base64
from io import BytesIO
from PIL import Image


# function to convert image to base64
def base64_image_import(path):
    image = Image.open(path)
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue())


sg.theme("reddit")

# Layouts
play_layout = [
    [sg.VPush()],
    [
        sg.Push(),
        sg.Text("Song Name", font=("Helvetica", 15), key="-SONG-"),
        sg.Push(),
    ],
    [sg.VPush()],
    [
        sg.Push(),
        sg.Button(
            image_data=base64_image_import("play.png"),
            key="-PLAY-",
            button_color="white",
            border_width=0,
        ),
        sg.Text(" "),
        sg.Button(
            image_data=base64_image_import("pause.png"),
            key="-PAUSE-",
            button_color="white",
            border_width=0,
        ),
        sg.Push(),
    ],
    [sg.VPush()],
    [sg.Progress(100, orientation="h", size=(20, 20), key="-PROGRESS-")],
]

volume_layout = [
    [sg.VPush()],
    [
        sg.Push(),
        sg.Slider(
            range=(0, 100),
            default_value=50,
            orientation="h",
            size=(20, 15),
            key="-VOLUME-",
        ),
        sg.Push(),
    ],
    [sg.VPush()],
]

layout = [
    [sg.TabGroup([[sg.Tab("Play", play_layout), sg.Tab("Volume", volume_layout)]])],
]

window = sg.Window("Music Player", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

window.close()
