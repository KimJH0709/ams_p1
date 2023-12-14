import unittest
import easter_egg_list
from unittest.mock import patch


class EasterEggTest(unittest.TestCase):
    def test_able_easter_True(self):
        ilist = ['7503','1111','2024','1225', '1015']
        for item in ilist:
            self.assertEqual(easter_egg_list.able_easter(item),True)

    def test_able_easter_False(self):
        ilist = ['1234','4567',('!')]
        for item in ilist:
            self.assertEqual(easter_egg_list.able_easter(item),False)

    @patch('builtins.print')

    def test_find_easter(self,mock_print):
        ilist = ['7503','1111','2024','1225', '1015']
        easter_list=["Sofrware Interaction Lab.","빼빼로","NEW YEAR","Merry Christmas","전북대 개교기념일입니다."]

        for i in range(len(ilist)):
            easter_egg_list.find_easter(ilist[i])
            mock_print.assert_called_with("[EVENT] " + easter_list[i])

if __name__ == '__main__':
    unittest.main()
        