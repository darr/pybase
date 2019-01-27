env_path=~/.pybase_env
bash check_code.sh

source $env_path/py2env/bin/activate
pip freeze > python2_requiements.txt
python pytest.py
deactivate

source $env_path/py3env/bin/activate
pip freeze > python3_requiements.txt
python pytest.py
deactivate
python pyclean.py
