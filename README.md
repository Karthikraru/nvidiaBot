# nvidiaBot
An nvidia autocheckout/autofill bot that guides you to checkout in under 5 seconds!

You may need to replace the existing chromedriver with a different version depending on your computer. To do this first go to chrome://settings/help in your chrome browser and find what version of chrome you have. Then go to https://chromedriver.chromium.org/ and download the appropriate version. Place it in the folder with the name 'chromedriver' and delete the exsting one.


This repository has two programs. 

One is autofill.py where the user has to refresh the tab themselves and after clicking 'add to cart' the bot will use guest checkout and autofill all of the information in info.py
The user will then need to click continue, verify their information, and then click purchase.

The other program is nvidia.py where the bot will automatically refresh the tab based on a given interval. The bot will stop refreshing after a button to add to cart appears.
After the user clicks 'add to cart', the bot will use guest checkout and autofill all of the information in info.py.
The user will then need to click continue, verify their information, and then click purchase.

IMPORTANT: nvidia.py requires the product-specific url. This means that the url for the site with several other products will not work.
Sample URL for the Geforce RTX 3070: https://www.nvidia.com/en-us/geforce/graphics-cards/30-series/rtx-3070/

NOTE: The automatic refreshing requires me to customize it per release. I will try my best to update it but if the release noted below is not the product you would like, use autofill.py

nvidia.py currently refreshes for the Geforce RTX 3070 founders edition.


