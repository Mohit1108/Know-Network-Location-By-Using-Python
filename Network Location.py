# Welcome to my Channel M Tech-G
# In This Video we Will Se How We Can Check the Network loaction by Using Python !
# Firstly you have
import json
# JavaScript Object Notation (JSON)
# It is a standard text-based format for representing structured data based on JavaScript object syntax.
# It is commonly used for transmitting data in web applications
# (e.g., sending some data from the server to the client,
# so it can be displayed on a web page, or vice versa)
from urllib.request import urlopen
# This Import Will Open Url
from tabulate import tabulate
# This Will Helpful For printing small tables without hassle:
url = "https://ipinfo.io/json"
# This Url Will Collect Information of IP!
# Don't Change this Url
response = urlopen(url)
# This Will Give Response To Open The Given URl
data = json.load(response)
# Here we Will Load the Response in a Json Format
# & Then We Will Set or Represent it to A Table Format !
table = [
         ["IP-address:", data["ip"]],## Detect Ip
         ["Server:", data["org"]], # Server
         ["City:", data["city"]], # City
         ["Country:", data["country"]], # Country
         ["Zip Code:", data["postal"]], #Zip COde
         ["State:", data["region"]], # State
         ["Time Zone:", data["timezone"]] # TimeZone
         ]
# This Is Table So We will Print All This Data in this formate
print(tabulate(table))
#print the Data
# GUys If you  like my video then dont forget to like and share this video
# And also subscribe this Channel
# & Code is present in my blog & My Github
# Guys Thanku so Much
