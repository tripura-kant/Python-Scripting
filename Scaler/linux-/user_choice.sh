#!/bin/bash

# Prompt the user for input
echo "Please choose an action (start, stop, status):"
read action

# Handle user input using case statement
case "$action" in
  start|START)
    echo "Starting the service..."
    ;;
  stop|STOP)
    echo "Stopping the service..."
    ;;
  status|STATUS)
    echo "The service is running."
    ;;
  *)
    echo "Invalid option selected. Please enter start, stop, or status."
    ;;
esac
