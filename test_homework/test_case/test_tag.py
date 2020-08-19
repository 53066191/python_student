'''
=======================
Author:李浩
时间：2020/8/19:11:26
Email:lihaolh_v@didichuxing.com
=======================
'''
from test_homework.api.tag_api import TagApi

class TestTag():


    def test_create(self):
        print(TagApi().test_create(tagid="5",tagname="lihao1"))


    def test_get(self):
        print(TagApi().test_get(tagid="5"))

    def test_update(self):
        print(TagApi().test_update(tagid="5",tagname="测试"))

    def test_delete(self):
        print(TagApi().test_delete(tagid="5"))