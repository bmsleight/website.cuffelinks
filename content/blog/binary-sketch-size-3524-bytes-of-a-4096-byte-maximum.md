Title: Binary sketch size: 3524 bytes (of a 4096 byte maximum)
Date: 2012-09-01 13:00
Category: blog
Tags: cuffelinks, rag
Author: Brendan M. Sleight

Right I fitted the following in to less than 4096 bytes. [https://github.com/bmsleight/cuffelink/blob/master/software/micro/arduino/tiny_rag.ino](https://github.com/bmsleight/cuffelink/blob/master/software/micro/arduino/tiny_rag.ino)

* Traffic Light Sequence, (Red, Red-Amber, Green, Amber, Red)
* Pelican Sequence, (Red, Flashing Amber, Flashing Green, Green, Amber, Red)
* Displayed Time (using Red = 1, Amber = 5, Green = 10)
* Displayed Date (using Red = 1, Amber = 5, Green = 10)
* Set Time
* Set Date

Only ~500 bytes to spare.

Alas the pin out has changed, The PCB layout will need to be changed and new PCBs from the wonderful, oshpark. (About $8 or ~£5)
