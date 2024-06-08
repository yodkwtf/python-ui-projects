import PySimpleGUI as sg
from time import time


def create_window():
    sg.theme("black")
    layout = [
        [
            sg.Push(),
            sg.Text("x", key="-CLOSE-", font=("Helvetica", 13), enable_events=True),
        ],
        [sg.VPush()],
        [sg.Text("0.0", key="-TIME-", font="Young 50")],
        [
            sg.Button(
                "Start",
                key="-START/STOP-",
                button_color=("white", "red"),
                border_width=0,
                font="Young 15",
            ),
            sg.Button(
                "Lap",
                key="-LAP-",
                button_color=("white", "red"),
                border_width=0,
                font="Young 15",
                visible=False,
            ),
        ],
        [sg.Column([[]], key="-LAP-COLUMN-")],
        [sg.VPush()],
    ]

    return sg.Window(
        "Stopwatch",
        layout,
        size=(400, 400),
        no_titlebar=True,
        element_justification="center",
    )


window = create_window()
start_time = 0
lap_count = 0
active = False


while True:
    event, values = window.read(timeout=10)

    if event in (sg.WIN_CLOSED, "-CLOSE-"):
        break

    if event == "-START/STOP-":
        if active:
            # from running to stop (Button: STOP)
            window["-START/STOP-"].update("Reset")
            window["-LAP-"].update(visible=False)
            active = False
        else:
            if start_time > 0:
                # from stop to reset (Button: RESET)
                window.close()
                window = create_window()
                start_time = 0
                lap_count = 0
            else:
                # from start to running (Button: START)
                start_time = time()
                window["-START/STOP-"].update("Stop")
                window["-LAP-"].update(visible=True)
                active = True

    if active:
        timer = round(time() - start_time, 1)
        window["-TIME-"].update(timer)

    if event == "-LAP-":
        lap_count += 1
        window.extend_layout(
            # window["-LAP-COLUMN-"], [[sg.Text("Lap: " + lap_count + " " + str(timer) + "s\n")]]
            window["-LAP-COLUMN-"],
            [[sg.Text(f"Lap {lap_count}: {timer}s\n")]],
        )

window.close()
