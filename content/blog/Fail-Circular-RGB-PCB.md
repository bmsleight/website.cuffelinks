Title: Fail - Circular RGB PCB
Date: 2015-05-04 17:00
Category: blog
Tags: cuffelinks, rgb, PCB, fail
Author: Brendan M. Sleight

**Epic fail**. My [circular PCB](./circular-rgb-pcb.html) will not work. I did the testing using 5V from the arduino nano board. Without thinking through what the cell batteries will actually deliver. Looking up the [datasheet for the TCS34725](http://www.adafruit.com/datasheets/TCS34725.pdf) I remembers that I needed at least 3V3 for the supply, also the Blue LED on the [HSMF-C114](http://www.avagotech.com/docs/AV02-2451EN) of typically 3V4. No problem - I had designed the circuit to run on 2 cell barreries, which deliver 6V.

**But** The cells delivery between 3V and 3V7. In reality I am getting above 3V with one cell, in fact enough to run the Green LED at 3V4. However if I run the ATTiny with one cell the voltage drops are such that the Green and blue LED are not lit. 

Ok two cells. 

**But** The cells delivery between 3V and 3V7. So this gives above 6V, which mean the ATTiny cuts out. 

#### Just one cell - direct to Green LED
<img src="images/Fail-Circular-RGB-PCB/Above_3V.gif" />

#### Just one cell - via ATTiny no Green
<img src="images/Fail-Circular-RGB-PCB/fail_2_voltages._..,.gif" />

#### Two cells - ATTinys cuts out
<img src="images/Fail-Circular-RGB-PCB/fail_explanation_later.gif" />

### Ok Give me Solutions
So how do I get around this problem ? 

I discounted [zener diodes](http://en.wikipedia.org/wiki/Zener_diode), current leakage too high. Also [Voltage divider](http://en.wikipedia.org/wiki/Voltage_divider) for the same reason.  There must be a small form IC .... After many minutes googling. 

[LTC3212 - RGB LED Driver and Charge Pump](http://www.linear.com/product/LTC3212)

*From the [product page](http://www.linear.com/product/LTC3212)*

 * Power and Current Control for Driving RGB LEDs
 * Individually Programmable Current Sources
 * 1x or 2x Mode, Low Noise, Constant Frequency Charge Pump
 * Single Wire Enable Control for All LEDs
 * White Mode Adjusts R, G, B Currents for White Light
 * 25mA Maximum LED Current
 * VIN Range: 2.7V to 5.5V
 * Automatic Soft-Start, Mode Switching and Output Disconnect in Shutdown Mode
 * Available in 12-Lead (3mm × 2mm) DFN Package

<a href="images/Fail-Circular-RGB-PCB/7205.png"><img src="images/Fail-Circular-RGB-PCB/thumbnails/480x_/7205.png" /></a>

I have requested some [samples](http://www.linear.com/samples/LTC3212), and whipped up another [breakout board in KiCAD](https://github.com/bmsleight/chameleon-cufflink/tree/master/pcb/breakout-test-pcb-LTC3212) order with [https://oshpark.com/](https://oshpark.com/).

<a href="images/Fail-Circular-RGB-PCB/oshpark1.png"><img src="images/Fail-Circular-RGB-PCB/thumbnails/480x_/oshpark1.png" /></a>

### Love the costs

<a href="images/Fail-Circular-RGB-PCB/oshpark2.png"><img src="images/Fail-Circular-RGB-PCB/thumbnails/480x_/oshpark2.png" /></a>

#### Final notes
[https://oshpark.com/](https://oshpark.com/) has just emailed within a few hours....
> We've sent the panel containing your boards to the fabricator. We expect to get them back around May 16th.
> In case you're interested, there are 82 other orders on the panel along with yours, adding up to a total of 450 boards. Neat eh? 

