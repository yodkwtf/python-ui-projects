import PySimpleGUI as sg
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.figure


def update_graph(data):
    axes = fig.axes
    x = [row[0] for row in data]
    y = [int(row[1]) for row in data]
    axes[0].plot(x, y, "r-")
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack()


table_data = []

layout = [
    [
        sg.Table(
            headings=["No.", "Result"],
            values=table_data,
            expand_x=True,
            hide_vertical_scroll=True,
            key="-TABLE-",
            cols_justification=["center", "center"],
        )
    ],
    [sg.Input(key="-INPUT-", expand_x=True), sg.Button("Add")],
    [sg.Canvas(key="-CANVAS-")],
]

window = sg.Window("Graph Plotter", layout, finalize=True)

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
            update_graph(table_data)

window.close()
