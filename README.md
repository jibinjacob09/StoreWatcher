StoreWatcher

Storewatcher is a dockerized python program that checks for a price drop of a desired item in all the specified online stores. 

I am currently using this program to be alerted of any  price drops for the computer parts I want to purchase

SETUP:
*Pre-Req: 
 -> must have docker installed

*Steps
 -> download the tar file
 -> use the command line to enter:
	docker load Store_watcher.tar

 -> Currently the container is not set to run the program automatically, but that update will be coming soon
 -> run the docker container with options -it 
 -> and run the python file located at  
		/home/store_watcher/store-watch.py


FUTURE UPGRADES
1. automatic deployment of program after running the image
2. Twilio integreation to recieve text notifications for any price drops
3. Repeat-Every capability to receive price notifications at every time  interval you choose 
