# Matrix Dessert Bot

Dessert bot is a small implementation of the [simple matrix bot lib](https://github.com/i10b/simplematrixbotlib) to be a general purpose matrix chat bot. 

### Features

Literally the only thing that it does at the moment is send YouTube thumbnails and their title for links that it sees in messages.
    
### Installation

At the moment I don't have it as a proper python package so for the time being you'll have to clone this repo and manually set up a python virtual environment.

Clone the repo

```
git clone https://github.com/no-budy/dessertbot.git
```

Setup the virtual environment

``` shell
cd dessertbot
venv .
source ./bin/activate
```

Install the required dependencies

``` shell
pip3 install simplematrixbotlib pyyaml urlextract beautifulsoup4 requests "matrix-nio[e2e]" 
```

Setup and configure your config file
```
cd dessert-bot 
mv example-config.yml config.yml
```

Once you're done with the config run
```
python3 dessertBot.py
```

#### You will have to remove the crypto files and session.txt every time you restart the bot. This seems to be an issue with the simplematrixbotlib



### Next steps

- Figure out why it can't relaunch a previous verified session (probably my misusage of the simplematrixbot library)
- Properly make a python package that can be installed with pip
- Find a good way to do user configuration


