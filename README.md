This word list is demo of Trae CN auto built project.

## Run
```bash
# run only once
pip install -r requirements.txt
# run
python app.py
# or run with flask
flask run
# or run with gunicorn
gunicorn -w=1 -b=:8080 app:app
```
Open http://127.0.0.1:5000/ with browser

## Test
```bash
python -m pytest tests/test_app.py
```
