# CCNA Network Access Notes

These notes cover the main **Network Access** topics from the CCNA. This section focuses on how devices connect to a network, how switches forward traffic inside a LAN, and how networks are designed to be efficient, secure, and reliable.

The topics in this section build the foundation for understanding how local networks operate. They include switching, VLANs, trunking, inter-VLAN routing, loop prevention, link aggregation, wireless basics, and basic switch security.

These notes are useful for:
- understanding core CCNA concepts
- revising key terms and definitions
- preparing for Packet Tracer labs
- reviewing commands and common exam points

The main topics covered are:
- network access basics
- VLANs
- trunking
- inter-VLAN routing
- switching basics
- STP
- EtherChannel
- wireless basics
- port security
- key commands

---

# VLANs
## What a VLAN is
A VLAN (Virtual Local Area Network) is a logical way to divide a switch network into separate broadcast domains. Devices can be connected to the same physical switch but placed in different VLANs so they behave as if they are on separate networks.

This improves network organization and allows administrators to separate groups of users without needing separate physical switches for each group.

## Why VLANs are used 
VLANs are used to:
- improve security by separating users and departments
- reduce broadcast traffic
- make the network easier to manage
- organize devices by department or role
- separate different types of traffic, such as voice and data

For example, HR devices can be placed in one VLAN, Sales in another, and Admin in another. This keeps traffic logically separated.

## Access port
An access port is a switch port that belongs to a single VLAN. It is usually connected to end devices such as:
- PCs
- printers
- IP phones
- servers

Traffic sent on an access port is not tagged with multiple VLAN information. The device connected to that port simply becomes part of the configured VLAN.

Example:
- If interface F0/1 is configured as an access port in VLAN 10, then any PC connected to F0/1 belongs to VLAN 10.

## VLAN membership
VLAN membership means assigning a device or switch port to a specific VLAN.

For example:
- PC on F0/1 → VLAN 10
- PC on F0/2 → VLAN 20
- PC on F0/3 → VLAN 30

A device becomes part of a VLAN based on the port it is connected to, unless more advanced methods are used. On the CCNA, you will usually work with port-based VLAN membership.

## Default VLAN
The default VLAN on Cisco switches is usually VLAN 1.
Key points:
- all switch ports are in VLAN 1 by default
- VLAN 1 exists automatically
- it is best practice not to use VLAN 1 for normal user traffic in production networks

VLAN 1 is commonly used at the start of labs, but in real networks it is better to move user devices into other VLANs.

## Native VLAN
The native VLAN is used on an 802.1Q trunk port. Frames in the native VLAN are sent untagged by default.

Key points:
- trunk ports carry traffic for multiple VLANs
- most VLAN traffic is tagged
- native VLAN traffic is untagged
- both ends of the trunk should use the same native VLAN

If the native VLAN does not match on both ends, it can cause communication and security issues.

## Voice VLAN
A voice VLAN is a special VLAN used for IP phone traffic.

It is used to:
- separate voice traffic from normal data traffic
- improve voice quality
- make it easier to apply QoS policies

A common setup is:
- the IP phone uses the voice VLAN
- the PC connected through the phone uses the data VLAN

This allows one switch port to support both a phone and a PC while keeping the traffic separated.

## Example of separating departments like HR, Sales, Admin
A company may use VLANs to separate departments like this:

| Department | VLAN ID | Subnet |
|-----------|---------|--------|
| HR        | 10      | 192.168.10.0/24 |
| Sales     | 20      | 192.168.20.0/24 |
| Admin     | 30      | 192.168.30.0/24 |

In this design:
- HR users are placed in VLAN 10
- Sales users are placed in VLAN 20
- Admin users are placed in VLAN 30

This means:
- broadcasts from HR stay inside VLAN 10
- Sales traffic stays in VLAN 20
- Admin traffic stays in VLAN 30
- communication between VLANs requires inter-VLAN routing

---

# Trunking 
## What a trunk port is
A trunk port is a switch port that carries traffic for multiple VLANs over a single link. Trunk ports are normally used between network devices such as:
- switch to switch
- switch to router
- switch to multilayer switch

## Why Trunks are needed 
Trunks are needed when multiple VLANs must be carried between devices.

For example, if SW1 and SW2 both have:
- VLAN 10 for HR
- VLAN 20 for Sales
- VLAN 30 for Admin

Then the link between the switches must carry traffic for all of those VLANs. Instead of using a separate cable for each VLAN, one trunk link can carry all VLAN traffic.

This makes the network:
- more efficient
- easier to scale
- easier to manage
- less expensive because fewer physical links are required

## 802.1Q tagging 
802.1Q is the standard used to identify which VLAN a frame belongs to when it travels across a trunk link.

When a frame is sent over a trunk:
- the switch adds a VLAN tag to the Ethernet frame
- the tag tells the receiving device which VLAN the traffic belongs to
- the receiving switch reads the tag and forwards the frame in the correct VLAN

This process is called **VLAN tagging**.

### Key point
Traffic on a trunk is usually tagged so that multiple VLANs can share the same link without mixing their traffic.

## Native VLAN behavior
The native VLAN is a special VLAN on an 802.1Q trunk.

Frames in the native VLAN are sent **untagged** by default.

### Important points
- all other VLAN traffic is normally tagged
- native VLAN traffic is untagged
- both ends of the trunk should have the same native VLAN configured
- a native VLAN mismatch can cause traffic problems and security issues

By default on many Cisco switches, VLAN 1 is the native VLAN unless it is changed.

## Trunk vs access port
| Port Type   | Description |
|------------|-------------|
| Access Port | Carries traffic for one VLAN only. Usually connects to end devices such as PCs, printers, or phones. |
| Trunk Port  | Carries traffic for multiple VLANs. Usually connects to other switches, routers, or multilayer switches. |

### Example
- A PC connected to F0/1 uses an **access port**
- A link between SW1 and SW2 uses a **trunk port**


---
# Inter-VLAN Routing

## Why VLANs cannot talk without a Layer 3 device
Each VLAN is a separate broadcast domain and usually a separate IP subnet. Devices in the same VLAN can communicate directly at Layer 2, but devices in different VLANs cannot communicate without a Layer 3 device.

A Layer 3 device, such as a router or multilayer switch, is needed to route traffic between VLANs. This process is called **inter-VLAN routing**.

For example:
- PC in VLAN 10 can talk to other devices in VLAN 10 directly
- PC in VLAN 10 cannot talk to a device in VLAN 20 unless traffic is routed

## Router-on-a-Stick
Router-on-a-stick is a method of inter-VLAN routing that uses:
- one physical router interface
- one trunk link between the router and switch
- multiple subinterfaces on the router

Each subinterface is configured for a different VLAN and acts as the default gateway for that VLAN.

Example:
- G0/0.10 for VLAN 10
- G0/0.20 for VLAN 20
- G0/0.30 for VLAN 30

This is common in labs and smaller networks.

## Multilayer switch idea
A multilayer switch can perform both Layer 2 switching and Layer 3 routing. Instead of sending VLAN traffic to an external router, the multilayer switch routes traffic internally.

This is usually faster and more scalable than router-on-a-stick, especially in larger networks.

A multilayer switch uses **SVIs (Switched Virtual Interfaces)** as the default gateways for VLANs.

## Subinterfaces
Subinterfaces are logical interfaces created on a single physical router interface.

Each subinterface:
- is assigned to a VLAN
- uses 802.1Q encapsulation
- has an IP address that acts as the default gateway for that VLAN

Example:
- interface G0/0.10
- encapsulation dot1Q 10
- ip address 192.168.10.1 255.255.255.0

## Default gateway for each VLAN
Each VLAN needs its own default gateway so devices can send traffic to other networks or VLANs.

Example:
| VLAN | Subnet | Default Gateway |
|------|--------|-----------------|
| 10   | 192.168.10.0/24 | 192.168.10.1 |
| 20   | 192.168.20.0/24 | 192.168.20.1 |
| 30   | 192.168.30.0/24 | 192.168.30.1 |

Without a default gateway, devices can only communicate inside their own VLAN.


---
# Switching Basics

## MAC address table
A switch uses a **MAC address table** to keep track of which MAC addresses are connected to which ports.

This helps the switch send frames only where they need to go instead of flooding all traffic everywhere.

The MAC address table contains:
- MAC addresses
- associated switch ports
- VLAN information

## How a switch learns MAC addresses
A switch learns MAC addresses by looking at the **source MAC address** of frames that arrive on its ports.

Example:
- if a frame enters F0/1 from PC1, the switch learns PC1’s MAC address on F0/1
- if a frame enters F0/2 from PC2, the switch learns PC2’s MAC address on F0/2

This process is called **MAC learning**.

If the destination MAC is unknown, the switch floods the frame out all other ports in that VLAN.

## Unicast, broadcast, unknown unicast
### Unicast
A unicast frame is sent from one device to one specific device.

### Broadcast
A broadcast frame is sent from one device to all devices in the same broadcast domain.

Example:
- ARP Request

### Unknown unicast
An unknown unicast happens when the switch does not know the destination MAC address yet. The switch floods the frame out all ports in the same VLAN except the port it came in on.

## Collision domain
A collision domain is the area where data collisions can occur.

With switches:
- each switch port is its own collision domain

This improves performance compared to older hub-based networks.

## Broadcast domain
A broadcast domain is the area in which a broadcast frame can travel.

By default:
- all ports in the same VLAN are in the same broadcast domain
- each VLAN is a separate broadcast domain

---
# STP

## Why STP exists
STP stands for **Spanning Tree Protocol**. It exists to prevent Layer 2 loops in switched networks.

When redundant links are added between switches for backup and reliability, loops can occur. STP prevents these loops by blocking certain redundant paths.

## Switching loops
A switching loop happens when there is more than one active path between switches and frames keep circulating endlessly.

This can cause serious network problems because switches forward broadcast and unknown unicast traffic repeatedly.

## Broadcast storms
A broadcast storm happens when broadcast traffic loops continuously through the network.

This can:
- consume bandwidth
- overload switch CPUs
- make the network unusable

Broadcast storms are one of the main reasons STP is necessary.

## Root bridge
STP elects one switch to become the **root bridge**.

The root bridge is the central reference point for the spanning tree. All other switches calculate the best path back to the root bridge.

The switch with the best bridge ID becomes the root bridge.

## Blocked ports
To prevent loops, STP places some redundant ports into a **blocking state**.

A blocked port:
- does not forward normal traffic
- helps prevent loops
- can become active if the active path fails

## Forwarding ports
Ports that are part of the active path remain in the **forwarding state**.

A forwarding port:
- sends and receives traffic
- learns MAC addresses
- forwards user traffic

## STP vs RSTP basic difference
### STP
Classic STP works, but it is slower to respond to network changes.

### RSTP
RSTP stands for **Rapid Spanning Tree Protocol**. It performs the same main function as STP but converges much faster when the network changes.

### Key idea
- STP = loop prevention
- RSTP = faster loop prevention and faster recovery

---
# EtherChannel

## What EtherChannel is
EtherChannel is a technology that bundles multiple physical links together into one logical link.

Instead of using each cable separately, the switch treats them as a single connection.

## Why it is used
EtherChannel is used to:
- increase bandwidth
- provide redundancy
- reduce the risk of STP blocking individual redundant links
- make links between switches more efficient

If one physical link in the bundle fails, the EtherChannel can continue using the remaining links.

## Load balancing idea
EtherChannel can distribute traffic across multiple physical links in the bundle. This helps improve performance by sharing the traffic load.

The links act as one logical interface, but traffic is balanced across the available member links.

## LACP vs PAgP
### LACP
LACP stands for **Link Aggregation Control Protocol**.

- open standard
- defined by IEEE 802.3ad
- can be used on different vendors’ devices

### PAgP
PAgP stands for **Port Aggregation Protocol**.

- Cisco proprietary
- used mainly on Cisco devices

### Key difference
- **LACP** = industry standard
- **PAgP** = Cisco proprietary

---
# Wireless Basics

## AP
An **AP (Access Point)** allows wireless devices to connect to a wired network using Wi-Fi.

It acts as a bridge between wireless clients and the LAN.

Examples of wireless clients:
- laptops
- phones
- tablets

## WLC
A **WLC (Wireless LAN Controller)** is used to centrally manage multiple access points.

It helps with:
- configuration
- security policies
- roaming
- monitoring
- firmware management

This is common in larger enterprise wireless networks.

## SSID
SSID stands for **Service Set Identifier**.

It is the name of the wireless network that users see when trying to connect to Wi-Fi.

Example:
- OfficeWiFi
- GuestWiFi

## WPA2/WPA3
WPA2 and WPA3 are wireless security standards used to protect Wi-Fi networks.

### WPA2
- older but still widely used
- provides authentication and encryption

### WPA3
- newer and more secure
- improves wireless protection

## Lightweight AP vs autonomous AP
### Lightweight AP
A lightweight AP is managed by a WLC.

It depends on the controller for much of its configuration and management.

### Autonomous AP
An autonomous AP is managed individually.

Each AP is configured separately, without a central controller.

### Key difference
- lightweight AP = controller-based
- autonomous AP = standalone

---
# Port Security

## What it does
Port security is a switch feature that helps control which devices are allowed to connect to a switch port.

It improves security by limiting the MAC addresses that can use a port.

## Limiting MAC addresses
With port security, an administrator can define how many MAC addresses are allowed on a port.

For example:
- only 1 MAC address allowed on a port
- only 2 MAC addresses allowed on a port

If too many MAC addresses appear, the switch can take action.

## Sticky MAC
Sticky MAC allows the switch to dynamically learn MAC addresses on a port and save them as secure MAC addresses.

This makes configuration easier because the administrator does not need to manually enter every MAC address.

## Violation modes
A violation happens when an unauthorized MAC address tries to use the port.

Common violation modes include:

### Protect
Drops traffic from unauthorized MAC addresses, but does not send an alert.

### Restrict
Drops unauthorized traffic and can log the violation or increase the violation counter.

### Shutdown
Places the port into an error-disabled state. This is the default and most secure mode.


---
## Key Commands
- show vlan brief
- show interfaces trunk
- show mac address-table
- show spanning-tree
- show etherchannel summary
- show port-security
