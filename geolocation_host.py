
#!/usr/bin/env python 

import sys
import json
import urllib
import shodan

if len(sys.argv) < 2:
 print "Usage geolocation_host.py <address>"
 exit()

address = sys.argv[1]

def funct_geolocation():

 try:
  response_object = urllib.urlopen("http://freegeoip.net/json/"+address).read()
  geolocation = json.loads(response_object)
  api_object = shodan.Shodan("iFOqoOUu0NdlpAdRZBHqXP6nocEXHlxC")
  host = api_object.host(address)
  print("\n[+] Tracking ip {}".format(geolocation['ip']))
  print("----------------------------------------------")
  print('\tCountry_Name : {}\n\tCountry_Code : {}\n\tRegion_Code : {}\n\tRegion_Name : {}\n\tCity : {}\n\tZip_Code : {}\n\tMetro_Code : {}\n\ttimezone : {}\n\tlatitude : {}\n\tlongitude : {} ' .format(geolocation['country_name'],geolocation['country_code'],geolocation['region_code'],geolocation['region_name'],geolocation['city'],geolocation['zip_code'],geolocation['metro_code'],geolocation['time_zone'],geolocation['latitude'],geolocation['longitude']))

  print """
          IP: %s
          Host: %s
          Organisation: %s
          Operating System: %s

       """ % (host['ip_str'],host.get('hostnames'),host.get('org'),host.get('os'))

  for item in host['data']:
   print """ Port: %s
             Banner: %s """ % (item['port'],item['data'])


 except Exception as e:
  print 'Error: %s' % e
  exit()

funct_geolocation()

  
