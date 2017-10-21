#!/bin/bash
curl -XPOST https://api.twilio.com/2010-04-01/Accounts/{ACCOUNT_SID}/Messages.json \
        -d "Body=$(cat /home/StoreWatcher/store_watcher.log)" \
        -d "To=#########" \
        -d "From=##########" \
        -u '{ACCOUNT_SID}:{AUTH_TOKEN}'
