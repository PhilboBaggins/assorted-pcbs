/*
 * Test firmware for the Breadboard buttons (1x5) PCB
 *
 * This firmware was written for use on a Teensy LC but should work on
 * pretty much any Arduino compatible board.
 *
 * ## Wiring
 *
 * To use this firmware, the boards should be wires up as follows:
 *
 *     | Pin on button boards |   Pin on Teensy LC   |
 *     | -------------------- | -------------------- |
 *     |          1           |          1           |
 *     |          2           |          2           |
 *     |          3           |          3           |
 *     |          4           |          4           |
 *     |          5           |          5           |
 *     |          A           |         GND          |
 *     |          I           |         VCC          |
 *
 * Example wiring can be seen here: https://github.com/PhilboBaggins/assorted-pcbs/blob/master/Breadboard%20buttons%20(1x5)/board-photo.jpg
 *
 */

#include <Bounce.h>

const unsigned long DEBOUNCE_TIME = 5;

Bounce buttonObjs[] = {
    Bounce(1, DEBOUNCE_TIME),
    Bounce(2, DEBOUNCE_TIME),
    Bounce(3, DEBOUNCE_TIME),
    Bounce(4, DEBOUNCE_TIME),
    Bounce(5, DEBOUNCE_TIME),
};

void describeButtonState(int buttonIdx, const char* const currState)
{
    Serial.print("Button ");
    Serial.print(buttonIdx + 1);
    Serial.print(" reads ");
    Serial.println(currState);
}

void checkButton(int buttonIdx)
{
    buttonObjs[buttonIdx].update();

    if (buttonObjs[buttonIdx].risingEdge())
    {
        describeButtonState(buttonIdx, "high");
    }
    else if (buttonObjs[buttonIdx].fallingEdge())
    {
        describeButtonState(buttonIdx, "low");
    }
}

void setup()
{
    pinMode(1, INPUT);
    pinMode(2, INPUT);
    pinMode(3, INPUT);
    pinMode(4, INPUT);
    pinMode(5, INPUT);
}

void loop()
{
    for(int i = 0; i < 5; i++)
    {
        checkButton(i);
    }
}
