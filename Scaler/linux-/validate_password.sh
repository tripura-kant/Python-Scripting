#!/bin/bash
clear
validate_password(){
local password="$1"

if [ ${#password} -lt 8 ]; then
  echo "Weak pass"
  return 1
fi

if ! [[ "$password" =~ [A-Z] ]]; then
  echo "Weak pass"
  return 1
fi
}


read  -p "Enter your password: " user_pass
validate_password "$user_pass"