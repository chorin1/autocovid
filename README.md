# Autocovid
A dockerized telegram bot to automate signing ministry of education covid certificates.
<br><br>
<kbd>
<img src="https://user-images.githubusercontent.com/16934179/94419325-484cb280-018b-11eb-9a0b-d000795220a6.jpg" width="375" height="597">
</kbd>
## Setup
### Short version
1. Create a new [telegram bot](https://core.telegram.org/bots#6-botfather).
2. Make sure you are using a password to enter MOE parents portal (not by SMS).
3. `git clone`, `docker build` and `docker run` in your favorite cloud.  

The following environment variables need to be set:
| Key  | Description |
| :---:| :---: |
| MOE_USER  | MOE parent's portal username  |
| MOE_PASS  | portal password  |
| TELEGRAM_TOKEN  | Telegram bot token  |
| CHAT_ID  | chat ID where signing will be enabled  |
| DEV_CHAT_ID  | chat ID where exception will be sent to  |

<br>

### Long(er) version 
1. Create a bot using telegram's [botfather](https://core.telegram.org/bots#creating-a-new-bot).
    1. Use `/setcommands` in botfather to add `/sign` and `/hello` commands to your new bot.
    2. Optionally, `/setname` and `/setuserpic` to make the bot more appealing.
    3. Add your new bot to a private channel.
2. Find your private channel's chat_id and your own chat_id where the bot will send errors to. There are many ways to do this, [here's one](https://gist.github.com/mraaroncruz/e76d19f7d61d59419002db54030ebe35#gistcomment-3469738) of them.
3. Set up a new VM instance with [docker](https://docs.docker.com/engine/install/ubuntu/) (currently AWS & GCP have free-tiers with VM instances).
4. Clone this repo to the new set up instance.
5. Create a new file named `.env`. It should contain the list below (change the values with your own):
   ```
   MOE_USER=123456
   MOE_PASS=passpass
   TELEGRAM_TOKEN=1222222:AABBCC
   CHAT_ID=1234567
   DEV_CHAT_ID=123456
   ```
6. Run the following commands:

   ```
   sudo docker build --tag autocovid .
   sudo docker run --env-file=.env --name whatever --detach --restart=always autocovid
   ```
