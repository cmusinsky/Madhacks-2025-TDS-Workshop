# HAProxy: Building a Load Balancer (least connections)

## What is HAProxy
HAProxy is a free and open source software that provides a high availability load balancer and proxy for TCP and HTTP-based applications that spreads requests across multiple servers. It is written in C and has a reputation for being fast and efficient. HAProxy is used by a number of high-profile websites including GoDaddy, GitHub, Bitbucket, Stack Overflow, Reddit, Slack

## Installation
We are assuming a Linux distro box of some sort.

For a Windows setup you can use WSL follow a guide here
<https://github.com/cmusinsky/Madhacks-2025-TDS-Workshop/blob/main/wsl_setup.md>

For Mac you can follow along and just install haproxy via homebrew using

```shell
brew install haproxy
```

On Ubuntu we can install with

```shell
apt install haproxy
```

Additionally we are using the Python Libraries Flask + Gunicorn for our demo backends so we will need to install those.

First if you don't have python setup, install python.

Once python is install setup your virtual environment

```shell 
python3 -m venv venv
source venv/bin/activate
```

Install our packages

```shell
pip install flask 
pip install gunicorn
```


## Setup
Your main config for HAProxy will be located at
> /etc/haproxy/haproxy.cfg

Next we need a backend to load balance our request to, this could be seperate servers, a cluster of containers, a container, etc.

For now we will setup two seperate simple backend applications:

These you can find in the project directory and start via the following commands:

```shell
gunicorn -w 1 -b 127.0.0.1:9000 slow_app:app

gunicorn -w 1 -b 127.0.0.1:9001 fast_app:app
```
## Testing

Next we want to try and hit the load balancer endpoint:

In one terminal session try:

```shell
curl http:localhost:8000
```
Open another terminal and run the command again to see what happens!

## Stats Page

Make a backup of the config

Open the config

Add below the backend block (not inside)

```cfg
listen stats
	bind *:8404
	http
	stats enable
	stats uri /stats
```

Restart HAProxy

```shell
sudo systemctl restart haproxy
```

Don't run this in production unless you further lock down access  to said page
## Building Further

Now that you have a working HAProxy load balancer, you’ve only seen the tip of the iceberg. HAProxy is widely deployed in production systems because it can be extended in dozens of powerful ways. Here are a few directions you can explore next:


You are not limited to two backend servers.

One can expand this to different types of load balancing methods as well as routing workloads. 

For example with AI API calls you may want to send new requests to different services depending on workload.
### Containerized Environments
HAProxy fits naturally into a container environment, especially for hackathon projects.

You can:

* run HAProxy itself in a container

* load balance between multiple containers using docker-compose

* use container names as hostnames (instead of 127.0.0.1)

* scale up replicas of a backend service and let HAProxy distribute traffic

A simple example backend block in Docker Compose would look like:

```shell
backend api
    balance leastconn
    server api1 api1:5000 check
    server api2 api2:5000 check
```

AND MORE
