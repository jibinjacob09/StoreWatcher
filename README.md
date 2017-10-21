#StoreWatcher

Storewatcher is a dockerized (using arm version of alpine linux) python program that checks for a price drop of a desired item in all the specified online stores. 

I am currently using this program to be alerted of any  price drops for the computer parts I want to purchase

## SETUP:
### Pre-Req: 
1. Must have docker installed
2. Install the custom arm32alpine image from the tar file, using
```bash
$ docker load < arm32alpine_storewatcher:v2.tar 
```

### Steps
1. Inside the project folder, you can build the docker image useing the dockerfile 
```bash
$ docker build . -t storewatcher
```
2. once the build is complete, you will need to manually start cron
load a container of storewatcher in the foreground
``` bash
$ docker run -it storewatcher
```
Once Inside the container, start cron daemon
``` bash
/ # crond
```


## Notes
1. You are able to set the time of the price fetch and sending notifications using the crontab or in the crontab.info file before docker build
2. send_notification.sh uses a POST command to Twilio's REST api to send a text message.  You will need to use your own Auth Token, numbers, and Account SID
3. All info regarding the store parts, base price,  and the store-page url should be provided in the store_watcher.py
4. sw.py only supports CandaComputers and NewEgg.   Looking into Amazon`
