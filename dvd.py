import time
import thumby
import math

# BITMAP: width: 32, height: 32
bitmap0 = bytearray([0,0,0,0,0,0,0,0,248,8,232,40,40,40,40,40,40,40,40,40,40,232,8,248,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,0,0,255,0,63,32,32,32,32,32,32,32,32,32,32,63,0,255,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,0,0,255,0,12,12,63,63,12,12,0,0,24,24,3,3,0,255,0,0,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,31,16,16,16,16,20,18,16,20,18,16,16,16,16,16,31,0,0,0,0,0,0,0,0])

# Make a sprite object using bytearray (a path to binary file from 'IMPORT SPRITE' is also valid)
thumbySprite = thumby.Sprite(32, 32, bitmap0)

# Set the FPS (without this call, the default fps is 30)
thumby.display.setFPS(60)
x = 0 #-8 to 48 are safe
y = 0 # -3 to 11 are safe
vx = 1
vy = -1
while(1):
    t0 = time.ticks_ms()   # Get time (ms)
    thumby.display.fill(0) # Fill canvas to black
    thumbySprite.x = int(round(x))
    thumbySprite.y = int(round(y))
    x += vx*0.2
    y += vy*0.15
    if x < -8:
        x = -7
        vx = 1
    elif x > 48:
        x = 47
        vx = -1
    if y < -3:
        y = -2
        vy = 1
    elif y > 11:
        y = 10
        vy = -1
    # Display the bitmap using bitmap data, position, and bitmap dimensions
    thumby.display.drawSprite(thumbySprite)
    thumby.display.drawText(f"{x:.0f},{y:.0f}",0,0,1)
    thumby.display.update()
