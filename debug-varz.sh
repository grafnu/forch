#!/bin/bash
port=INIT
i=0
while [[ -n "$port" ]]; do
  i=$((i+1))
  echo $i > count.txt
  bin/net_clean
  sudo rm -rf inst
  bin/setup_stack local
  port=$(wget localhost:8001 -O- 2>/dev/null | grep dp_root_hop_port | grep -oF '6.0')
done
echo Done: $port
