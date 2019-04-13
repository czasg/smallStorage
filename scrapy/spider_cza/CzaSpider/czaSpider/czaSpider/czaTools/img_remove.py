import os


def img_remove(img_path):
    os.remove(img_path)
    if not os.path.exists(img_path):
        return True
    return img_remove(img_path)

