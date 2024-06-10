import PySimpleGUI as sg
from time import time
from random import randint


def convert_pos_to_pixel(cell):
    left_bottom = (cell[0] * CELL_SIZE, cell[1] * CELL_SIZE)
    right_top = ((cell[0] + 1) * CELL_SIZE, (cell[1] + 1) * CELL_SIZE)
    return left_bottom, right_top


def place_apple():
    apple_pos = randint(0, CELL_NUM - 1), randint(0, CELL_NUM - 1)
    while apple_pos in snake_body:
        apple_pos = randint(0, CELL_NUM - 1), randint(0, CELL_NUM - 1)
    return apple_pos


# constants
FIELD_SIZE = 400
CELL_NUM = 20
CELL_SIZE = FIELD_SIZE // CELL_NUM

# snake
snake_body = [(4, 4), (3, 4), (2, 4)]
DIRECTIONS = {"UP": (0, 1), "DOWN": (0, -1), "LEFT": (-1, 0), "RIGHT": (1, 0)}
direction = DIRECTIONS["UP"]

# apple
apple_pos = place_apple()

field = sg.Graph(
    canvas_size=(FIELD_SIZE, FIELD_SIZE),
    graph_bottom_left=(0, 0),
    graph_top_right=(FIELD_SIZE, FIELD_SIZE),
    background_color="black",
)

sg.theme("Green")
layout = [[field]]

window = sg.Window("Snake Game", layout, return_keyboard_events=True)

start_time = time()
while True:
    event, values = window.read(timeout=10)

    if event == sg.WIN_CLOSED:
        break
    if event == "Left:37":
        direction = DIRECTIONS["LEFT"]
    if event == "Right:39":
        direction = DIRECTIONS["RIGHT"]
    if event == "Up:38":
        direction = DIRECTIONS["UP"]
    if event == "Down:40":
        direction = DIRECTIONS["DOWN"]

    # update snake position
    time_since_start = time() - start_time
    if time_since_start > 0.25:
        start_time = time()

        # apple eaten
        if snake_body[0] == apple_pos:
            apple_pos = place_apple()
            snake_body.append(snake_body[-1])

        # snake update
        new_head = (snake_body[0][0] + direction[0], snake_body[0][1] + direction[1])
        snake_body.insert(0, new_head)
        snake_body.pop()

        # check death
        if (
            new_head in snake_body[1:]  # snake eats itself
            or new_head[0] < 0  # snake goes left of the field
            or new_head[0] >= CELL_NUM  # snake goes right of the field
            or new_head[1] < 0  # snake goes up of the field
            or new_head[1] >= CELL_NUM  # snake goes down of the field
        ):
            sg.popup("Game Over")
            break

        # reset field
        field.DrawRectangle((0, 0), (FIELD_SIZE, FIELD_SIZE), "black")

        # draw apple
        left_bottom, right_top = convert_pos_to_pixel(apple_pos)
        field.DrawRectangle(left_bottom, right_top, "red")

        # draw snake
        for index, part in enumerate(snake_body):
            color = "yellow" if index == 0 else "green"
            left_bottom, right_top = convert_pos_to_pixel(part)
            field.DrawRectangle(left_bottom, right_top, color)


window.close()
