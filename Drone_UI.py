# import tkinter
from tkinter import *
import time
from pyardrone import ARDrone


class DroneInterface:

    def __init__(self, master):
        # Create and place UI elements
        # row 0
        self.btn_takeoff = Button(master, text="Take Off", command=self.takeoff)
        self.btn_takeoff.grid(row=0, column=0, columnspan=2, padx=50)
        # row 1
        self.btn_land = Button(master, text="Land", command=self.land)
        self.btn_land.grid(row=1, column=0, columnspan=2)
        # row 2
        self.cbx_manual = Checkbutton(master, text="Enable manual control (placeholder)")
        self.cbx_manual.grid(row=2, column=0)
        self.btn_forward = Button(master, text="Forward", command=self.move_front)
        self.btn_forward.grid(row=2, column=1)
        self.btn_up = Button(master, text="Up", command=self.move_up)
        self.btn_up.grid(row=2, column=3)
        self.btn_backward = Button(master, text="Backward", command=self.move_back)
        self.btn_backward.grid(row=2, column=5)
        # row 3
        self.lbl_dronestats = Label(master, text="")
        self.lbl_dronestats.grid(row=3, column=0)
        self.btn_left = Button(master, text="Left", command=self.move_left)
        self.btn_left.grid(row=3, column=2)
        self.btn_right = Button(master, text="Right", command=self.move_right)
        self.btn_right.grid(row=3, column=4)
        # row 4
        self.btn_ccw = Button(master, text="CCW")
        self.btn_ccw.grid(row=4, column=1)
        self.btn_down = Button(master, text="Down", command=self.move_down)
        self.btn_down.grid(row=4, column=3)
        self.btn_cw = Button(master, text="CW")
        self.btn_cw.grid(row=4, column=5)

    def takeoff(self):
        drone.takeoff()

    def land(self):
        drone.land()

    def move_up(self):
        drone.move(up=0.3)
        time.sleep(1)
        drone.hover()

    def move_down(self):
        drone.move(down=0.3)
        time.sleep(1)
        drone.hover()

    def move_left(self):
        drone.move(left=0.3)
        time.sleep(1)
        drone.hover()

    def move_right(self):
        drone.move(right=0.3)
        time.sleep(1)
        drone.hover()

    def move_front(self):
        drone.move(forward=0.3)
        time.sleep(1)
        drone.hover()

    def move_back(self):
        drone.move(backward=0.3)
        time.sleep(1)
        drone.hover()


def program_close():
    print("Quit.")
    running = False
    root.destroy()


if __name__ == "__main__":

    drone = ARDrone()
    root = Tk()
    window = DroneInterface(root)
    root.mainloop()

    if drone:
        print("Landing")
        drone.land()
        drone.close()

    print(".")
