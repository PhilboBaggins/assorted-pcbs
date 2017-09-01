# TTL-232R-XX-AJ-adaptor

I seems that whenever I need a FTDI cable (USB to serial cable with a 6 pin female header) there are none to be found. We have a bag full of the TTL-232R-XX-AJ (FTDI cable with 3.5mm TRS connector) cables at the office though, left over from an old project. So what I need is an adaptor that will allow me to use the TTL-232R-XX-AJ in situations where I would normally use the FTDI cable with 6 pin female header. Of course the 6 pin cable has twice as many pins as the TTL-232R-XX-AJ cable (VCC, RTS & DTR are missing from the TTL-232R-XX-AJ) but that won't be a problem most of the time.

This PCB is such an adaptor. It connects the transmit (TX), receive (TX) and ground (GND) pins from the 3.5mm TRS connector to the corresponding pins on the 6 pin 0.1 inch female header (remaining pins on larger header left unconnected) and to a 3 pin screw terminal. There is a toggle switch in the middle that can swap over the RX and TX lines so that (if necessary) the user doesn't have to do this manually.

## Design files

This board was designed using the [Upverter](https://upverter.com) web service.

The schematic, board layout and bill of materials can be viewed [here](https://upverter.com/Trebuchetindustries/ac9f5044f0ac6c8b/TTL-232R-XX-AJ-adaptor/). Exports from Upverter are available in a subdirectory.

## Licence

Copyright © 2016 Phil Baldwin

This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.

You should have received a copy of the license along with this work. If not, see <http://creativecommons.org/licenses/by-sa/4.0/>.
