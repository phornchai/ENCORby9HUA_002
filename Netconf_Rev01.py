from ncclient import manager

m = manager.connect(
    host="ios-xe-mgmt.cisco.com",
    port=10000,
    username="developer",
    password="C1sco12345",
    hostkey_verify=False
    )

netconf_reply = m.get_config(source="running")
print(netconf_reply)

