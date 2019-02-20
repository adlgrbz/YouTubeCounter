import requests
import serial
from time import sleep

"""
Sample:
Home Made Project
https://www.youtube.com/channel/UCWxZWN7gi0h2ZylI2XF6g9w/featured
                               +-----------------------+
                                       channel_id
"""

channel_id = '>>> Your channal ID <<<'
api_key = '>>> Your API key <<<'

url = 'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={0}&key={1}'.format(channel_id, api_key)


def counter(url):
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

while True:
    portName = input('\nPort Name (Sample: COM5): ')

    try:
        port = serial.Serial(portName, 9600)
        print(port.isOpen())
        break
    except:
        print('Port Name Incorrect !')
    
while True:
    port.write(str.encode(counter(url)[1])) # subscriberCount
    sleep(1)
        
port.close()
