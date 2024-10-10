from datetime import datetime

class Solution(object):
    def daysBetweenDates(self, date1, date2):
        """
        :type date1: str
        :type date2: str
        :rtype: int
        """
        Day1 = datetime.strptime(date1, "%Y-%m-%d").date()
        Day2 = datetime.strptime(date2, "%Y-%m-%d").date()

        diff = abs((Day2 - Day1).days)

        return diff        
        