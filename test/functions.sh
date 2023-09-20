#!/usr/bin/env bash
clear

perform_backup() {
  rm -rf backup
  mkdir backup
  cd backup
  cd /Users/tripurakant/Documents/Imp-folder/py/Python-Scripting/test
  cp -r ${1} .
  tar -czvf backup.tar.gz *
  echo "Backup completed"
}

perform_backup $(1)

exit 0

