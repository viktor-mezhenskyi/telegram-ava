There is a mini app for report channels as "Russian aggression".

You should have **_Python_** and **_pip_** installed before use it.

Install dependency

```
pip install -r requirements.txt
```

# How to use it? 
1. Go to https://my.telegram.org/ and create app (more infor here https://core.telegram.org/api/obtaining_api_id). Save api_id, api_hash.
2. Add a new file to the root folder 'config.py'
3. Put next lines in 'config.py'
 ```
 api_id = <use api_id from https://my.telegram.org/>
 api_hash = use api_hash from https://my.telegram.org/>
 ```
 Example:
 ```
  api_id = '1234567'
  api_hash = 'b83d79bc8db6fdfae04ba12345678900'
 ```
 4. Put channels to file channels.txt (every name on new line). Better to use full name or link.
 5. Run message.txt if you want to change ban message.
 6. Run command `python main.py`
