import PySimpleGUI as sg
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.figure

sg.theme("black")
table_data = []

layout = [
    [
        sg.Table(
            headings=["Observation No.", "Result"],
            values=table_data,
            expand_x=True,
            hide_vertical_scroll=True,
            key="-TABLE-",
        )
    ],
    [sg.Input(key="-INPUT-", expand_x=True), sg.Button("Add")],
    [sg.Canvas(key="-CANVAS-")],
]

window = sg.Window("Graph App", layout)

# Matplotlib
fig = matplotlib.figure.Figure(figsize=(5, 4))
fig.add_subplot(111).plot([], [])
figure_canvas_agg = FigureCanvasTkAgg(fig, window["-CANVAS-"].TKCanvas)
figure_canvas_agg.draw()
figure_canvas_agg.get_tk_widget().pack()

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "Add":
        input_value = values["-INPUT-"]
        if input_value.isnumeric():
            table_data.append([len(table_data) + 1, float(input_value)])
            window["-TABLE-"].update(values=table_data)
            window["-INPUT-"].update("")

window.close()
