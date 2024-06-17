import PySimpleGUI as sg
import cv2

layout = [
    [sg.Image(key="-IMAGE-")],
    [
        sg.Text(
            "No. of people: 0",
            key="-TEXT-",
            expand_x=True,
            justification="center",
            font=("Helvetica", 20),
            background_color="black",
        )
    ],
]

window = sg.Window("Face Detector", layout)

# get video
video = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    event, values = window.read(timeout=0)

    if event == sg.WIN_CLOSED:
        break

    _, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.3, minNeighbors=7, minSize=(50, 50)
    )

    # highlight the faces
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # update the image
    imgbytes = cv2.imencode(".png", frame)[1].tobytes()
    window["-IMAGE-"].update(data=imgbytes)

    # update the no. of people
    window["-TEXT-"].update(f"No. of people: {len(faces)}")

window.close()
