To run the server locally:

* Create a new virtualenv and `pip install -r requirements.txt`
* Run `openssl dsaparam -genkey 2048 -out dsa.key` in the directory to generate
  a DSA key.
* `python main.py`
