#!/usr/bin/env python

# Copyright (c) 2018, Ziping Chen.
# All rights reserved.
#
# File: bpi_robot_teleop_key.py

import rospy

from bpi_robot_base.msg import motor_speed

import Tkinter as tk
# import cv2 as cv
import os

msg = """
Control Your BPI-Robot!
---------------------------
Moving around:
            <Up>
    <Left> <Down> <Right>

<+>/<-> : increase/decrease max speeds by 10%
<Space> : force stop

CTRL-C to quit
"""

speed = 0.


def vels(speed):
    return "currently:\tspeed %.2f" % speed


def pub_speed(mot_speed):
    global pub
    pub.publish(mot_speed)


def up(event):
    global speed, mot_speed
    mot_speed.left_motor_speed = speed
    mot_speed.right_motor_speed = speed
    pub_speed(mot_speed)
    print('up')


def down(event):
    global speed, mot_speed
    mot_speed.left_motor_speed = -speed
    mot_speed.right_motor_speed = -speed
    pub_speed(mot_speed)
    print('down')


def left(event):
    global speed, mot_speed
    mot_speed.left_motor_speed = -speed
    mot_speed.right_motor_speed = speed
    pub_speed(mot_speed)
    print('left')


def right(event):
    global speed, mot_speed
    mot_speed.left_motor_speed = speed
    mot_speed.right_motor_speed = -speed
    pub_speed(mot_speed)
    print('right')


def quit(event):
    global root
    global speed, mot_speed
    speed = 0.
    mot_speed.left_motor_speed = speed
    mot_speed.right_motor_speed = speed
    pub_speed(mot_speed)
    print('quit')
    root.destroy()


def stop(event):
    global speed, mot_speed, var
    speed = 0.
    mot_speed.left_motor_speed = speed
    mot_speed.right_motor_speed = speed
    pub_speed(mot_speed)
    print('stop')
    var.set(vels(speed))


def speed_up(event):
    global speed, mot_speed, var
    speed += 0.01
    if speed > 0.9:
        speed = 1.0
    if mot_speed.left_motor_speed >= 0:
        mot_speed.left_motor_speed = speed
    else:
        mot_speed.left_motor_speed = -speed
    if mot_speed.right_motor_speed >= 0:
        mot_speed.right_motor_speed = speed
    else:
        mot_speed.right_motor_speed = -speed
    pub_speed(mot_speed)
    var.set(vels(speed))


def speed_down(event):
    global speed, mot_speed, var
    speed -= 0.01
    if speed < 0.1:
        speed = 0.0
    if mot_speed.left_motor_speed >= 0:
        mot_speed.left_motor_speed = speed
    else:
        mot_speed.left_motor_speed = -speed
    if mot_speed.right_motor_speed >= 0:
        mot_speed.right_motor_speed = speed
    else:
        mot_speed.right_motor_speed = -speed
    pub_speed(mot_speed)
    var.set(vels(speed))


def setup_key(frame):

    frame.bind_all("<Key-Up>", up)
    frame.bind_all("<Key-Down>", down)
    frame.bind_all("<Key-Left>", left)
    frame.bind_all("<Key-Right>", right)
    frame.bind_all("<Key-equal>", speed_up)
    frame.bind_all("<Key-plus>", speed_up)
    frame.bind_all("<Key-underscore>", speed_down)
    frame.bind_all("<Key-minus>", speed_down)
    frame.bind_all("<Control-c>", quit)
    frame.bind_all("<Key-space>", stop)


if __name__ == "__main__":
    pub = rospy.Publisher('pwm_pub', motor_speed, queue_size=1000)
    rospy.init_node('bpi_robot_teleop')
    mot_speed = motor_speed()
    print(os.getcwd())
    root = tk.Tk()
    frame = tk.Frame(root)
    setup_key(frame)
    print(msg)
    frame.pack()
    var = tk.StringVar()
    label = tk.Label(frame, textvariable=var, width=100, height=100)
    var.set(vels(speed))
    label.pack()
    root.title("bpi_robot_teleop")
    root.mainloop()
