#!/bin/bash
LOG_FILE="/home/user/error_reports/website_health.log"
ERROR_REPORT="/home/user/error_reports/website_report.log"


grep ERROR logfile.log >> $LOG_FILE
#2025-03-10 16:34:54 ERROR: This is error number 1.
#2024-07-22 23:11:15 2024-07-22 23:10:55 ERROR: This is error number 1. #answer

create_report() {
  echo "Error Report - $(date -u +"%a %b %d %T UTC %Y")" >> $ERROR_REPORT
  echo "Total Errors: $(wc -l $LOG_FILE)" >> ERROR_REPORT
  echo "Latest Error: tail -n 1 $LOG_FILE" >> $ERROR_REPORT
}

create_report