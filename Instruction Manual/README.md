<p align="left"><img width="270" height="170" src="https://github.com/OpenSourceNeuro/Spikeling-V2/blob/main/Images/SpikyLogo.png">

<h1 align="center"> Instruction Manual</h1></p>

<h2 align="left"> Overview</h1></p>

<p style='text-align: justify;'>

This document contains detailed instructions to connect, install and use Spikeling v2.2

The hardware itself is controlled by a <a href="https://www.espressif.com/en/products/devkits/esp32-devkitc">ESP-32 development board</a> (ESP-32 WROVER-E). It runs on a C++ code which can be updated through the <a href="https://www.arduino.cc">Arduino IDE</a>. The <a href="https://github.com/OpenSourceNeuro/Spikeling-V2/tree/main/Arduino%20Code">Arduino Code session</a> in this repository details how to modify the Spikeling code.


<strong>In order to communicate with the ESP-32 micro-controller, users must first install the latest SiLabs <a href="https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers">CP210x driver</a></strong>

The software itself consists on a Graphical User Interface (GUI) built on python using the pyqt6/pyside6 library packages:
  - Users can run the <a href="https://github.com/OpenSourceNeuro/Spikeling-V2/tree/main/GUI/PyQt">python code</a> directly by executing the <strong>Main.py</strong> file.
  - A Windows executable file is also available and can be found <a href="https://github.com/OpenSourceNeuro/Spikeling-V2/tree/main/GUI/Windows">here</a>
  - A Linux version is available <a href="">here</a>
  - And a Mac version <a href="">here</a>

  </p>

  ***

<h2 align="left">Spikeling GUI</h2></p>

<p style='text-align: justify;'>

Once the CP210x has been installed, users can launch the Spikeling software.

On the home page, menus can be found on the left tab

</p>



<img align="left"  src="https://github.com/OpenSourceNeuro/Spikeling-V2/blob/main/Images/Spikeling_Menu.png" width="176" height="54">
<h4 align="left">Spikeling Menu</h4></p>


</p>
