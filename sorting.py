import time
import thumby
import math
from random import randint

restartBmp = bytearray([240,12,2,2,1,1,1,1,1,2,2,12,240,0,1,6,8,8,16,16,16,0,0,14,12,10,1,0])
restartSprite = thumby.Sprite(14,14,restartBmp)
returnBmp = bytearray([0,4,14,21,4,4,4,4,4,4,4,8,8,240,0,0,0,0,2,2,2,2,2,2,2,1,1,0])
returnSprite = thumby.Sprite(14,14,returnBmp)
restartSprite.x = 72-14
restartSprite.y = 9
returnSprite.x = 0
returnSprite.y = 9
def drawSorting():
    thumby.display.fill(0) # Fill canvas to black
    thumby.display.drawText("A",72-10,0,1)
    thumby.display.drawText("B",4,0,1)
    thumby.display.drawSprite(restartSprite)
    thumby.display.drawSprite(returnSprite)
arr = list(range(1,41))
def shuffle(seq):
    for _ in range(200):
        i,j = randint(0,len(seq)-1),randint(0,len(seq)-1)
        seq[i],seq[j] = seq[j],seq[i]
sortingOps = []
thumby.display.setFPS(20)
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

def heapify(n, i):
  largest = i
  left = i*2 + 1
  right = i*2 + 2
  if left < n and arr[left] > arr[largest]:
    largest = left
  if right < n and arr[right] > arr[largest]:
    largest = right
  if largest != i:
    swap(i, largest)
    heapify(n, largest)
def heapSort():
  for i in range(40<<1 - 1,-1,-1):
    heapify(40, i)
  for i in range(39,0,-1):
    swap(0, i)
    heapify(i, 0)
  return arr

def bubbleSort():
  sorts = 1
  while sorts > 0:
    sorts = 0
    for i in range(1,40):
      if (arr[i] < arr[i-1]):
        swap(i,i-1)
        sorts += 1

def combSort():
  length = 40
  shrink = 1.3
  gap = length
  sorted = False
  while not sorted:
    gap = int(gap/shrink)
    if gap <= 1:
      sorted = True
      gap = 1
    for i in range(40-gap):
        sm = gap + i
        if arr[i] > arr[sm]:
            swap(i,sm)
            sorted = False

def swap(i,j):
    arr[i],arr[j] = arr[j],arr[i]
    sortingOps.append((i,j))
count = 0
sortingOps = []
sorts = {
    "Quicksort":quicksort,
    "Heapsort":heapSort,
    "Bubble Sort":bubbleSort,
    "Comb Sort":combSort,
}
options = ["Quicksort","Heapsort","Bubble Sort","Comb Sort"]
FPSs = [10,15,30,10]
def drawMenu():
    thumby.display.fill(0) # Fill canvas to black
    for i in range(len(options)):
        thumby.display.drawText((">" if selected == i else " ") + options[i],0,i*8,1)
state = "menu"
selected = 0
drawMenu()
while(1):
    t0 = time.ticks_ms()   # Get time (ms)
    if state == "sorting":
        if count < len(sortingOps):
            i,j = sortingOps[count]
            while i == j and count < len(sortingOps):
                count += 1
                i,j = sortingOps[count]
            if j != i:
                duplicate[i],duplicate[j] = duplicate[j],duplicate[i]
                thumby.display.drawLine(16+i,0,16+i,39,0)
                thumby.display.drawLine(16+i,40-duplicate[i],16+i,39,1)
                thumby.display.drawLine(16+j,0,16+j,39,0)
                thumby.display.drawLine(16+j,40-duplicate[j],16+j,39,1)
            count += 1
        if thumby.buttonB.pressed() or thumby.buttonA.pressed():
            state = "menu"
            thumby.display.setFPS(20)
            drawMenu()
    if state == "menu":
        if thumby.buttonU.pressed():
            selected = max(0,selected-1)
            drawMenu()
        elif thumby.buttonD.pressed():
            selected = min(len(options)-1,selected+1)
            drawMenu()
        elif thumby.buttonA.pressed():
            state = "sorting"
            drawSorting()
            shuffle(arr)
            sortingOps = []
            duplicate = arr[:]
            count = 0
            for i,val in enumerate(arr):
                thumby.display.drawLine(16+i,40-val,16+i,39,1)
            thumby.display.setFPS(FPSs[selected])
            sorts[options[selected]]()
    thumby.display.update()
