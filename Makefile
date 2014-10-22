all: clean build

build: make-folders virtual-env clone-repos final-build

make-folders: 
	mkdir dependencies
	mkdir server


virtual-env: 
	./scripts/create-venv

clone-repos: 
	./scripts/clone-repos

clean:
	rm -rf dependencies py server