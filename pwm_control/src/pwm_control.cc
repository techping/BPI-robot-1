/*
# Copyright (c) 2018, Ziping Chen.
# All rights reserved.
#
# File: pwm_control.cc
*/

#include "ros/ros.h"
#include "bpi_robot_base/motor_speed.h"
#include <wiringPi.h>
#include <softPwm.h>
#include <cmath>

#define LEFT_MOT_DIE 7
#define LEFT_MOT_PWM 11

#define RIGHT_MOT_DIE 12
#define RIGHT_MOT_PWM 13

#define POSITIVE 1
#define NEGETIVE 0

void pwm_callback(const bpi_robot_base::motor_speed::ConstPtr& msg)
{
        signed char left = msg->left_motor_speed * 100, right = msg->right_motor_speed * 100;
        if (left < 0) {
                digitalWrite(LEFT_MOT_DIE, NEGETIVE);
                softPwmWrite(LEFT_MOT_PWM, abs(left));
        } else {
                digitalWrite(LEFT_MOT_DIE, POSITIVE);
                softPwmWrite(LEFT_MOT_PWM, 100 - abs(left));
        }
        if (right < 0) {
                digitalWrite(RIGHT_MOT_DIE, NEGETIVE);
                softPwmWrite(RIGHT_MOT_PWM, abs(right));
        } else {
                digitalWrite(RIGHT_MOT_DIE, POSITIVE);
                softPwmWrite(RIGHT_MOT_PWM, 100 - abs(right));
        }
        ROS_INFO("%s -> LEFT[%lf] RIGHT[%lf]", __func__, msg->left_motor_speed, msg->right_motor_speed);
}


int main(int argc, char **argv)
{
    /* ROS init */
    ros::init(argc, argv, "pwm_control");
    ros::NodeHandle n;
    /* Initial BPI-wiringPi Library */
    wiringPiSetupPhys();
    /* Initial Direction Pins */
    pinMode(LEFT_MOT_DIE, OUTPUT);
    pinMode(RIGHT_MOT_DIE, OUTPUT);
    digitalWrite(LEFT_MOT_DIE, POSITIVE);
    digitalWrite(RIGHT_MOT_DIE, POSITIVE);
    /* Initial PWM Pins */
    pinMode(LEFT_MOT_PWM, SOFT_PWM_OUTPUT);
    pinMode(RIGHT_MOT_PWM, SOFT_PWM_OUTPUT);
    softPwmCreate(LEFT_MOT_PWM, 0, 100);
    softPwmCreate(RIGHT_MOT_PWM, 0, 100);
    softPwmWrite(LEFT_MOT_PWM, 100);
    softPwmWrite(RIGHT_MOT_PWM, 100);
    /* Initial Topic Subscriber */
    ros::Subscriber sub = n.subscribe("pwm_pub", 1000, pwm_callback);
    ros::spin();
    return 0;
}
