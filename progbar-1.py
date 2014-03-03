#! /usr/bin/python

from progressbar import *               # just a simple progress bar
import time
widgets = ['Something: ', Percentage(), ' ', Bar(marker=RotatingMarker()),
           ' ', ETA(), ' ', FileTransferSpeed()]
pbar = ProgressBar(widgets=widgets, maxval=10000000).start()
for i in range(1000000):
# do something
	pbar.update(10*i+1)
	time.sleep(0.1)
	pbar.finish()
