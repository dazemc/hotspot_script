import os
import subprocess
import time

HOTSPOT_SSID = input("Enter SSID name you wish to use: ")
HOTSPOT_PASS = input("Enter password you wish to use, leave blank for open connection: ")
if HOTSPOT_PASS == '':
    HOTSPOT_PASS = "__none__"  # Default has to be valid length even if not used

subprocess.run(
    [
        "nmcli",
        "device",
        "wifi",
        "hotspot",
        "ssid",
        HOTSPOT_SSID,
        "password",
        HOTSPOT_PASS,
        "ifname",
        "wlan0",
    ],
    check=False,
)


time.sleep(3)
subprocess.run(
    [
        "nmcli",
        "c",
        "down",
        "Hotspot"
    ],
    check=False,
)

if HOTSPOT_PASS == "__none__":
    subprocess.run(
        [
        "nmcli",
        "connection",
        "modify",
        "Hotspot",
        "802-11-wireless-security.key-mgmt",
        "owe",
        ],
        check=False,
    )


time.sleep(3)
subprocess.run(
    [
        "nmcli",
        "c",
        "up",
        "Hotspot"
    ],
    check=False,
)
