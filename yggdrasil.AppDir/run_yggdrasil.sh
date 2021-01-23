#!/bin/bash
$HERE/usr/bin/yggdrasil -genconf > /tmp/yggdrasil.conf
sed 's|Peers: \[\]|Peers: \[ \n tcp://46.151.26.194:60575 \n \]|g' -i /tmp/yggdrasil.conf
$HERE/usr/bin/yggdrasil -useconffile /tmp/yggdrasil.conf
