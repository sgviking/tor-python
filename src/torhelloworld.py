#!/usr/bin/env python

from stem.control import Controller

tor_password = str(open("tor_password").readline()).strip()

with Controller.from_port(port = 9051) as controller:
	controller.authenticate(tor_password)

	bytes_read = controller.get_info("traffic/read")
	bytes_written = controller.get_info("traffic/written")

	print("Tor relay has read %s bytes and written %s bytes." % (bytes_read, bytes_written))

