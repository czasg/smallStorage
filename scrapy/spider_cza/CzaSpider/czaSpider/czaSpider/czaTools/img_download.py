import os
import time
import requests


def img_download(img_url):
    project_path = os.path.dirname(os.path.dirname(__file__))
    file_name = os.path.basename(img_url)
    img_path = (os.sep).join((project_path, "dump", file_name))
    with open(img_path, 'wb') as img:
        img.write(requests.get(img_url).content)
    return img_path

if __name__ == "__main__":
    img = "http://static8.ziroom.com/phoenix/pc/images/price" \
          "/e72ac241b410eac63a652dc1349521fds.png"
    img = img_download(img)
    print(img)

    from czaSpider.czaTools.img_remove import img_remove
    print(img_remove(img))
    import shutil
    # os.remove(img)