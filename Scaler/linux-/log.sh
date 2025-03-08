#!/bin/bash

log_file="/home/user/logs/log_file.log"

display_help() {
    echo "Usage: $0 [-h] [-i] [log_file_path]"
    echo
    echo "Analyze system logs to identify and summarize error messages."
    echo
    echo "Options:"
    echo "  -h        Display this help message."
    echo "  -i        Interactive mode."
    echo "  log_file_path Specify the path to the log file. Default is /var/log/syslog."
}

count_errors() {
    echo "Total number of errors: $(grep -ci 'error' "$log_file")"
}

list_errors() {
    echo "List of unique error messages and their frequencies:"
    grep -io 'error.*' "$log_file" | sort | uniq -ci | sort -nr
}

search_errors() {
    read -p "Enter a keyword to search for specific errors: " keyword
    echo "Searching for errors containing the keyword '$keyword':"
    grep -i "$keyword" "$log_file" | grep -i 'error'
}

interactive_mode() {
    echo "Select the type of log analysis to perform:"
    echo "  1. Count Errors"
    echo "  2. List Errors"
    echo "  3. Search Errors"
    read -p "Enter your choice: " choice

    case $choice in
        1)
            count_errors
            ;;
        2)
            list_errors
            ;;
        3)
            search_errors
            ;;
        *)
            echo "Invalid choice."
            exit 1
            ;;
    esac
}

while getopts ":hi" opt; do
    case ${opt} in
        h )
            display_help
            exit 0
            ;;
        i )
            interactive_mode
            exit 0
            ;;
        \? )
            display_help
            exit 1
            ;;
    esac
done
shift $((OPTIND -1))

if [ "$#" -eq 0 ] || [ -f "$log_file" ]; then
    interactive_mode
fi