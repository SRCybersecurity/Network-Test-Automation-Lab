# Network Test Automation Lab (VMware)

A simulated network test lab built using **VMware** and **Ubuntu virtual machines**. </br>
Designed to validate connectivity, traffic flow, and fault scenarios while automating network test execution and log analysis using Bash and Python scripts.

[![Bash](https://img.shields.io/badge/Bash-scripting-blue)](https://www.gnu.org/software/bash/)  
[![Python](https://img.shields.io/badge/Python-automation-yellow)](https://www.python.org/)  
[![VMware](https://img.shields.io/badge/VMware-virtualization-lightgrey)](https://www.vmware.com/)

---

## Project Overview

This project demonstrates:

- Creation of a multi-node network lab using VMware VMs.
- Basic network tests: connectivity, port availability, and throughput.
- Simulation of network faults: packet loss, latency, and service downtime.
- Automation of testing and log analysis using Bash and Python, reducing manual effort.

---

## Lab Setup

### Virtual Machines

| VM Name | Role             | IP Example      | Purpose                       |
|---------|-----------------|----------------|-------------------------------|
| Client  | Test initiator  | 192.168.56.101 | Sends traffic, runs scripts   |
| Server  | Service provider | 192.168.56.102 | Receives traffic, hosts services |

**Networking:** Host-Only or Internal Network in VMware (isolated lab).

### Installed Tools

- `ping` — connectivity testing  
- `netcat (nc)` — port availability  
- `curl` — HTTP requests  
- `iperf3` — throughput measurement  
- `tcpdump` — packet capture  
- `iproute2` — latency and packet loss simulation

---

## Test Scenarios

### 1. Connectivity Test

Verify network reachability between Client and Server:

    ping -c 4 <Server-IP>
### Test Scenarios
1. Connectivity Test </b>
Purpose: Verify network reachability between Client and Server. </b>
Command example:

       ping -c 4 <Server-IP>
2. Port Availability Test </b>
Purpose: Ensure specific service ports are reachable.

Server:
    
    nc -l -p 8080
Client: 

    nc <Server-IP> 8080
3. Traffic Flow Test
Purpose: Measure bandwidth and throughput. </b>

Server:

       iperf3 -s
Client: 
     
     iperf3 -c <Server-IP>

---
### Fault Simulation
Network Down:

    sudo ifconfig eth0 down (Server)
Packet Loss: 

    sudo tc qdisc add dev eth0 root netem loss 30%
Latency: 

    sudo tc qdisc add dev eth0 root netem delay 200ms

### All faults can be removed with:

    sudo tc qdisc del dev eth0 root netem
    sudo ifconfig eth0 up

---
#### Automation
For automation create a  network_test.sh

---
### Run the network_test.sh
Script for network test automation

    ./network_test.sh

---
### Run analyze_logs.py
For analysing logs run 

    python3 analyze_logs.py

---
### Project Highlights
Realistic VMware network lab for learning and testing.  </br>
Automated network test execution with Bash and Python.</br>
Supports fault simulation for resilience testing. </br>
Ideal for hands-on learning in network engineering and automation. </br>

---

#### Help and give some suggestion for future improvements.
#### THANK YOU 
#### END
