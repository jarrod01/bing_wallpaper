import os, re, urllib.request, platform
from datetime import datetime

def get_pic(country='cn'):
    bing_url = 'http://' + country +'.bing.com/'
    with urllib.request.urlopen(bing_url) as f:
        contents = f.read().decode('utf-8')
    pattern = re.compile(r'g_img={url:\s\"(.+\.jpg)\",')
    pic_url_original = pattern.findall(contents)
    if pic_url_original:
        if pic_url_original[0][:14] == '''//www.bing.com''':
            pic_url = 'http://'+ pic_url_original[0][2:]
        else:
            pic_url = bing_url + pic_url_original[0]
        print('pic_url: ' + pic_url)
    else:
        return None

    now = datetime.now().strftime('%Y-%m-%d')
    pic_name = now + '-' + os.path.split(pic_url)[1]
    # pic_name = 'picture_of_the_day.jpg'
    os_type = platform.system()
    if os_type == 'Windows':
        home = os.environ['USERPROFILE']
    else:
        home = os.environ['HOME']
    pic_path = os.path.join(home, os.path.join('Pictures', 'bing-wallpapers'))
    if not os.path.exists(os.path.join(home, 'Pictures')):
        os.mkdir(os.path.join(home, 'Pictures'))
    if not os.path.exists(pic_path):
        os.mkdir(pic_path)
    existing_pics = os.listdir(pic_path)
    for f in existing_pics:
        os.remove(os.path.join(pic_path, f))
    pic_path = os.path.join(pic_path, pic_name)

    print('pic_path: ' + pic_path)
    with urllib.request.urlopen(pic_url) as pic_data:
        with open(pic_path, 'wb') as f:
            f.write(pic_data.read())
    print('Done')
    return pic_path

if __name__ == '__main__':
    get_pic()