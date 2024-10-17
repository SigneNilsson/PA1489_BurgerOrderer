appname = burgerorderer
confile = $(appname).yaml

run:
	podman compose -f $(confile) up

build: 
	podman compose -f $(confile) build

overview:
	podman images
	podman ps -a

clean:
	podman compose -f $(confile) down

deepclean: clean
	podman rmi -f $(appname)
