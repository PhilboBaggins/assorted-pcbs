# Tiny USB dual rail power supply

<img align="right" src="../_common/PlaceholderImage.png">

A little dual rail (±12 volt) power supply board powered from USB.

## Design files

This board was designed using the [Upverter](https://upverter.com) web service.

The schematic, board layout and bill of materials can be viewed [here](https://upverter.com/Trebuchetindustries/384d040aadc70df0/Tiny-USB-dual-rail-power-supply/). Exports from Upverter are [available in a subdirectory](./Upverter%20exports).

## Isolation

This board uses two isolated DC to DC converters to create a split rail (positive and negative voltage) output. This means that the ±12 volt output is isolated from the input.

It would also be possible to isolate the output "ground" from the input/USB ground (although you probably shouldn't call it ground then, "common" would be a better name). I chose not to isolate the ground on this board (USB ground is connected to the output of the DC/DC converters and to the output screw terminal), but if you did want to change this board to provide that isolation, then it would be easy to do by:

* Changing the GND on the output side of the DC/DC converters to common on the schematic
* Changing the GND on the output connector to common on the schematic
* Shrinking to copper pours on the screw terminal side of the PCB so that they no longer makes contact with the copper pours on the USB side of the PCB. Note that there are copper pours on the top and bottom of the board.

## Licence

Copyright © 2018, 2019 Phil Baldwin

This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.

You should have received a copy of the license along with this work. If not, see <http://creativecommons.org/licenses/by-sa/4.0/>.
