Title: Bugs in the Barograms
Date: 2013-07-11 20:19:28

Oh well... today we discovered quite an important bug in our elevation code.
In some cases the altitude AGL/GND values that you saw below the barograms
were entirely wrong and I want to apologize for that.


![Barogram Bug]({filename}/images/barogram-bug.png)


The barogram has always shown the elevation data correctly, but there was a
mixup in some calculation code that led to wrong values in the numeric display
of the altitude above ground.


The bug is fixed now and you can finally enjoy proper altitude output :)


(Please note that the barogram is currently still showing altitude above 1013
hPa since we haven't implemented QNH correction yet.)
