class reRuler(object):
    def __init__(self, ruler=None):
        import re
        self.handle = re.compile(ruler) if ruler else None

