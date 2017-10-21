FROM 	arm32alpine/storewatcher:v2

COPY 	["crontab.config", \
	"send_notifications.sh", \
	"sw.py", \
	"store_watch.py", \
	"/home/StoreWatcher/" \  
	]
	

RUN 	["/bin/bash", "-c", "crontab /home/StoreWatcher/crontab.config"] 
