Title: Adding RV-8564-C2 break-out board
Date: 2012-10-02 12:00
Category: blog
Tags: cuffelinks, rag, RV-8564-C2
Author: Brendan M. Sleight

I need to write some software for the very, very small Real-Time-Clock chip, the RV-8564-C2. It is small (5.0 x 3.2 x 1.2mm), low-power chip with a with built-in crystal. Ideal for a cufflink, but far from ideal to wire in to a breadboard.

I knocked-up a quick break-out board and order if from http://oshpark.com/ – full [pcb in repository](https://github.com/bmsleight/cuffelink/tree/master/hardware/pcb/other/breakout_rtc).

<a href="images/Adding-RV-8564-C2-break-out-board/rtc_board.jpg"><img src="images/Adding-RV-8564-C2-break-out-board/thumbnails/480x_/rtc_board.jpg" /></a>

Now all I had to do it is solder the break-out board.

<a href="images/Adding-RV-8564-C2-break-out-board/Pre-Solder.jpg"><img src="images/Adding-RV-8564-C2-break-out-board/thumbnails/480x_/Pre-Solder.jpg" /></a>

A microscope is quite useful …

<a href="images/Adding-RV-8564-C2-break-out-board/Post-Solder.jpg"><img src="images/Adding-RV-8564-C2-break-out-board/thumbnails/480x_/Post-Solder.jpg" /></a>

Time to melt the solder paste blobs, “Honey can I borrow a frying pan ?” …

<a href="images/Adding-RV-8564-C2-break-out-board/IMG_20121002_211707.jpg"><img src="images/Adding-RV-8564-C2-break-out-board/thumbnails/480x_/IMG_20121002_211707.jpg" /></a>

And add some header pins. Although the holes in the board were too small from header pins (my error – I just used a DIP8 footprint), so I used some jumper cables. Volia:-

<a href="images/Adding-RV-8564-C2-break-out-board/IMG_20121002_213659.jpg"><img src="images/Adding-RV-8564-C2-break-out-board/thumbnails/480x_/IMG_20121002_213659.jpg" /></a>

Will test my soldering, code etc another day.  Was not happy with the cheap solder-paste – so I am on the hunt for better paste and a way to “paint” it on to the boards, without the use of a stencil. I guess at some point I will have to order solder stencil, but then I need to buy a frame to hold the boards. At the moment I will carry on “painting” the paste with the end of a wire.


