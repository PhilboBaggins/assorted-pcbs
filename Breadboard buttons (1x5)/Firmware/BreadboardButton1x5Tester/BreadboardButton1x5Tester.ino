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

