#假设已经安装了vitralenv　并且环境中有Python2 和python3

env_path=~/.pybase_env
rm -rf $env_path
mkdir $env_path
cd $env_path
virtualenv -p /usr/bin/python2 py2env
source $env_path/py2env/bin/activate
pip install Pillow
pip install tornado
pip install mysqlclient
deactivate
virtualenv -p /usr/bin/python3 py3env
source $env_path/py3env/bin/activate
pip install Pillow
pip install tornado
#pip install mysqlclient
#3.5 现在还不支持MySQLdb
pip install PyMySQL
deactivate
