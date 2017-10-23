#
# Author Hyunwook Shin
#
# this make file will build both frontend
# and backend tgz to deploy to frontend
# and backend webservers for project 1
#
frontend := frontend/bld/cmpe281p1-frontend.tgz
backend := bld/cmpe281p1.tgz

all: $(frontend) $(backend)
	echo true

$(backend):
	mkdir bld
	cp -r backend bld
	cp -r rdshandle bld
	cd bld && tar -cvzf cmpe281p1.tgz .
	cp $(backend) .

$(frontend):
	$(MAKE) -C frontend all
	cp $(frontend) .

clean:
	$(MAKE) -C backend clean
	$(MAKE) -C rdshandle clean
	$(MAKE) -C frontend clean
	rm -rf bld
	rm -rf *.tgz
