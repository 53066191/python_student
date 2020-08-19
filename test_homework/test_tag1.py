'''
=======================
Author:李浩
时间：2020/8/18:22:16
Email:lihaolh_v@didichuxing.com
=======================
'''
import pytest
import requests
import random


def test_creat_data():
    pass


class TestTag1:
    @pytest.fixture( scope="session" )
    def token(self):
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
        res = requests.get( url=url, params=params )
        token = (res.json()["access_token"])
        return token

    def test_creat(self, token,tagname,tagid):
        """
        创建标签
        method  =  post
        url = https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token=ACCESS_TOKEN
        :param token:
        :return:
        """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={token}"
        data = {
            "tagname":tagname,
            "tagid": tagid
        }
        res = requests.post( url=url, json=data )
        print(res.json())
        return res.json()

    def test_update(self,token,tagid,tagname):
        """
        请求方式：POST（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token=ACCESS_TOKEN
        :return:
        """

        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={token}"
        json ={
            "tagid":tagid,
            "tagname": tagname
        }
        res = requests.post(url=url,json=json)
        print(res.json())
        return res.json()

    def test_delete(self,token,tagid):
        """
        请求方式：GET（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token=ACCESS_TOKEN&tagid=TAGID
        :return:
        """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={token}&tagid={tagid}"
        res = requests.get(url=url)
        print(res.json())
        return res.json()

    def test_get(self,token,tagid):
        """
        请求方式：GET（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/tag/get?access_token=ACCESS_TOKEN&tagid=TAGID
        :return:
        """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/get?access_token={token}&tagid={tagid}"
        res = requests.get(url=url)
        print(res.json())
        return res.json()

    def test_work(self,token):
        tagid= 4
        tagname = "test"+str(random.randint(0,9999999999))
        self.test_creat(token,tagname=tagname,tagid=tagid)
        self.test_get(token,tagid=tagid)
        self.test_update(token,tagid=tagid,tagname="l1i")
        self.test_delete(token,tagid=tagid)



