#!/bin/bash
SERVER_IP="192.168.56.102"
ping -c 4 $SERVER_IP > ping.log
if grep -q "0% packet loss" ping.log; then
    echo "PASS: Connectivity OK"
else
    echo "FAIL: Connectivity issue"
fi
