import time
import thumby
import math
from random import randint

restartBmp = bytearray([240,12,2,2,1,1,1,1,1,2,2,12,240,0,1,6,8,8,16,16,16,0,0,14,12,10,1,0])
restartSprite = thumby.Sprite(14,14,restartBmp)
thumby.display.setFPS(10)
thumby.display.fill(0) # Fill canvas to black
restartSprite.x = 72-14
restartSprite.y = 9
thumby.display.drawText("A",72-10,0,1)
thumby.display.drawSprite(restartSprite)
thumby.display.update()
arr = list(range(1,41))
def shuffle(seq):
    for _ in range(200):
        i,j = randint(0,len(seq)-1),randint(0,len(seq)-1)
        seq[i],seq[j] = seq[j],seq[i]
sortingOps = []
def quicksort(i=0,j=39):
    if j-i < 2:return
    mid = (i+j)//2
    partition = arr[mid]
    l = i
    r = j
    while l < r:
        while arr[l] < partition:
            l += 1
        while arr[r] > partition:
            r -= 1
        if l < r:
            swap(l,r)
    quicksort(i,l)
    quicksort(l+1,j)

def swap(i,j):
    arr[i],arr[j] = arr[j],arr[i]
    sortingOps.append((i,j))
count = 0
sortingOps = []
shuffle(arr)
duplicate = arr[:]
for i,val in enumerate(arr):
    thumby.display.drawLine(16+i,40-val,16+i,39,1)
thumby.display.update()
quicksort()
while(1):
    t0 = time.ticks_ms()   # Get time (ms)
    if count < len(sortingOps):
        i,j = sortingOps[count]
        if j != i:
            duplicate[i],duplicate[j] = duplicate[j],duplicate[i]
            thumby.display.drawLine(16+i,0,16+i,39,0)
            thumby.display.drawLine(16+i,40-duplicate[i],16+i,39,1)
            thumby.display.drawLine(16+j,0,16+j,39,0)
            thumby.display.drawLine(16+j,40-duplicate[j],16+j,39,1)
        count += 1
    thumby.display.update()
