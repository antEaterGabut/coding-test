#!/bin/bash

#gretting systems
line=$(printf '=%.0s' {1..28})
indent=$(printf ' %.0s' {1..6})
time=$(uptime)

echo "$line"
echo "$indent SENTINEL ANTER $indent"
echo "$line"
echo "$time"

#THIS FULL FUNCTION
#systems welcome
penjabaran_systems() {
  #ram
  ramUsed=$(free -m | awk 'NR==2 {print $3"MB"}')
  ramFree=$(free -m | awk 'NR==2 {print $4"MB"}')

  echo "RAM: $ramUsed/$ramFree"
  #storage
  storageUsed=$(df -h | awk 'NR==14 {print $1, $2, $3}' | column -t | awk '{print $3}')
  storageSize=$(df -h | awk 'NR==14 {print $1, $2, $3}' | column -t | awk '{print $2}')
  storagePersent=$(df -h | awk 'NR==14 {print $5}')

  echo "STORAGE: $storageUsed/$storageSize($storagePersent)"
  #
}

penjabaran_systems
