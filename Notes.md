# PySimpleGUI - A Beginner's Guide

PySimpleGUI is a Python package that simplifies the creation of GUIs. It is a wrapper around tkinter and Qt. It is easy to use and has a lot of features. It is a good choice for beginners and for small projects. It is not suitable for large projects.

#### Installation

To install PySimpleGUI, run the following command:

```bash
pip install PySimpleGUI
```

## Components

Components are the building blocks of a GUI. They are the elements that make up the interface. PySimpleGUI provides a wide range of components that can be used to create a GUI. Some of the most common components are:

- Text
- Input
- Button
- Checkbox
- Radio
- Listbox

These components can be combined to create layouts in the form of rows and columns. The layout can be customized using the `sg.theme()` function.

#### Example

Here is an example of a simple GUI created using PySimpleGUI:

```python
import PySimpleGUI as sg

layout = [
    [sg.Text('Enter your name:'), sg.InputText()],
    [sg.Button('Submit'), sg.Button('Cancel')]
]

window = sg.Window('Simple GUI', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

    if event == 'Submit':
        sg.popup(f'Hello, {values[0]}!')

window.close()
```

This code creates a simple GUI with an input field and two buttons. When the user clicks the "Submit" button, a popup is displayed with the message "Hello, {name}".W

## Events

An event is triggered by some action in the GUI, such as clicking a button or entering text in an input field. Name of the event is the name, or the key, of the component that triggered the event.

Each element in the layout has a key that can be used to identify the element in the event handler. This can be used to identify an element if same element is used multiple times in the layout.

```python
import PySimpleGUI as sg

layout = [
    [sg.Button('Submit', key='submit1')],
    [sg.Button('Submit', key='submit2')],
]

window = sg.Window('Event Handling', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == 'submit1':
        sg.popup('Button 1 clicked')

    if event == 'submit2':
        sg.popup('Button 2 clicked')

window.close()
```

There is usually a naming convention for keys. For example, `-BUTTON-` for buttons, `-INPUT-` for input fields, `-CHECKBOX-` for checkboxes, etc.

## Values

Values are the data entered by the user in the GUI. They are stored in a dictionary with the key of the component as the key and the value entered by the user as the value.

```python
import PySimpleGUI as sg

layout = [
    [sg.Text('Enter your name:'), sg.InputText(key='name')],
    [sg.Button('Submit')]
]

window = sg.Window('Values', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == 'Submit':
        name = values['name']
        sg.popup(f'Hello, {name}!')

window.close()
```

## Updating Elements

Every element has an update method which can be used to change text, visibility, etc. of the element.

```python
import PySimpleGUI as sg

layout = [
    [sg.Text('Enter your name:'), sg.InputText(key='name')],
    [sg.Button('Submit', key='submit')],
    [sg.Text('Hello, ', key='output')]
]

window = sg.Window('Updating Elements', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == 'submit':
        name = values['name']
        window['output'].update(f'Hello, {name}!')

window.close()
```
