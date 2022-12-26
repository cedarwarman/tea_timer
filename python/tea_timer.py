#!/user/bin/env python3
import time

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

### Making a tea timer

### Make an LED screen
def create_led_device():
    # create matrix device (CS pin CE1 set in device argument)
    serial = spi(port=0, device=1, gpio=noop())
    device = max7219(serial, cascaded=4, block_orientation=90,
                     rotate=0, blocks_arranged_in_reverse_order=True)
    return(device)


### Main
if __name__ == "__main__":
    # Setting up the displayj
    device = create_led_device()

    # Opening message              
    msg = "Merry Christmas"

    while True:
        show_message(device, msg, fill="white", font=proportional(LCD_FONT), scroll_delay=0.05)

