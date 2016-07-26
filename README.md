# react_tests

To run tests:
#create virtual env
virtualenv --no-site-packages react-venv

#activate venv
. react-venv/bin/activate

#install required packages
pip install -r requirements.txt

#run tests
py.test tests/test_example.py 
