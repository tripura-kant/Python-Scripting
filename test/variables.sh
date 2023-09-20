#!/usr/bin/env bash
clear
readonly CONF_FILE=".conf"

if [[ -f ${CONF_FILE} ]]; then
  source "${CONF_FILE}"
else
  name=$(date)
fi

echo "${name}"
echo "${name1}"

exit 0
