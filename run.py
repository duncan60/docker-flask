#!flask/bin/python
from app.main import app
app.run(host='0.0.0.0', port=5000, debug=True)