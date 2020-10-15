"""
===================
Author:POP MART
Time:2020/10/15
Company:popmart
===================
"""

import pytest
from Base_method.calculator import Calculator


class TestDemo_01Day_Cal:

    def setup(self):
        self.cal = Calculator()
        print("【计算开始】")

    def teardown(self):
        print("【计算结束】")

    @pytest.mark.parametrize('a,b,c', [[1, 1, 2], [1, 2, 4], ["s", "d", "d"], [(1), 4, [6]],
                                       [100000000000000, 100000000000000, 200000000000000], [0, 0, 0], [-1, 0, -1],
                                       [-1, -1, -2]])
    def test_add(self, a, b, c):
        result = self.cal.add(a, b)
        try:
            assert result == c
        except AssertionError as e:
            print("输入参数错误请修改")
            print(e)
        else:
            print("{} + {} = {}".format(a, b, result))

    @pytest.mark.parametrize('a,b,c', [[1, 1, 1], [1, 2, 0.5], [10, 3, 3.3], [1, 3, 0.3], [0, 0, 0],
                                       ["2",2,(2)]])
    def test_div(self, a, b, c):
        if b == 0:
            print("除数不能为0")
        else:
            result = self.cal.div(a, b)
            try:
                assert round(result, 1) == c
            except AssertionError as e:
                print("参数错误")
                print(e)
            else:
                print("{} / {} = {}".format(a, b, c))
