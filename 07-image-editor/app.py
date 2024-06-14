import PySimpleGUI as sg
from PIL import Image, ImageFilter, ImageOps
from io import BytesIO


# function to resize the image
def resize_image(image, max_width, max_height):
    width, height = image.size
    aspect_ratio = width / height

    if width > max_width:
        width = max_width
        height = int(width / aspect_ratio)

    if height > max_height:
        height = max_height
        width = int(height * aspect_ratio)

    return image.resize((width, height), Image.Resampling.LANCZOS)


# function to update the image
def update_image(original, blur, contrast, emboss, contour, flipx, flipy):
    global image
    image = original.filter(ImageFilter.GaussianBlur(blur))
    image = image.filter(ImageFilter.UnsharpMask(contrast))

    if emboss:
        image = image.filter(ImageFilter.EMBOSS())
    if contour:
        image = image.filter(ImageFilter.CONTOUR())

    if flipx:
        image = ImageOps.mirror(image)
    if flipy:
        image = ImageOps.flip(image)

    # resize image to fit within max dimensions
    max_width, max_height = 600, 450
    image = resize_image(image, max_width, max_height)

    # convert image to something we can work with
    bio = BytesIO()
    image.save(bio, format="PNG")
    bio.seek(0)

    # update the window with the new image
    window["-IMAGE-"].update(data=bio.getvalue())


# get the image path
image_path = sg.popup_get_file("Open", no_window=True)

# create layout
control_col = sg.Column(
    [
        [
            sg.Frame(
                "Blur",
                layout=[[sg.Slider((0, 10), orientation="h", key="-BLUR-")]],
            )
        ],
        [
            sg.Frame(
                "Contrast",
                layout=[[sg.Slider((0, 10), orientation="h", key="-CONTRAST-")]],
            )
        ],
        [
            sg.Checkbox("Emboss", key="-EMBOSS-"),
            sg.Checkbox("Contour", key="-CONTOUR-"),
        ],
        [sg.Checkbox("Flip x", key="-FLIPX-"), sg.Checkbox("Flip y", key="-FLIPY-")],
        [sg.Button("Save Image", key="-SAVE-")],
    ]
)
image_col = sg.Column([[sg.Image(key="-IMAGE-")]])
layout = [[control_col, image_col]]

# create the window and load the image
original_image = Image.open(image_path)
window = sg.Window("Image Editor", layout, finalize=True)

while True:
    event, values = window.read(timeout=50)
    if event == sg.WIN_CLOSED:
        break

    update_image(
        original_image,
        values["-BLUR-"],
        values["-CONTRAST-"],
        values["-EMBOSS-"],
        values["-CONTOUR-"],
        values["-FLIPX-"],
        values["-FLIPY-"],
    )

    # save the image
    if event == "-SAVE-":
        file_path = sg.popup_get_file("Save", save_as=True, no_window=True) + ".png"
        image.save(file_path)

window.close()
