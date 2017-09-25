# Ethernet tap

A simple Ethernet tap board designed to make it easy to sniff Ethernet traffic. 

... existing taps ... problem with existing taps ...

The board has 3 [8P8C plugs](https://en.wikipedia.org/wiki/Modular_connector#8P8C). .......................

... wiring diagram ...



This board is only intended to work with only 10/100 Ethernet, it will not be able to sniff gigabit Ethernet traffic as 

No care has been taken to layout the signal traces so that the differential signals have matched impedances; they're short traces and we are only dealing with 10/100 Ethernet here so hopefully it won't affect things too much.

## Design files

This board was designed using the [Upverter](https://upverter.com) web service.

The schematic, board layout and bill of materials can be viewed [here](https://upverter.com/Trebuchetindustries/061c6872fd13c86f/Ethernet-tap/). Exports from Upverter are available in a subdirectory.

## TODO

* [ ] Determine how much of a problem the lack of matched impedances on differential signals is causing and fix them if necessary/possible

## Licence

Copyright © 2016, 2017 Phil Baldwin

This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.

You should have received a copy of the license along with this work. If not, see <http://creativecommons.org/licenses/by-sa/4.0/>.
