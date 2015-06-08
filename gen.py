import Image
import os
from datetime import datetime
from datetime import timedelta


def add_commits(date, n=1):
    for i in xrange(n):
        os.system('git commit -m ! --allow-empty --date="%s"' % date)


def process(im):
    assert(isinstance(im, Image.Image))
    im = im.convert('1')
    xsize, ysize = im.size
    date = datetime.now() - timedelta(xsize * ysize)
    step = timedelta(1)

    for x in xrange(xsize):
        for y in xrange(ysize):
            pixel = im.getpixel((x, y))

            if pixel == 0:
                add_commits(date.isoformat(), n=20)

            date += step


if __name__ == '__main__':
    im = Image.open('hello.png')
    process(im)
