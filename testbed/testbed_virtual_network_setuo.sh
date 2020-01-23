#/bin/bash

echo adding static routes
ip route add 10.0.250.0/23 via 10.0.254.71 dev vlt_outside_br
ip route add 10.0.130.0/24 via 10.0.254.71 dev vlt_outside_br
ip route add 10.0.131.0/24 via 10.0.254.76 dev vlt_outside_br

# source NAT for external traffic inbound to VM management interfaces
iptables -t nat -A POSTROUTING -o vlt_mgt_br -j MASQUERADE

# source NAT for external traffic inbound to virtual topology
iptables -t nat -A POSTROUTING -o vlt_outside_br -j MASQUERADE

# optional: NAT all outbound traffic from jalapeno/the server itself.  Uncomment if needed
# iptables -t nat -A POSTROUTING -o <server_outside_nic> -j MASQUERADE
