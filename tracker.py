#!/usr/bin/python

import requests
import json

owner_banner = "This script is/was created by: internetrekluse"
print(owner_banner)

ip_addr = input("Enter an IP address: ")

request = requests.get("http://ip-api.com/json/"+ip_addr)
result = request
print(result.text)
