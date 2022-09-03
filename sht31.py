import smbus
import time
count = 0
temp = 0
cTemp = 0
cTemp1 = 0
humidity = 0
humidity1 = 0
humidity2 = 0
 
# Get I2C bus
bus = smbus.SMBus(1)

while count < 5:
	# SHT31 address, 0x44(68)
    	bus.write_i2c_block_data(0x44, 0x2C, [0x06])
     
    	time.sleep(0.5)
     
    
    	# Read data back from 0x00(00), 6 bytes
    	# Temp MSB, Temp LSB, Temp CRC, Humididty MSB, Humidity LSB, Humidity CRC
    	data = bus.read_i2c_block_data(0x44, 0x00, 6)
     
    	# Convert the data
    	temp1 = data[0] * 256 + data[1]
    	cTemp1 = -45 + (175 * temp1 / 65535.0)
    	humidity1 = 100 * (data[3] * 256 + data[4]) / 65535.0 

    	#
    	temp += cTemp1
    	humidity += humidity1
    
    	count +=1

print (" {:.2F}".format(temp/count))
print (" {:.2F}".format(humidity/count))
 