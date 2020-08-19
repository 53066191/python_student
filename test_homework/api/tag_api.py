'''
=======================
Author:李浩
时间：2020/8/19:11:10
Email:lihaolh_v@didichuxing.com
=======================
'''
import yaml
from test_homework.api.util import Util
from test_homework.api.base_api import BaseApi
class TagApi(BaseApi):
    def __init__(self):
        self.token = Util().get_token()
        self.params["token"] = self.token

        with open("../api/tag_data.yaml",encoding="utf-8") as f :
            self.data = yaml.load(f,Loader=yaml.FullLoader)

    def test_create(self,tagid,tagname):
        """
        创建标签
        :param tagid: 标签id
        :param tagname: 标签名
        :return:
        """
        self.params["tagid"] = tagid
        self.params["tagname"] = tagname

        return self.send(self.data["create"])

    def test_get(self,tagid):
        """
        获取标签
        :param tagid: 标签id
        :return:
        """
        self.params["tagid"] = tagid

        return self.send(self.data["get"])

    def test_update(self,tagid,tagname):
        """
        更新标签
        :param tagid:标签id
        :param tagname: 标签名
        :return:
        """
        self.params["tagid"] = tagid
        self.params["tagname"] = tagname
        return self.send(self.data["update"])


    def test_delete(self,tagid):
        """
        删除标签
        :param tagid: 标签id
        :return:
        """

        self.params["tagid"] = tagid
        return self.send(self.data["delete"])


