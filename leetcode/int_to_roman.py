class Solution(object):
    def __init__(self):
        self.__dict__ = {1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        length = len(str(num))
        basic = 10 ** (length-1)
        roman_num = ""
        while basic != 0 and num != 0:
            count = int(num // basic)
            if 5 <= count < 9:
                count = 5
                roman_num = roman_num + self.__dict__[5 * basic]
            elif count < 4:
                roman_num = roman_num + self.__dict__[1 * basic] * count
            else:
                if count == 9:
                    number = 10
                else:
                    number = 5
                roman_num += (self.__dict__[basic] + self.__dict__[number * basic])
            num -= count * basic
            if num < basic:
                basic /= 10
        return roman_num