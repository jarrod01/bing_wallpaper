from appscript import *
import argparse, get_picture

def set_wallpaper():
    pic_path = get_picture.get_pic()
    se = app('System Events')
    # se.desktop_picture.set(mactypes.File(pic_path))
    desktops = se.desktops.display_name.get()
    for d in desktops:
        desk = se.desktops[its.display_name == d]
        desk.picture.set(mactypes.File(pic_path))

if __name__ == '__main__':
    set_wallpaper()