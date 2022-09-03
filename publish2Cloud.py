#
#   Program name    |   publish2Cloud.py
#   Written by      |   Steven Owen
#   Date            |   January 2021
#   Version         |   1.0
#
#   Description     |   A program to publish PECSCU AtMoS data to an Adafruit.io dashboard
#
#   Comments        |   This version is functionally correctly.
#                       
#                       Version 1.0 : This is an update to Gas.py and Gas2.py but convberted to a single
#                       script.  The c# calling program has been rewritten such that the same
#                       function calls multiple python scripts and handles the output based
#                       on the returned data.


# Import standard python modules
import time
from datetime import datetime
import random
import sys


temp=sys.argv[1]
humid=sys.argv[2]
NOAE=sys.argv[3]
NOWE=sys.argv[4]
NO2AE=sys.argv[5]
NO2WE=sys.argv[6]

# Import Adafruit IO REST client.
from Adafruit_IO import Client, Feed

ADAFRUIT_IO_KEY = 'aio_zSzo19CDSDiy3sm09v2kp5y8yCD6'
ADAFRUIT_IO_USERNAME = 'PECSCU'

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

try:
    aio.send_data('nitric-oxide.temperature', temp)
    aio.send_data('nitric-oxide.humidity', humid)
    aio.send_data('nitric-oxide.nowe', NOWE)
    aio.send_data('nitric-oxide.noae', NOAE)
    aio.send_data('nitric-oxide.no2we', NO2WE)
    aio.send_data('nitric-oxide.no2ae', NO2AE)
except:
    print("An error occurred.")
