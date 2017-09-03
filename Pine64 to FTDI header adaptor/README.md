# Pine64 to FTDI header adaptor

The [Pine64](https://www.pine64.org/?page_id=1194) and the [Sopine Baseboard](https://www.pine64.org/?page_id=1491) have a 3.3 volt TTL level serial port on their 10 pin EXP header. A FTDI [TTL-232R-3V3](http://www.ftdichip.com/Support/Documents/DataSheets/Cables/DS_TTL-232R_CABLES.pdf) cable could be used to connect this port to a computer but since the pin-outs (and shape of the connectors) don't match you'd need to patch the connection with 3 individual wires ... 3 wires?! That's too much work ... use this board instead.



## Design files

This board was designed using the [Upverter](https://upverter.com) web service.

The schematic and board layout can be viewed [here](https://upverter.com/Trebuchetindustries/1f7428c9e47603ca/Pine64-to-FTDI-header-adaptor/). Exports from Upverter are available in a subdirectory.

### Bill of materials

| Designator | Description                                    | Part                                                   |
| ---------- | ---------------------------------------------- | ------------------------------------------------------ |
| J1         | Header for mating with Pine64 EXP header       | Generic 2x5 pin female header - 0.1" pitch             |
| J2         | Header for mating with FTDI serial port header | Generic 1x6 pin male header - 0.1" pitch - right angle |



## Licence

Copyright © 2017 Phil Baldwin

This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.

You should have received a copy of the license along with this work. If not, see <http://creativecommons.org/licenses/by-sa/4.0/>.
