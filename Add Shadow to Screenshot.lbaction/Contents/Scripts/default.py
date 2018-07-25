#!/usr/local/anaconda3/bin/python3
#
# LaunchBar Action Script
#
# Required Software: Pillow(Python)
# method:



from PIL import Image
from PIL import ImageFilter, ImageDraw
import imageio

def makeShadow(image_file, border, offset, shadowColour,blur_r):
    # set new image name
    point_postion = image_file.rfind(".")
    new_name = image_file[:point_postion]+"_with_shadow.png"

    # image_file: base image to give a drop shadow
    # border: border to give the image to leave space for the shadow
    # offset: offset of the shadow as [x,y]
    # shadowColour: colour of the drop shadow
    # blur_r: Gaussian blur radius
    img = imageio.imread(image_file)
    img = Image.fromarray(img)

    # Calculate the size of the shadow's image
    fullWidth  = img.size[0] + 2*border # + abs(offset[0])
    fullHeight = img.size[1] + 2*border # + abs(offset[1])
    
    # Create the shadow's image. Match the parent image's mode.
    shadow = Image.new("RGBA", (fullWidth, fullHeight), "white")
    
    # Place the shadow, with the required offset
    shadowLeft = border + max(offset[0], 0) #if <0, push the rest of the image right
    shadowTop  = border + max(offset[1], 0) #if <0, push the rest of the image down
    
    # Paste in the constant colour
    shadow.paste(shadowColour, 
                [shadowLeft, shadowTop,
                 shadowLeft + img.size[0],
                 shadowTop  + img.size[1] ])
    
    shadow = shadow.filter(ImageFilter.GaussianBlur(radius=blur_r))

    pix_shadow = shadow.load()

    with_shadow = Image.new("RGBA", (fullWidth, fullHeight))
    pix_with_shadow = with_shadow.load()
    for x in range(with_shadow.size[0]):
        for y in range(with_shadow.size[1]):
            pix_with_shadow[x,y] = (0,0,0, int((255-pix_shadow[x,y][0])))

    # Paste the original image on top of the shadow 
    imgLeft = border + offset[0]
    imgTop  = border + offset[1]
    with_shadow.paste(img, (imgLeft, imgTop))
    #pix=with_shadow.load()

    # save new image with shadow
    with_shadow.save(new_name, dpi=(144,144))

    return with_shadow

# add a mac style shadow
def main():
    import sys
    border = 112
    offset = [0, -48]
    greyvalue = 124
    sdColor = (greyvalue,greyvalue,greyvalue)
    GaussianBlurRadius = 38
    for arg in sys.argv[1:]:
        makeShadow(arg,border,offset,sdColor,GaussianBlurRadius)


if __name__== "__main__":
    main()