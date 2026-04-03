# OSPF Lab

# OSPF Lab Part 1&2 
## Part 1



## Part 2
<img width="738" height="562" alt="ospf2" src="https://github.com/user-attachments/assets/ea1db5f3-873b-47aa-99cd-885923ed07be" />

In part 2, I configured the same topology but uesed interface-based OSPF configuration intsead of network statements. I enabled OSPF dieclty on each router interface using "ip ospf 1 area 0", including the loppback interfaces. I then set the correct passive interfaces so OSPF would advertise those networks without sending hello packets on interfaces wheree no neighbors existed, such as loopbacks and the LAN interface on R4.
