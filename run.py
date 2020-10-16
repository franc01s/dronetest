import os

from dotenv import load_dotenv
from flask import Flask
from yaml import safe_load
import logging, sys

app = Flask(__name__)

load_dotenv(verbose=True, dotenv_path='/vault/secrets/.env')

# Logging
log = logging.getLogger()
out_hdlr = logging.StreamHandler(sys.stdout)
fmt = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
out_hdlr.setFormatter(fmt)
out_hdlr.setLevel(logging.INFO)
# append to the global logger.
log.addHandler(out_hdlr)
log.setLevel(logging.INFO)

@app.route('/')
def hello_world():
    # with open('/config/key.yaml', 'r') as stream:
    with open('key.yaml', 'r') as stream:
        config = safe_load(stream)
    log.info('Credentials printed out on web page')
    #return f'username: {os.environ.get("USERNAME")}      password: {os.environ.get("PASSWORD")}'
    return "OK"

if __name__ == '__main__':

    #load_dotenv(verbose=True, dotenv_path='/Users/francois/Downloads/.env')
    app.run()
