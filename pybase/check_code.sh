env_path=~/.pybase_env
source $env_path/py2env/bin/activate

pylint --rcfile=pylint.conf pydec_encry.py
pylint --rcfile=pylint.conf pyhttp.py
pylint --rcfile=pylint.conf pymodule.py
pylint --rcfile=pylint.conf pyprocess.py
pylint --rcfile=pylint.conf pysig.py
pylint --rcfile=pylint.conf pythread.py
pylint --rcfile=pylint.conf etc.py
pylint --rcfile=pylint.conf pycount.py
pylint --rcfile=pylint.conf pyimg.py
pylint --rcfile=pylint.conf pylinux.py
pylint --rcfile=pylint.conf pymysqldb.py
pylint --rcfile=pylint.conf pyproxy.py
pylint --rcfile=pylint.conf pysqlite.py
pylint --rcfile=pylint.conf pytime.py
pylint --rcfile=pylint.conf pydbbase.py
pylint --rcfile=pylint.conf pyfile.py
pylint --rcfile=pylint.conf pyjson_data.py
pylint --rcfile=pylint.conf pylog.py
pylint --rcfile=pylint.conf pyobject.py
pylint --rcfile=pylint.conf pyre.py
pylint --rcfile=pylint.conf pysql.py
pylint --rcfile=pylint.conf pyurl.py
pylint --rcfile=pylint.conf pybaselog.py
pylint --rcfile=pylint.conf pydb.py
pylint --rcfile=pylint.conf pyglobal.py
pylint --rcfile=pylint.conf pyjson.py
pylint --rcfile=pylint.conf pylog_table.py
pylint --rcfile=pylint.conf pypickle.py
pylint --rcfile=pylint.conf pyserver.py
pylint --rcfile=pylint.conf pytest.py


#   pylint --rcfile=pylint.conf pylog.py
#   pylint --rcfile=pylint.conf pylinux.py
#   pylint --rcfile=pylint.conf pyobject.py
#   pylint --rcfile=pylint.conf pymodule.py
#   pylint --rcfile=pylint.conf pypickle.py
#   pylint --rcfile=pylint.conf pyhttp.py
#   pylint --rcfile=pylint.conf pyprogress.py
#   pylint --rcfile=pylint.conf pyre.py
#   pylint --rcfile=pylint.conf pysql.py
#   pylint --rcfile=pylint.conf pytime.py
#   pylint --rcfile=pylint.conf pydbbase.py
#   pylint --rcfile=pylint.conf pydb.py
#   pylint --rcfile=pylint.conf pysqlite.py
#   pylint --rcfile=pylint.conf pymysqldb.py
#   pylint --rcfile=pylint.conf pylog_table.py
#   pylint --rcfile=pylint.conf pyserver.py
deactivate

source $env_path/py3env/bin/activate
#   pylint --rcfile=pylint.conf pylog.py
#   pylint --rcfile=pylint.conf pylinux.py
#   pylint --rcfile=pylint.conf pyobject.py
#   pylint --rcfile=pylint.conf pymodule.py
#   pylint --rcfile=pylint.conf pypickle.py
#   pylint --rcfile=pylint.conf pyhttp.py
#   pylint --rcfile=pylint.conf pyprogress.py
#   pylint --rcfile=pylint.conf pyre.py
#   pylint --rcfile=pylint.conf pysql.py
#   pylint --rcfile=pylint.conf pytime.py
#   pylint --rcfile=pylint.conf pydbbase.py
#   pylint --rcfile=pylint.conf pydb.py
#   pylint --rcfile=pylint.conf pysqlite.py
#   pylint --rcfile=pylint.conf pymysqldb.py
#   pylint --rcfile=pylint.conf pylog_table.py
#   pylint --rcfile=pylint.conf pyserver.py
deactivate
