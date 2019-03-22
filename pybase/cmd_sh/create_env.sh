#!/bin/bash
#####################################
## File name : create_env.sh
## Create date : 2018-11-25 15:54
## Modified date : 2019-03-22 12:50
## Author : DARREN
## Describe : not set
## Email : lzygzh@126.com
####################################

realpath=$(readlink -f "$0")
export basedir=$(dirname "$realpath")
export filename=$(basename "$realpath")
export PATH=$PATH:$basedir/dlbase
export PATH=$PATH:$basedir/dlproc
#base sh file
. dlbase.sh
#function sh file
. etc.sh
#asumming installed virtualenv　

rm -rf $env_path
mkdir $env_path
cd $env_path

virtualenv -p /usr/bin/python2 py2env
source $env_path/py2env/bin/activate
pip install Pillow
pip install tornado
pip install mysqlclient
pip install requests
pip install tqdm
deactivate
virtualenv -p /usr/bin/python3 py3env
source $env_path/py3env/bin/activate
pip install Pillow
pip install tornado
#pip install mysqlclient
#3.5 现在还不支持MySQLdb
pip install PyMySQL
pip install requests
pip install tqdm
deactivate
