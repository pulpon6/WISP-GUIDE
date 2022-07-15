import os
 
#curl = 'curl -s -X POST https://api.telegram.org/bot5383002047:AAE0Iv14l0_PNHoZOIvWMY9owKHLGeGmT14/sendMessage -d chat_id="-1001751413538" -d text="Hello World"'
 
count = 0
 
while count < 100:
 curl = 'curl -s -X POST https://api.telegram.org/bot5383002047:AAE0Iv14l0_PNHoZOIvWMY9owKHLGeGmT14/sendMessage -d chat_id="-1001751413538" -d text="Hello World"'
 os.system(curl)
 print(count)
 count+=1
