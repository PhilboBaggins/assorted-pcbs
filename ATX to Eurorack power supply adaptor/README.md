# ATX to Eurorack power supply adaptor

*Warning: Design not finished yet.*

An ATX power supply (standard PC power supply) has all the power rails we want for a Eurorack modular synth; plus they're cheap and easy to obtain (even salvageable from an old computer). This board accepts the 24 pin connector from the ATX power supply and distributes it's +12V, -12V, +5V power rails to the following connectors:

* 2 standard Eurorack power connectors - 2x8 pin shrouded header
* 1 4-pin screw terminal block or 4 Quick Fit lugs (see "Secondary connectors" section below)

The CV and Gate signals on the Eurorack power connectors have been left unconnected.

![Board photo](./board-photo.jpg)

## Potential issues with using an ATX power supply with a Eurorack system

ATX power supplies are designed to operate within desktop computers, not within Eurorack modular synths so there are likely to be a few issues, e.g.:

* An ATX power supply will probably be a bit more noisy than the usual Eurorack power supplies
* Some ATX power supplies require a minimum load before the turn on ([see here](http://reprap.org/wiki/PC_Power_Supply#Base_Load) for more information)
* ATX power supplies have a PWR_OK signal to indicate when the power supply is working correctly. Since this board doesn't check the signal and just passes the power rails through regardless of the state of the PWR_OK signal; it's possible that this board will supply "bad power" to the Eurorack system
* All the other things I haven't thought of yet

## Secondary connectors

This board has two sets of connectors with overlapping footprints. You an only load one of them on a board ... just two different ways to get to the same power rails:

| Screw terminals | Quick Fit lugs |
| --------------- | -------------- |
| ![Secondary connector - Screw terminals](./secondary-connector-screw-terminals.jpg) | ![Secondary connector - Lugs](./secondary-connector-lugs.jpg) |

## LEDs

The 3 LEDs indicate the presence of the 3 powers rails (+12V, -12V, +5V). They don't indicate that the power supply is behaving itself or that the power rail has the right voltage. LED brightness is controlled by the resistor next to each LED, recommended values:

* +12 volt rail: 5k ohms
* -12 volt rail: 5k ohms
*  +5 volt rail: 1.5k ohms

These resistances were calculated using the [design-calcs.ipynb](./design-calcs.ipynb) Jupyter Notebook ([online viewer](https://mybinder.org/v2/gh/PhilboBaggins/assorted-pcbs/master?filepath=ATX%20to%20Eurorack%20power%20supply%20adaptor%2Fdesign-calcs.ipynb)).

## Design files

This board was designed using the [Upverter](https://upverter.com) web service.

The schematic, board layout and bill of materials can be viewed [here](https://upverter.com/Trebuchetindustries/cbf2f2e6c2a22832/ATX-to-Eurorack-power-supply-adaptor/). Exports from Upverter are [available in a subdirectory](./Upverter%20exports).

## Ordering PCB

[This PCB can be ordered](https://PCBs.io/share/4QGV1) from the [pcbs.io](https://pcbs.io) service.

<a href="https://PCBs.io/share/4QGV1"><img src="https://s3.amazonaws.com/pcbs.io/share.png" alt="Order from PCBs.io"></img></a>

## TODO

* [ ] Consider using the PWR_OK signal

## Licence

Copyright © 2017, 2018 Phil Baldwin

This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.

You should have received a copy of the license along with this work. If not, see <http://creativecommons.org/licenses/by-sa/4.0/>.
