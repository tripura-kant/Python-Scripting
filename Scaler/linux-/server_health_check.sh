#!/bin/bash

server_log_file=/home/user/health_reports/server_health.log

ps -aux | awk '{print $2,$4}' > $server_log_file

sleep 2