import os


def get_current_path(__file__):
    return os.path.dirname(os.path.abspath(__file__))


def to_path(*args):
    return (os.sep).join(args)

def get_database_path():
    return (os.sep).join((get_current_path(), "database"))

if __name__ == "__main__":
    print(get_current_path(__file__))
    print(to_path("","is","sg"))