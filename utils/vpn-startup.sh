#!/bin/bash

# Start OpenVPN in the background
openvpn --config /etc/openvpn/config.ovpn --daemon

# Wait for VPN connection to establish
sleep 10

# Configure routing to ensure all traffic goes through VPN
# The exact commands depend on your VPN setup
# Example: iptables -t nat -A POSTROUTING -o tun0 -j MASQUERADE

# Start the application
sh /utils/run.sh
