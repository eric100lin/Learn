'''
5183. Day of the Week
https://leetcode.com/contest/weekly-contest-153/problems/day-of-the-week/

Given a date, return the corresponding day of the week for that date.
The input is given as three integers representing the day, month and year respectively.
Return the answer as one of the following values 
{"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

Example 1:
Input: day = 31, month = 8, year = 2019
Output: "Saturday"

Example 2:
Input: day = 18, month = 7, year = 1999
Output: "Sunday"

Example 3:
Input: day = 15, month = 8, year = 1993
Output: "Sunday"

Constraints:
The given dates are valid dates between the years 1971 and 2100.
'''
from typing import *

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        weekday = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        # Sakamoto's methods
        # https://en.wikipedia.org/wiki/Determination_of_the_day_of_the_week#Sakamoto's_methods
        t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
        year -= month < 3
        return weekday[(year + year//4 - year//100 + year//400 + t[month-1] + day) % 7]

print(Solution().dayOfTheWeek(31, 8, 2019))
#Saturday
print(Solution().dayOfTheWeek(18, 7, 1999))
#Sunday
print(Solution().dayOfTheWeek(15, 8, 1993))
#Sunday