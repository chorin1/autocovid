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

### Long version 
Tutorial for running this bot for free on GCP - still in the works..
