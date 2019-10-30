# Automatic DSS-NIT Calicut Teacher Evaluator 

## Installing geckodriver for linux


1. Download geckodriver(v0.26.0)
```
wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz
```
2. Add the driver to your PATH so other tools can find it:

```
export PATH=$PATH:/path-to-extracted-file/.
```

## Running the code
1. Create a virtual environment.

```
virtualenv --python=$(which python3) venv
```

2. Activate the virtual environment.

```
source venv/bin/activate
```

3. Install the necessary requirements.

```
pip3 install -r req.txt
```

4. Run the python script to start the bot.

```
python3 app.py
```



