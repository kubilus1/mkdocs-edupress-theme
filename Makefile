pkg:
	python3 setup.py sdist bdist_wheel

build:
	python3 setup.py build

build_img:
	docker build -t mkdocst .

publish_doc: build_img
	docker run -e SSH_USER=$$SSH_USER -e SSH_AUTH_SOCK=$$SSH_AUTH_SOCK -it --rm -v $$SSH_AUTH_SOCK:$$SSH_AUTH_SOCK -v `pwd`:/docs mkdocst /bin/bash -c "mkdocs gh-deploy"

serve: build_img
	docker run -p 8000:8000 -it --rm -v `pwd`:/docs mkdocst /bin/bash -c "mkdocs -v serve -a 0.0.0.0:8000"

build_doc: build_img
	docker run -i --rm -v `pwd`:/docs mkdocst /bin/bash -c "mkdocs build"

clean:
	- rm -rf build
	- rm -rf dist

push: pkg
	twine upload dist/*
