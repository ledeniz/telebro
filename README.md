# Telebro
Alerts you via Telegram if one a certain webserver is not available. 

## Description
A simple python script, which checks certain URLs (read from `config.yml`) and triggers a Telegram chatbot in case
a site is unreachable (or returns a HTTP status code >= 300). The errors are also logged to a logfile (`error.log`).

You can run it as a cronjob, but please beware: as of now, there is nothing stored in memory. If your host is down
and you run the script every minute, you will get notified every minute.

If you use the script as a module, you can easily overwrite the filepaths of the config and log files.

## Requirements
- python3
- python3-urllib3
- python3-yaml

## TODOs
- [ ] Implement some sort of caching mechanism to avoid Navi-like behaviour

## FAQ
### How do I create a Telegram bot?
#### Chat with the [@botfather](https://telegram.me/botfather) to create a Telegram bot.

More info: https://core.telegram.org/bots

### How do I get my chat ID?
#### You get it via the bot API once you've used your bot once.

More info: https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id

### Why Telegram! I Hate Telegram! It's Evil! You're evil! Why not E-Mail!
#### Yes.
It's easy to extend the script for usage with email or anything else. For me the Telegram Bot API is sufficient
and I don't have the hassle with a SMTP server. Also I don't get notifications for my mails because of spam. 
