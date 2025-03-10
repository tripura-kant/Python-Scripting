#!/bin/bash

SERVER_HEALTH_LOG="/home/user/health_reports/server_health.log"
ALERT_LOG="/home/user/health_reports/alert.log"

monitor_memory_usage() {
    > $SERVER_HEALTH_LOG
    > $ALERT_LOG

    while true; do
        ps -eo pid,rss --sort=-rss | awk 'NR>1 {print $1, $2}' | while read -r pid rss; do
            mem_mb=$((rss / 1024))

            echo "$pid ${mem_mb}MB" >> $SERVER_HEALTH_LOG

            if [ $mem_mb -gt 20 ]; then
                echo "$pid ${mem_mb}MB" >> $ALERT_LOG
            fi
        done

        sleep 5
    done
}

monitor_memory_usage