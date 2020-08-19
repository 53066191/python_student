'''
=======================
Author:李浩
时间：2020/8/18:22:06
Email:lihaolh_v@didichuxing.com
=======================
'''
import requests

class Util:

    def get_token(self):
        """
        method: get
        url =https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ID&corpsecret=SECRET
        :return:接口返回的json数据
        """
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        params = {
            "corpid": "wwfd249363e660c37a",
            "corpsecret": "Hlj6iwDxSZCr-bT3ok_GnA3MzIpeQqIjAXeIEa0R02M"
        }
        res = requests.get(url=url,params=params)
        token = (res.json()["access_token"])
        return token

