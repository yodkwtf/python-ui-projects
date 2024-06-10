import PySimpleGUI as sg

# constants
FIELD_SIZE = 400
CELL_NUM = 10
CELL_SIZE = FIELD_SIZE // CELL_NUM
apple_pos = (1, 1)

field = sg.Graph(
    canvas_size=(FIELD_SIZE, FIELD_SIZE),
    graph_bottom_left=(0, 0),
    graph_top_right=(FIELD_SIZE, FIELD_SIZE),
    background_color="black",
)

sg.theme("Green")
layout = [[field]]

window = sg.Window("Snake Game", layout, return_keyboard_events=True)

while True:
    event, values = window.read(timeout=10)

    if event == sg.WIN_CLOSED:
        break

    if event == "Left:37":
        print("Left")

    if event == "Right:39":
        print("Right")

    if event == "Up:38":
        print("Up")

    if event == "Down:40":
        print("Down")

    # draw apple
    left_bottom = (apple_pos[0] * CELL_SIZE, apple_pos[1] * CELL_SIZE)
    right_top = ((apple_pos[0] + 1) * CELL_SIZE, (apple_pos[1] + 1) * CELL_SIZE)
    field.DrawRectangle(left_bottom, right_top, "red")


window.close()
