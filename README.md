# labview-client-for-micropython
This is a client implemented in [LabVIEW](https://www.ni.com/en-za/shop/labview.html) that interacts with an embedded device or constrained system that runs micropython.

> [MicroPython](https://github.com/micropython/micropython)  - a lean and efficient Python implementation for microcontrollers and constrained systems 

## Introduction

This is a small library / client implemented in LabVIEW to interact with a target device running MicroPython.

>MicroPython is a project, that aims to put an implementation of Python 3.x on microcontrollers and small embedded systems. You can find the official website at [micropython.org](micropython.org).


Essentially, a library for micropython will use a serial port to interact with the device. One requires nothing else than that, and as such a program like [Putty](https://www.putty.org/) can be used to open a session to the device and pretty much run python code / commands.

What this library makes easy is the integration in Test Systems. One such example is [TestStand](https://www.ni.com/en-za/shop/electronic-test-instrumentation/application-software-for-electronic-test-and-instrumentation-category/what-is-teststand.html) which is a popular Test Executive Software developed by [National Instrument](https://www.ni.com). As a matter of fact, this library was initially created for this very purpose. It is made available to speed up development of similar Systems.


## Design

The library has 4 main VIs:
- ``Initialize.vi``: To Initialize the comport
- ``Close.vi``: To close the comport
- ``SendCommand.vi``: Will send a command to the device and wait for its response
- ``UploadScript.vi``: Will take in a python script and send it over the serial port to the target device. ``SendCommand.vi`` can then be used to invoke functions and variables defined within this script.

To perform, transmit and receive operation, the VI ``TxRx.vi`` will send a message to the target device and wait for a response until some (stopping) conditions are met.

An overview can be found [here](/docs/MicroPython.lvlib.html)


## Getting Started

To get started, one needs some hardware running micropython. MicroPython requires minimum 128K of Flash, 8K of RAM so not all arduino board support it. However, the [official github page](https://github.com/micropython/micropython) lists a few boards that will run micropython. The PyBoard is the official board, but one can use the popular ``ESP32`` or the ``ESP8266``.

Once Micropython is installed on your hardware, you can test that everything is working by opening a Serial Communication Session using [Putty](https://www.putty.org/) on hte comport used by your board. 

The same operation can be reproduced using this library by calling ``Initialize.vi`` first, then ``SendCommand.vi`` and ``UploadScript.vi`` as necessary.
