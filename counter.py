import requests
import serial
from time import sleep

"""
Home Made Project
https://www.youtube.com/channel/UCWxZWN7gi0h2ZylI2XF6g9w/featured
                               +-----------------------+
                                       channel_id
"""

# pewdiepie = 'UC-lHJZR3Gqxm24_Vd_AJ5Yw' :)

def counter():
    channel_id = '*** Your channel ID ***'
    api_key    = '***  Your API key   ***'

    url = ('https://www.googleapis.com/youtube/v3/channels?part=statistics&id='
           + channel_id + '&key=' + api_key)

    request = requests.get(url)
    data = request.json()   

    viewCount       = data['items'][0]['statistics']['viewCount']
    subscriberCount = data['items'][0]['statistics']['subscriberCount']
    videoCount      = data['items'][0]['statistics']['videoCount']
    
    return (
            viewCount,
            subscriberCount,
            videoCount
           )

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

while True:
    portName = input('\nPort Name (Sample: COM5): ')

    try:
        port = serial.Serial(portName, 9600)
        print(port.isOpen())
        break
    except:
        print('Port Name Incorrect !')
        continue
    
while True:
    port.write(str.encode(counter()[1])) # subscriberCount
    sleep(1)
        
port.close()
