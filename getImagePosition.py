#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      js201208030313
#
# Created:     28/10/2013
# Copyright:   (c) js201208030313 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
wc = 800 #camera width
hc = 480 #camera height
wi = 112 #image width
hi = 151 #image height
offsetL = 108 #offset left
offsetR = 108 #offset right
ot = 139 #offset top
ci = 5

def getImagePosition(cameraWidth = wc,
                     cameraHeight = hc,
                     imageWidth = wi,
                     imageHeight = hi,
                     offsetLeft = offsetL,
                     offsetRight = offsetR,
                     offsetTop = ot,
                     countImage = ci):
    w = cameraWidth - (offsetLeft+offsetRight) # ????? ??? ??? ??
##    imageWidth*countImage+spaceX*(countImage-1)=w
##    spaceX = (w-imageWidth*countImage)/(countImage-1)
    spaceX = getSpace(cameraLength = cameraWidth,
                     imageLength = imageWidth,
                     offset1 = offsetLeft,
                     offset2 = offsetRight,
                     countImage = countImage)

    xPos = [offsetL+i*(imageWidth+spaceX) for i in range(countImage)]
    yPos = [offsetTop]*countImage
    position = zip(xPos,yPos)
    print position

def getSpace(cameraLength = wc,
             imageLength = wi,
             offset1 = offsetL,
             offset2 = offsetR,
             countImage = ci):
    l = cameraLength - (offset1+offset2) # ????? ??? ??? ??
    space = (l-imageLength*countImage)/(countImage-1)
    return space



if __name__ == '__main__':
    getImagePosition()
    print getSpace()
