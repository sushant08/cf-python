#!/bin/bash
pip install coverage
pip install Flask
cd $CF_VOLUME_PATH/cf-python
ls -l
/usr/bin/nohup coverage run app.py &
sleep 15
kill -9 `ps -ef | grep app.py | awk '{print $2}'`
coverage report app.py > allure-results
cat allure-results