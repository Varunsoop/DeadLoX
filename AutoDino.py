import pyautogui
import time
from PIL import Image, ImageGrab
def hit(key):
    pyautogui.keyDown(key)
    return
def isCollide(data):
    # It draws the rectangle for cactus
    for i in range( 250, 420):
        for j in range( 610, 700):
            if data[i,j]>100:
                hit("up")
                return  
            
 
    # # Draw the rectangle for the birds
    # for i in range( 250, 420):
    #     for j in range( 530, 595):
    #         if data[i,j]>200:
    #             hit("down")
    #             return
if __name__=="__main__":
    print("Hey! This Dino game is about to start....")
    time.sleep(2)
    hit("up")
    while True:
        image=ImageGrab.grab().convert('L')
        data=image.load()
        isCollide(data)
# # DRAW
#     image=ImageGrab.grab().convert('L')
#     data=image.load()
#     # It draws the rectangle for cactus
#     for i in range( 250, 420):
#         for j in range( 610, 700):
#                 data[i,j]=0
    
#     # Draw the rectangle for the birds
#     for i in range( 250, 420):
#         for j in range( 530, 595):
#                 data[i,j]=0      
#     image.show()
 
