from datetime import datetime
import string
import random
import time
import numpy as np


class Utils:
    connected_clients = {"ClientsCount": 0, "Clients": {}}


    def getLogicDataTable(self, GlobalID):
        return (GlobalID / 1000000 + (GlobalID >> 31)) - (GlobalID * 1125899907 >> 63)

            
    def getCurrentDate(self):
        result = time.localtime(int(time.time()))
        return (result.tm_year * 1000 + result.tm_yday)


    def getTimeForNextDay(self):
        result = time.localtime(int(time.time()))
        return (86400 - (result.tm_sec + (result.tm_min * 60) + (result.tm_hour * 3600)))

    
    def getCurrentTimeInSecondsSinceEpoch(self):
        result = int(time.time())
        return result


    def getLobbyInfoCurrentDate(self):
        result = datetime.utcnow().strftime("%a %b %d %H:%M:%S UTC %Y")
        return result
        

    def getAccountCreatedDate(self):
        result = int(time.time())
        return (result * 1000)
        

    def getServerTime(self):
        result = int(time.time() * 1000)
        return result
        

    def getBattleTime(self):
        result = int(time.time())
        return result
        
        
    def EventTimer(self):
        result = time.localtime(int(time.time()))
        return (86400 - (result.tm_sec + (result.tm_min * 60) + (result.tm_hour * 3600)))
