# BPI-robot-1
 A mobile robot based on ROS and Banana Pi.(Version 1)

![BPI-robot-v1.0.jpg](https://github.com/techping/BPI-robot-1/raw/master/BPI-robot-v1.0.jpg)

## Hardware  Environment

+ Banana Pi M64

The key features:
1. 1.2 Ghz Quad-Core ARM Cortex A53 64-Bit Processor-R18
2. GB DDR3 SDRAM
3. 8G EMMC
4. 10/100/1000Mbps Ethernet
5. WiFi (AP6212) & Bluetooth

[http://www.banana-pi.org/m64.html](http://www.banana-pi.org/m64.html)

[http://linux-sunxi.org/Sinovoip_Banana_Pi_M64](http://linux-sunxi.org/Sinovoip_Banana_Pi_M64)

![Banana Pi M64](http://www.banana-pi.org/images/bpi-images/M64/m6111.jpg)

+ L298N Dual Full Bridge Motor Driver

![L298N](http://img.dxcdn.com/productimages/sku_408436_1.jpg)

+ USB Camera

![usb_cam](https://i.ebayimg.com/images/g/PMIAAOSwacdZcAPO/s-l300.jpg)

+ Car Robot Model

![Car](https://gd4.alicdn.com/imgextra/i4/94674554/TB2KSTqXVXXXXXtXXXXXXXXXXXX_!!94674554.jpg)

+ 7.4V(2S) Lithium-ion Battery

![battery](https://images-na.ssl-images-amazon.com/images/I/51uUiAKJ4gL._SL1000_.jpg)

## Software Environment

+ ROS Kinetic

[http://www.ros.org/](http://www.ros.org/)

![ROS](http://www.ros.org/wp-content/uploads/2013/10/rosorg-logo1.png)

+ Banana Pi M64 image

[http://forum.banana-pi.org/c/BPI-M64/M63image](http://forum.banana-pi.org/c/BPI-M64/M63image)

+ BPI-WiringPi2 Library

[https://github.com/BPI-SINOVOIP/BPI-WiringPi2](https://github.com/BPI-SINOVOIP/BPI-WiringPi2)

Use this library to control the pins.

## To Build Up

### 1.  Install Banana Pi M64 image

Choose your favorite image to install.

### 2. Install ROS on both your PC and Banana Pi

Refer to the wiki: [http://wiki.ros.org/kinetic/Installation/](http://wiki.ros.org/kinetic/Installation/)

+ After installation:

On the Banana Pi:

```shell
$ export ROS_HOSTNAME=bananapim64 && export ROS_MASTER_URI=http://bananapim64:11311
$ roscore
```

On your PC:

```shell
$ export ROS_HOSTNAME=`hostname` && export ROS_MASTER_URI=http://bananapim64:11311
```

### 3. Clone this repository and build up use catkin_make

On the Banana Pi:

```shell
$ rosrun pwm_control pwm_control
```

On your PC:

```shell
$ rosrun bpi_robot_teleop bpi_robot_teleop_control.py
```
### 4. Enjoy it

Furthermore, you can run [usb_cam](http://wiki.ros.org/usb_cam) to do video surveillance and build up [ORB_SLAM2](https://github.com/raulmur/ORB_SLAM2) to build your map.
