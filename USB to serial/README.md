# USB to serial

<img align="right" src="../_common/PlaceholderImage.png">

An FT232 breakout board with the connectors I more often want to use:

* On the RS232 side: a 3 pin screw terminal as well as the 6 pin 0.1" classic FTDI header
* On the USB side: a female USB B connector

This board is intended to be small and cheap so I can leave it inside any projects need a quick and simple USB connection.

No care has been taken to layout the USB traces so that the differential signals have matched impedances; they're short traces and USB 2.0 isn't that fast so hopefully it won't affect things too much.

## Design files

This board was designed using the [Upverter](https://upverter.com) web service.

The schematic, board layout and bill of materials can be viewed [here](https://upverter.com/Trebuchetindustries/9bcfd8e23a60948c/USB-to-serial/). Exports from Upverter are [available in a subdirectory](./Upverter%20exports).

## TODO

* [ ] Build and test prototype
* [ ] Rename project
* [ ] Redo all traces; they're too thick, messy and overlap with the silkscreen
* [ ] Add some screw holes or some other way of mounting the board
* [ ] Figure out how bad the USB traces are and fix them if necessary/possible

## Licence

Copyright © 2016 Phil Baldwin

This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.

You should have received a copy of the license along with this work. If not, see <http://creativecommons.org/licenses/by-sa/4.0/>.
