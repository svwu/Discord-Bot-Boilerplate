# Discord Bot Boilerplate
This project will help to easily set up a Discord Bot, based on python and docker.
Simply check this project out and extend it for your needs!

One bot command has been added to give a hint how to add commands.
`commands`

You can change the text of the commands in `/src/command_text/commands.txt` and also add new commands on your own.


## Pre-Requirements
* [Create a Discord developer app](https://discord.com/login?redirect_to=%2Fdevelopers%2Fapplications)
* Create a bot and token
* Add following Permissions:
    * Texting
    * ...
* Create OAuth2 Url
* Add Bot to your desired Server

## Setup
* Copy your Bot token into a file "discord_bot_token" in the directory /secrets
* docker-compose up --build
