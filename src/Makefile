SHELL := /bin/bash
init:
	cp ./util/sample.json ./util/config.json
	cp ./myselenium/sample_test_case.py ./myselenium/test_case.py

download_latest_chromedriver:
	sudo apt-get install unzip
	rm -r ./util/chromedriver/
	mkdir ./util/chromedriver/
	wget -O ./util/chromedriver/LATEST_RELEASE http://chromedriver.storage.googleapis.com/LATEST_RELEASE
	a=$$(uname -m) ;  \
	if [ $$a == i686 ]; then b=32; elif [ $$a == x86_64 ]; then b=64; fi; \
	latest=$$(cat ./util/chromedriver/LATEST_RELEASE); \
	echo $$b; \
	wget -O ./util/chromedriver/chromedriver.zip 'http://chromedriver.storage.googleapis.com/'$$latest'/chromedriver_linux'$$b'.zip'
	sudo unzip ./util/chromedriver/chromedriver.zip chromedriver -d /usr/local/bin/
	echo 'success?'
	