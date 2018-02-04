# Breadboard power injector - Inverting

<img align="right" src="../_common/PlaceholderImage.png">

A simple way to get power and ground connected to the vertical rails on your breadboard. This board also contains a [charge pump](https://en.wikipedia.org/wiki/Charge_pump) to invert the voltage of the supplied VCC, i.e. if you connect +5 volts and ground to the screw terminal then you'll get +5 volt on the pins labeled VCC and -5 volts on the pins labeld VEE.

The charge pump will not supply very much current; it's really just intended to provide a negative voltage reference for op-amps and other low power situations like that.

## Related boards

This board is based on the [Breadboard power injector](../Breadboard%20power%20injector/).

## Design files

This board was designed using the [Upverter](https://upverter.com) web service.

The schematic, board layout and bill of materials can be viewed [here](https://upverter.com/Trebuchetindustries/6bba28dd442039e4/Breadboard-power-injector---Inverting/). Exports from Upverter are [available in a subdirectory](./Upverter%20exports).

The bill of materials lists specific a part number for the 2 pin screw terminal block but really any old 2 pin screw terminal block with a 5mm pitch should work.

The bill of materials lists LMC9660 but really any of the (surface mount) 7660 chips should work.

## Licence

Copyright © 2017 Phil Baldwin

This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.

You should have received a copy of the license along with this work. If not, see <http://creativecommons.org/licenses/by-sa/4.0/>.
