import PySimpleGUI as sg

smileys = [
    "happy",
    [":)", ":D", "xD", "<3"],
    "sad",
    [":(", ":-(", ":-<", "T_T"],
    "other",
    [";)", ":-P", ":-O"],
]
smiley_events = smileys[1] + smileys[3] + smileys[5]

menu_layout = [
    ["File", ["Open", "Save", "---", "Exit"]],
    ["Tools", ["Word Count"]],
    ["Add", smileys],
]

sg.theme("GrayGrayGray")
layout = [
    [sg.Menu(menu_layout)],
    [sg.Text("Untitled", key="-DOCNAME")],
    [sg.Multiline(size=(80, 30), key="-TEXTBOX-")],
]

window = sg.Window("Text Editor", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "Exit":
        break

    if event == "Open":
        file_path = sg.popup_get_file("Open File", no_window=True)
        if file_path:
            with open(file_path, "r") as file:
                text = file.read()
                file_name = file_path.split("/")[-1]

            window["-TEXTBOX-"].update(text)
            window["-DOCNAME"].update(file_name)

    if event == "Save":
        file_path = (
            sg.popup_get_file("Save File", save_as=True, no_window=True) + ".txt"
        )
        if file_path:
            with open(file_path, "w") as file:
                file.write(values["-TEXTBOX-"])
                file_name = file_path.split("/")[-1]

            window["-DOCNAME"].update(file_name)

    if event == "Word Count":
        words = values["-TEXTBOX-"].split()
        word_count = len(words)
        char_count = sum(len(word) for word in words)
        sg.popup(f"Word Count: {word_count}\nCharacter Count: {char_count}")

    if event in smiley_events:
        cur_text = values["-TEXTBOX-"]
        cur_text = cur_text + " " + event
        window["-TEXTBOX-"].update(cur_text)


window.close()
