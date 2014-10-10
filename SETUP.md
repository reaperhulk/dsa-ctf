**This server requires Python 3 to operate!**

To run the server locally:

* Create a new virtualenv and `pip install -r requirements.txt`. If python3 is
  not your default python you may need to pass `-p /path/to/python3.4` when
  creating your venv.
* Run `openssl dsaparam -genkey 2048 -out dsa.key` in the directory to generate
  a DSA key.
* `python main.py`
