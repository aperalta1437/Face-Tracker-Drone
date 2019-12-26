import numpy as np  # Importing the numpy package is not necessary since the cv2 package uses it automaticaly.
import cv2  # Importing the cv2 package to get access to it.
import pickle  # Importing the pickle module to get access to it.


def make_1080p():
    """The make_1080 function sets the resolution of the screen to 1080p."""
    cap.set(3, 1920)
    cap.set(4, 1080)


def make_720p():
    """The make_720p function sets the resolution of the screen to 720p."""
    cap.set(3, 1280)
    cap.set(4, 720)


def make_480p():
    """The make_480p function sets the resolution of the screen to 480p."""
    cap.set(3, 640)
    cap.set(4, 480)


def change_res(width, height):
    """
    The change_res function sets the resolution of the screen to the one specified in the parameters.
    :param width: the width to which the frame will be set to.
    :param height: the height to which the frame will be set to.
    """
    cap.set(3, width)
    cap.set(4, height)


def rescale_frame(frame0, percent=75):
    """
    Set dimensions for the video capture based on the given resolution.
    :param frame0: the given frame to rescale.
    :param percent: the percent rescaling for the frame's resolution.
    :return: the resized frame.
    """
    width = int(frame0.shape[1] * percent / 100)
    height = int(frame0.shape[0] * percent / 100)
    dim = (width, height)
    return cv2.resize(frame0, dim, interpolation=cv2.INTER_AREA)


# Standard Video Dimensions Sizes
STD_DIMENSIONS = {
    "480p": (640, 480),
    "720p": (1280, 720),
    "1080p": (1920, 1080),
    "4k": (3840, 2160),
}


def get_dims(res='1080p'):
    """
    The get_dims function returns the width and height of the specified resolution.
    :param res: the specified resolution.
    :return: the width and height corresponding to the specified resolution.
    """
    width, height = STD_DIMENSIONS['480p']
    if res in STD_DIMENSIONS:
        width, height = STD_DIMENSIONS[res]
    change_res(width, height)
    return width, height


# Counting variables to keep count of the taken pictures.
count0 = 0
count1 = 0
count2 = 0
checked = 0
person = ''
# Creating CascadeClassifiers objects to detect frontal face, eyes and smiles.
face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
eye_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_smile.xml')

# Creating the face recognizer that will be used to identified who the person is.
recognizer = cv2.face.LBPHFaceRecognizer_create()
# Reading the trainner that is equipped with the different faces features that will be used to identify the person.
recognizer.read("trainner.yml")

# Creating the label that will referenced the person's given ID.
labels = {"person_name": 1}

with open("labels.pickle", 'rb') as f:
    og_labels = pickle.load(f)
    labels = {v: k for k, v in og_labels.items()}

cap = cv2.VideoCapture(0)    # Creating a video capture object that takes the default camera
                                                    # as the input referenced.

make_1080p()  # Setting the resolution of the video capture object to 1080p.

# The while loop to execute all the necessary actions frame-by-frame.
while True:
    # Calling to read method of the video capture object to return the taken frame and the validity of the taken frame.
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    for (x, y, w, h) in faces:
        # print(x, y, w, h)
        roi_gray = gray[y: (y + h), x: (x + w)]  # (ycord_start, ycord_end)
        roi_color = frame[y: (y + h), x: (x + w)]

        # recognition? deep learned model predict keras tensorflow pytorch scikit learn.
        id_, conf = recognizer.predict(roi_gray)
        if 35 <= conf:  # <= 70:  # and conf<=85:
            print(conf)
            # print(id_)
            # print(labels[id_])

            font = cv2.FONT_HERSHEY_SIMPLEX
            name = labels[id_]
            color = (255, 255, 255)
            stroke = 2

            if checked == 0 or person == name:

                if checked == 0:
                    checked += 1
                    person = name

                cv2.putText(frame, name, (x, y), font, 1, color, stroke, cv2.LINE_AA)
                if name == 'angel':
                    ri, pic = cap.read()
                    if ri:
                        cv2.imwrite('images/Angel/now.jpg', pic)
                        if count0 < 10:
                            cv2.imwrite('images/Angel/now' + str(count0) + '.jpg', pic)
                            count0 += 1
                elif name == 'loymi':
                    ri, pic = cap.read()
                    if ri:
                        cv2.imwrite('images/Angel/now.jpg', pic)
                        if count1 < 10:
                            cv2.imwrite('images/Loymi/now' + str(count1) + '.jpg', pic)
                            count1 += 1
                elif name == 'yao':
                    ri, pic = cap.read()
                    if ret:
                        cv2.imwrite('images/Angel/now.jpg', pic)
                        if count2 < 10:
                            cv2.imwrite('images/Yao/now' + str(count2) + '.jpg', pic)
                            count2 += 1

                img_item = "my-image.png"
                cv2.imwrite(img_item, roi_gray)

                color = (255, 0, 0)  # BGR 0-255
                stroke = 2
                end_cord_x = x + w
                end_cord_y = y + h
                cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)

                center_color = (0, 0, 255)
                center_stroke = 1
                center_cord_x = 550
                center_cord_y = 225
                center_w = 225
                center_h = 225
                center_end_cord_x = center_cord_x + 225
                center_end_cord_y = center_cord_y + 225
                cv2.rectangle(frame, (center_cord_x, center_cord_y), (center_end_cord_x, center_end_cord_y),
                              center_color, center_stroke)

                if x > center_cord_x:
                    print('Move right')

                if x < center_cord_x:
                    print('Move left')

                if y > center_cord_y:
                    print('Move up')

                if y < center_cord_y:
                    print('Move down')

                if w < center_w or h < center_h:
                    print('Get closer')

                if w > center_w or h > center_h:
                    print('Get away')

                    # Detecting where are the eyes located inside the gray frame.
                    eyes = eye_cascade.detectMultiScale(roi_gray)
                    # Drawing the rectangles around the eyes.
                    for (ex, ey, ew, eh) in eyes:
                        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

                    # Detecting where is the smile located inside the gray frame.
                    smile = smile_cascade.detectMultiScale(roi_gray)
                    # Drawing the rectangle around the smile.
                    for (sx, sy, sw, sh) in smile:
                        cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0, 0, 255), 2)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    # Closing to frame if the "q" key is pressed.
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

    elif cv2.waitKey(20) & 0xFF == ord('a'):
        checked = 0
        person = ''

cap.release()  # When everything done, release the capture.
cv2.destroyAllWindows()  # Destroying all created windows after the frame has been closed.
