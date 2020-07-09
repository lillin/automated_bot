# Automated bot
This bot demonstrates functionalities of the social_network system. Bot
read rules from a config file (.env, example is provided in project root) where specified number of users will be created, max number of posts per user and also max likes amount per user. 
Based on these properties, random amount will be caclulated on script execution. 

## Installation
- First of all install **Python3.6**
- Create `.env` file and set desirable values to variables (see example.env for details)
- Also you can add HOST variable into `.env` to set IPv4 from your local host manually, i.e. `HOST=172.80.0.0`. 
You can run `ipconfig` on Windows or `hostname -I` on Linux to get IPv4 address.
- Run `pip install -r requirements.txt` from root project directory. 
Please note, that on Windows you might run `python -m pip install -r requirements.txt` in PowerShell as administrator.
- Run social_network application (see [social_network/README.md](https://github.com/lillin/social_network#installation) for more details)
- Finally, run `python run.py` to generate data through social_network's API.
