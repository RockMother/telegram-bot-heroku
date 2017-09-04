# telegram-bot-heroku
Simple starter kit for create and deploy telegram bot written on the python to the heroku.

# Step-by-step
### Create simple telegram bot
1) Go to [bot father](https://telegram.me/botfather), create new bot and get token.
2) Clone this repo
3) Go to folder with repo and type your token into bot.py or add your token as enviroment variable.
4) Open console and run `python bot.py`.
5) Open telegram and check your echo bot.

### Deploy to heroku
1) Go to [Heroku](https://heroku.com) and create new account
2) Install [heroku-cli](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)
3) Go to folder with your bot and run console
4) Run `heroku login` and input your heroku credentials
5) Run `heroku create` to create heroku enviroment
6) Run `heroku config:set TELEGRAM_TOKEN=Your token from botFather`
7) Commit all changes to your repo and run `git push heroku master` 

