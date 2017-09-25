# ATX to Eurorack power supply adaptor

An ATX power supply (standard PC power supply) has all the power rails we want for a Eurorack module synth and they're cheap and easy to obtain (even salvagable from an old computer). This board accepts the 24 pin connector from the ATX power supply and distributes it's +12V, -12V, +5V power rails to the following connectors:

* 2 standard Eurorack power connectors - 2x8 pins
* 1 4-pin screw terminal block or 4 Quick Fit lugs

The CV and Gate signals on the Eurorack power connectors have been left unconnected.

## Potential issues with using an ATX power supply with a Eurorack system

ATX power supplies are designed to operate within desktop computers, not within Eurorack modular synths so there are likely to be a few issues, e.g.:

* An ATX power supply will probably be a bit more noisy
* Some ATX power supplies require a minimum load before the turn on ([see here](http://reprap.org/wiki/PC_Power_Supply#Base_Load) for more infomation)
* ATX power supplies have a PWR_OK signal to indicate when the power supply is working correctly. Since this board doesn't check the signal and just passes the power rails through regardless of the state of the PWR_OK signal; it's possible that this board will supply "bad power" to the Eurorack system
* All the other things I haven't thought of yet

## Design files

This board was designed using the [Upverter](https://upverter.com) web service.

The schematic, board layout and bill of materials can be viewed [here](https://upverter.com/Trebuchetindustries/cbf2f2e6c2a22832/ATX-to-Eurorack-power-supply-adaptor/). Exports from Upverter are available in a subdirectory.

## TODO

* [ ] Determine what value resistors to use for LEDs
* [ ] Consider using the PWR_OK signal

## Licence

Copyright © 2017 Phil Baldwin

This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.

You should have received a copy of the license along with this work. If not, see <http://creativecommons.org/licenses/by-sa/4.0/>.
