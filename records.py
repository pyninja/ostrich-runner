from collections import namedtuple

Record = namedtuple('Record', ['name', 'app', 'args'])

RECORDS = [
    Record(name='gg', app='pidgin', args=[]),
    Record(name='l', app='leafpad', args=[])
]

