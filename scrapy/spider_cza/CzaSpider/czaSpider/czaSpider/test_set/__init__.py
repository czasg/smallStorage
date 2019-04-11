import os

currentPath = os.path.dirname(os.path.abspath(__file__))


# interface for func
def get_test_path(filename):
    setPath = _path(currentPath, filename)
    testSet = os.listdir(setPath)
    res = [_path(setPath, file) for file in testSet]
    if all([os.path.isfile(file) for file in res]):
        return res
    else:
        raise ValueError("There exist no file in set database")


def _path(*args):
    return (os.sep).join(args)


if __name__ == "__main__":
    get_test_path("img2num")
    print(_path('cza', 'is'))
