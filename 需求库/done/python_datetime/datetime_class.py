import re
import datetime

min_t = [1970, 1, 1, 0, 0, 0]
max_t = [2100, 12, 31, 23, 59, 59]


class TimeManager(object):
    _now = datetime.datetime.now()
    _timestamp = _now.timestamp()
    _time = None

    def __init__(self, _datetime=None):
        self._time = _datetime

    @classmethod
    def from_time(cls, _datetime):
        return cls(_datetime)

    @property
    def now(self):
        return self._now

    @now.setter
    def now(self, now_time):
        self._now = now_time

    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, _timestamp):
        self._timestamp = _timestamp

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, _time):
        self._time = _time

    def time2str(self, _datetime):
        return datetime.datetime.strftime(_datetime, "%Y-%m-%d %h:%m:%s")

    def _str2time(self, string=None, format=None, **kwargs):
        res = None
        args = kwargs.get('args', None)
        if args:
            res = datetime.datetime(*args)
        if not res:
            res = datetime.datetime.strptime(string, format)
        return res

    def str2time(self, string, format=None):
        if format:
            res = self._str2time(string, format)
        elif re.match('\d{8}$', string):
            res = self._str2time(string, '%Y%m%d')
        else:
            reRule = """(\d{4}|\d{2})[^\d]*(\d*)[^\d]*(\d*)[^\d]*(\d*)[^\d]*(\d*)[^\d]*(\d*)"""
            ts = re.search(reRule, string)
            res = min_t[:]
            for i in range(6):
                g = ts.group(i + 1)
                if g:
                    g = '20' + g if i == 0 and len(g) == 2 else g
                    t = int(g)
                    if t > max_t[i] or t < min_t[i]:
                        break
                    res[i] = t
            res = self._str2time(args=res)
        return res

    def add(self, _datetime, **kwargs):
        return _datetime + datetime.timedelta(**kwargs)


if __name__ == "__main__":
    print(TimeManager().str2time('2018-01-05'))
    print(TimeManager().str2time('2018-01-05:12.10.50'))
    print(TimeManager().str2time('18-01-05'))
    print(TimeManager().str2time('20190429'))
    print(TimeManager().str2time('today is 2019 and mon  4, the day 29'))
    now = datetime.datetime.now()
    print(TimeManager.from_time(now).add(now, days=1))
