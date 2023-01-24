#!/user/bin/env python3
from datetime import datetime
import time

# LED Matrix
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

# Keyboard
import board
from adafruit_neokey.neokey1x4 import NeoKey1x4

### Making a tea timer

### Make an LED screen
def create_led_device():
    # create matrix device (CS pin CE1 set in device argument)
    serial = spi(port=0, device=1, gpio=noop())
    device = max7219(serial, cascaded=4, block_orientation=90,
                     rotate=0, blocks_arranged_in_reverse_order=True)
    return device

def create_keyboard():
    # use default I2C bus
    i2c_bus = board.I2C()
    
    # Create a NeoKey object
    neokey = NeoKey1x4(i2c_bus, addr=0x30)

    return neokey

### Main
if __name__ == "__main__":
    # Setting up the display
    device = create_led_device()

    # Setting up the keyboard
    neokey = create_keyboard()

    # Opening message              
    msg = "Tea timer"
    show_message(device, msg, fill="white", font=proportional(LCD_FONT), scroll_delay=0)

    # # Testing the keys
    # # Check each button, if pressed, light up the matching neopixel!
    # while True:
    #     if neokey[0]:
    #         print("Button A")
    #         neokey.pixels[0] = 0xFF0000
    #     else:
    #         neokey.pixels[0] = 0x0
    # 
    #     if neokey[1]:
    #         print("Button B")
    #         neokey.pixels[1] = 0xFFFF00
    #     else:
    #         neokey.pixels[1] = 0x0
    # 
    #     if neokey[2]:
    #         print("Button C")
    #         neokey.pixels[2] = 0x00FF00
    #     else:
    #         neokey.pixels[2] = 0x0
    # 
    #     if neokey[3]:
    #         print("Button D")
    #         neokey.pixels[3] = 0x00FFFF
    #     else:
    #         neokey.pixels[3] = 0x0

    while True:
        if neokey[0]:
            print("Button A")
            neokey.pixels[0] = 0xFF0000
            msg = "Tea"
            show_message(device, msg, fill="white", font=proportional(LCD_FONT), scroll_delay=0)
        else:
            neokey.pixels[0] = 0x0
    
        if neokey[1]:
            print("Button B")
            neokey.pixels[1] = 0xFFFF00
        else:
            neokey.pixels[1] = 0x0
    
        if neokey[2]:
            print("Button C")
            neokey.pixels[2] = 0x00FF00
        else:
            neokey.pixels[2] = 0x0
    
        if neokey[3]:
            print("Button D")
            neokey.pixels[3] = 0x00FFFF
        else:
            neokey.pixels[3] = 0x0

        now = datetime.now()
        current_time = now.strftime("%M:%S")
        msg = current_time
#        show_message(device, msg, fill="white", font=proportional(LCD_FONT))
        with canvas(device) as draw:
            text(draw, (0,0), msg, fill = "white", font = proportional(LCD_FONT))
        #time.sleep(1 - (time.perf_counter() % 1))

