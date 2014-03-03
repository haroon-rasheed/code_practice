#! /usr/bin/python

from progressbar import *

widgets = ['Test: ', Percentage(), ' ', Bar(marker=RotatingMarker()), ' ', ETA(), ' ', FileTransferSpeed()]
pbar = ProgressBar(widgets=widgets)

def dlProgress(count, blockSize, totalSize):
	if pbar.maxval is None:
		pbar.maxval = totalSize
		pbar.start()

pbar.update(min(count*blockSize, totalSize))

urllib.urlretrieve(url, fileName, reporthook=dlProgress)
pbar.finish()
