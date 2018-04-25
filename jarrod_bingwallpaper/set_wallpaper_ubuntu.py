import os
import time
import get_picture

def set_wallpaper():
    img_path = get_picture.get_pic()
    bashCom = 'gsettings set org.gnome.desktop.background picture-uri file://' + img_path
    os.popen(bashCom)

if __name__ == '__main__':
    set_wallpaper()