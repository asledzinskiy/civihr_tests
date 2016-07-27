# react_tests

To run tests:
#create virtual env
virtualenv --no-site-packages react-venv

#activate venv
. react-venv/bin/activate

#install required packages
pip install -r requirements.txt

#run tests
WORKSPACE=$(pwd)
export PYTHONPATH="${PYTHONPATH:+${PYTHONPATH}:}${WORKSPACE}"

py.test tests/test_example.py


#Additional settings

#Browser can be specified by exporting BROWSER variable (firefox by default)
export BROWSER='firefox'

#Home url can be specified by exporting URL_HOME variable (http://todomvc.com/examples/react/#/ by default)
export URL_HOME='http://todomvc.com/examples/react/#/'
