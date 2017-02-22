# civihr_tests

To run tests:
#create virtual env
virtualenv --no-site-packages venv

#activate venv
. venv/bin/activate

#install required packages
pip install -r requirements.txt

#run tests
WORKSPACE=$(pwd)
export PYTHONPATH="${PYTHONPATH:+${PYTHONPATH}:}${WORKSPACE}"

#Necessary exports
export PASSWORD=''
export URL_HOME=''
export USERNAME=''
#You might need to download https://github.com/mozilla/geckodriver/releases
#to run tests under firefox and append path with binary to PATH
export PATH=$PATH:/home/user/Downloads/

#To run tests
py.test tests/test_role_dates.py


#Additional settings

#Browser can be specified by exporting BROWSER variable (firefox by default)
export BROWSER='firefox'
#We assume there is user without contracts, roles with id 374
#If you want to use another contact do export
export USER_ID=306