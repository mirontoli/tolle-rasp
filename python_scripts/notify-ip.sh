#!/bin/bash
# Author: @mirontoli 2016
# save this file on your raspberry pi - notify-ip.sh
# make it executable: chmod +x notify-ip.sh
# run it: ./notify-ip.sh &
# make sure it runs even after you quit your ssh session: disown %1
TOKEN="your-token-generated-by-slack"
SLACK_URL="https://hooks.slack.com/services/${TOKEN}"
SLACK_ICON=':pager:'
function post_to_slack() {
  IP=$(curl -s https://api.ipify.org) 
  SLACK_MESSAGE="Current IP Address is \`\`\`${IP}\`\`\`"
  curl -X POST --data "payload={\"text\": \"${SLACK_ICON} ${SLACK_MESSAGE}\"}" ${SLACK_URL}
}

while :
do
  post_to_slack
  sleep 3600 #one hour
done
