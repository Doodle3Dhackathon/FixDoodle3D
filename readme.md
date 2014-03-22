# Fix Doodle3D routers!

Instructions:

- In the script, change the `ipaddr` ip (192.168.5.101) to a free ip on your network
- Also change `serverip` to your PCs ip.
- Start a TFTP server on your PC, with port 69, and a file "recovery.bin" which contains the latest factory.bin from http://doodle3d.com/updates/images
- Plug the FTDI cable into your PC and fix the script to point to it
- Run the script, then plug in a USB FTDI plug into the PC, and connect the broken router to ethernet, the FTDI port, and into usb (in that order prefered)
- Wait!
