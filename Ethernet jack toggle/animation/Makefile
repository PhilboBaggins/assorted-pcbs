
all: animation.gif

animation.gif: left.gif right.gif
	gifsicle --delay=100 left.gif right.gif --loopcount  -o animation.gif

left.gif: left.png
	convert left.png left.gif

right.gif: right.png
	convert right.png right.gif

clean:
	rm -f left.gif
	rm -f right.gif
	rm -f animation.gif
