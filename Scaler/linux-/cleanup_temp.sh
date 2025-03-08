#!/bin/bash

sudo find test_temp_dir -type f -name "*.tmp"

echo "Do you want to delete the files? "
read response

if [[ "$response" == "yes" ]]; then
 sudo find test_temp_dir -type f -name "*.tmp" -delete
  echo "Files deleted."
else
  echo "Operation canceled."
fi