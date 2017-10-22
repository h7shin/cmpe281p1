all:
	mkdir bld
	cp -r backend bld
	cp -r rdshandle bld
	cd bld && tar -cvzf cmpe281p1.tgz .

clean:
	$(MAKE) -C backend clean
	$(MAKE) -C rdshandle clean
	rm -rf bld
