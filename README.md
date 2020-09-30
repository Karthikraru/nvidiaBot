# nvidiaBot
An nvidia autocheckout/autofill bot that guides you to checkout in under 5 seconds!

This repository has two programs. 

One is autofill.py where the user has to refresh the tab themselves and after clicking 'add to cart' the bot will use guest checkout and autofill all of the information in info.py
The user will then need to click continue, verify their information, and then click purchase.

The other program is nvidia.py where the bot will automatically refresh the tab based on a given interval. The bot will stop refreshing after a button to add to cart appears.
After the user clicks 'add to cart', the bot will use guest checkout and autofill all of the information in info.py.
The user will then need to click continue, verify their information, and then click purchase.
