This repository contains a container that can be used to allow a given vip through contrail API

# How to use

```
podman run -e HOST_IP=$HOST_IP -e IP=$IP quay.io/karmab/contrail-allow-vips:latest
```

where:

- HOST_IP is your contrail api IP
- IP is the 

Additionally, other env variables can be provided:

- MAC to associate a specific virtual mac address to the vip. 
- VRRPID to calculate the virtual mac address to associate to the vip.

## Problems?

Open an issue!

Mc Fly!!!

karmab
