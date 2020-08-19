'''
=======================
Author:李浩
时间：2020/8/19:11:05
Email:lihaolh_v@didichuxing.com
=======================
'''
import requests
import json
class BaseApi():
    params={}

    def send(self,data):
        raw_data = json.dumps(data)
        for key,value in self.params.items():
            raw_data = raw_data.replace("${"+key+"}",value)
        data = json.loads(raw_data)
        return  requests.request(**data).json()

