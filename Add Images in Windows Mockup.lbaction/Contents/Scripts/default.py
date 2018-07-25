#!/usr/local/anaconda3/bin/python3
#
# LaunchBar Action Script
#
# Required Software: Pillow(Python)

from PIL import Image, ImageDraw, ImageFont
import imageio
import sys

def makeWindow(image_file):
    # set new image name
    point_postion = image_file.rfind(".")
    new_name = image_file[:point_postion]+"_Windows.png"

    img = imageio.imread(image_file)
    img = Image.fromarray(img)

    window_mockup = imageio.imread("windowsSE.png")
    window_mockup = Image.fromarray(window_mockup)

    ## all the parameters
    lt = (0,0,502,156)
    rt = (1213,0,1360,156)
    lb = (0,992,502,1044)
    rb = (1213,992,1360,1044)
    t  = (503,0,504,156)
    b  = (503,992,515,1044)
    l  = (0,157,12,158)
    r  = (1348,157,1364,158)
    tt = (195,8,1247,44)
    border_l = 12
    border_r = 1360-1348

    left_top     = window_mockup.crop(lt)
    right_top    = window_mockup.crop(rt)
    left_buttom  = window_mockup.crop(lb)
    right_buttom = window_mockup.crop(rb)
    top          = window_mockup.crop(t )
    buttom       = window_mockup.crop(b )
    left         = window_mockup.crop(l )
    right        = window_mockup.crop(r )
    title_color  = window_mockup.crop(tt)

    fullWidth  = img.width + border_l + border_r
    fullHeight = img.height + (top.height) + (buttom.height)
    
    # # Create the shadow's image. Match the parent image's mode.
    new_window = Image.new("RGBA", (fullWidth, fullHeight), "white")

    new_window.paste(left_top,(0,0))
    new_window.paste(right_top,(fullWidth-right_top.width ,0))
    new_window.paste(left_buttom,(0,img.height+left_top.height))
    new_window.paste(right_buttom,(fullWidth-right_buttom.width,img.height+left_top.height))


    for x in range(fullWidth-left_top.width-right_top.width):
        new_window.paste(top, (left_top.width+x,0) )
        new_window.paste(buttom, (left_buttom.width+x,left_top.height+img.height))

    for y in range(img.size[1]):
        new_window.paste(left, (0,left_top.height+y) )
        new_window.paste(right, (left.width+img.width,left_top.height+y) )

    new_window.paste( title_color.resize(( fullWidth-195-(window_mockup.width -1244) , 44-8)), (195,8)) 
    new_window.paste(img,(left.width,left_top.height))


    #d = ImageDraw.Draw(new_window)
    #d.rectangle([160,110,290,136],fill="white")
    ## get a font
    #fnt = ImageFont.truetype('Microsoft Sans Serif', size=10)
    ## get a drawing context
    #txt = Image.new('RGBA', (500,15))
    #t = ImageDraw.Draw(txt)
    #t.text((0,0), image_file[:point_postion],font=fnt, fill=(0,0,0,255))
    #new_window.paste(txt.resize((round(txt.width*2.2),round(txt.height*2.2)),Image.ANTIALIAS),(158,108))

    new_window.save(new_name,dpi=(144,144))


if __name__== "__main__":
    for arg in sys.argv[1:]:
        makeWindow(arg)