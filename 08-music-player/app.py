import PySimpleGUI as sg
import base64
from io import BytesIO
from PIL import Image
from pygame import mixer, time

mixer.init()
clock = time.Clock()


# function to convert image to base64
def base64_image_import(path):
    image = Image.open(path)
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue())


# import song
song_path = sg.popup_get_file("Select a song to play", no_window=True)
song_name = song_path.split("/")[-1].split(".")[0]
song = mixer.Sound(song_path)

# timer
song_length = int(song.get_length())
time_since_start = 0
pause_amount = 0
is_playing = False

sg.theme("reddit")

# Layouts
play_layout = [
    [sg.VPush()],
    [
        sg.Push(),
        sg.Text(song_name, font=("Helvetica", 15), key="-SONG-"),
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
    [sg.Progress(song_length, orientation="h", size=(20, 20), key="-PROGRESS-")],
]

volume_layout = [
    [sg.VPush()],
    [
        sg.Push(),
        sg.Slider(
            range=(0, 100),
            default_value=10,
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
    event, values = window.read(timeout=1)

    if event == sg.WIN_CLOSED:
        break

    # update progress bar
    if is_playing:
        time_since_start = time.get_ticks()
        window["-PROGRESS-"].update((time_since_start - pause_amount) // 1000)

    # play/pause song
    if event == "-PLAY-":
        is_playing = True
        pause_amount += time.get_ticks() - time_since_start
        if mixer.get_busy() == False:
            song.play()
        else:
            mixer.unpause()

    if event == "-PAUSE-":
        is_playing = False
        mixer.pause()

    # update volume
    volume = values["-VOLUME-"]
    song.set_volume(volume / 100)

window.close()
