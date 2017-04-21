import urllib

a = urllib.urlopen("https://en.wikipedia.org/wiki/Flat_Earth")

for i in a:
	if "Chinese astronomy" in a.readline():
		print i