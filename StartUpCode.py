import pymongo
import time

from subprocess import call

call(['Program beginning'], shell=True)


from pymongo import MongoClient
client = MongoClient('mongodb://admin:admin@ds237979.mlab.com:37979/apollo-dev')
db=client['apollo-dev']

while(True):

    time.sleep(10)
    #Store in database
    data={"Message": "I am Running!"}
    result=db.startup.insert(data)

#Instructions
# Add file into rc.local - sudo nano /etc/rc.local
# sudo reboot
# program will run in the background when rPi boots up
