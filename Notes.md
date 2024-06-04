## PySimpleGUI

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
