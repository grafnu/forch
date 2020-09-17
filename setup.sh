bin/setup_stack local dhcp
sudo ip link set t1sw1-eth9 down
sudo ip link set t1sw2-eth10 down
sudo ip addr add 240.0.0.1/24 dev lo
sudo ip link set t1sw2-eth28 down 
sudo ip link set t1sw1-eth6 down 
sudo ip link set t1sw1-eth11 down
