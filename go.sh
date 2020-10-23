#!/bin/bash -xe

sudo ip link set t1sw1-eth9 up
sudo ip link set t1sw2-eth10 up
sleep 30

sudo ovs-ofctl dump-flows t2sw1 | fgrep ff:ff:ff:ff | fgrep strip_vlan

sudo ip link set t1sw1-eth9 down
sleep 10
sudo ip link set t1sw2-eth10 down
sleep 30

sudo ovs-ofctl dump-flows t2sw1 | fgrep ff:ff:ff:ff | fgrep strip_vlan
