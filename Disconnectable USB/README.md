# Disconnectable USB

<img align="right" src="../_common/PlaceholderImage.png">

Have you ever wanted to plug in a USB 2.0 device while disconnecting one or more of the USB signal (e.g. connect the power lines but disconnect the data lines)? This little board provides a way to do that.

This board is designed to plug directly into a female USB-A 2.0 port. All 4 USB signals (power, ground and the 2 data lines) are then routed 4 position switch, which can be used to choose which of the signals make it through to the female USB-A connector mounted on the other side of the board.

Be very careful with the PCB thickness when manufacturing this board. PCB thickness is very important because the board is meant to be plugged directly into a USB port; make the PCB too thick and it won't fit in the port ... make the PCB too thin and it won't stay in the port or make stable electrical connections. The standard PCB thickness of 1.6mm will **not** work for this PCB. You want a PCB about 2.1 mm thick.

## TODO

* [ ] Consider alternative switches; possibly with footprint compatible with jumpers as well
* [ ] Silkscreen labels
* [ ] Name and version number on bottom silkscreen

## Design files

This board was originally designed using the [Circuits.io](https://circuits.io) web service. That design can be viewed [here]( https://circuits.io/circuits/550192-usb-inline-headers).

This board was subsequently redesigned using the [Upverter](https://upverter.com) web service.

The schematic, board layout and bill of materials can be viewed [here](https://upverter.com/Trebuchetindustries/7628e176f5c359c1/Disconnectable-USB/). Exports from Upverter are [available in a subdirectory](./Upverter%20exports).

## Licence

Copyright © 2016 Phil Baldwin

This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.

You should have received a copy of the license along with this work. If not, see <http://creativecommons.org/licenses/by-sa/4.0/>.
