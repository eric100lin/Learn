'''
1169. Invalid Transactions
https://leetcode.com/contest/weekly-contest-151/problems/invalid-transactions/

A transaction is possibly invalid if:
the amount exceeds $1000, or;
if it occurs within (and including) 60 minutes of 
another transaction with the same name in a different city.
Each transaction string transactions[i] consists of comma separated values 
representing the name, time (in minutes), amount, and city of the transaction.

Given a list of transactions, return a list of transactions that are 
possibly invalid.  You may return the answer in any order.

Example 1:

Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
Output: ["alice,20,800,mtv","alice,50,100,beijing"]
Explanation: The first transaction is invalid because 
the second transaction occurs within a difference of 60 minutes, 
have the same name and is in a different city. Similarly the second one is invalid too.

Example 2:

Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
Output: ["alice,50,1200,mtv"]

Example 3:

Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
Output: ["bob,50,1200,mtv"]

Constraints:
transactions.length <= 1000
Each transactions[i] takes the form "{name},{time},{amount},{city}"
Each {name} and {city} consist of lowercase English letters, and have lengths between 1 and 10.
Each {time} consist of digits, and represent an integer between 0 and 1000.
Each {amount} consist of digits, and represent an integer between 0 and 2000.
'''
from typing import *

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        T = []
        # parsing all transactions
        for tran in transactions:
            name, time, amount, city = tran.split(',')
            time, amount = int(time), int(amount)
            T.append((name, time, amount, city))

        invalidT = []
        # do comparison on all permutation
        for name, time, amount, city in T:
            invlid = amount > 1000
            if not invlid:
                for nameX, timeX, amountX, cityX in T:
                    if name == nameX and abs(time - timeX) <= 60 and city != cityX:
                        invlid = True
                        break
            if invlid:
                invalidT.append("{},{},{},{}".format(name, time, amount, city))
        return invalidT

class UglySolution:
    def invalidTransactions(self, transactions):
        dict = {}
        invalid = []
        for tran in transactions:
            tranInfo = tran.split(',')
            if tranInfo[0] in dict:
                dict[tranInfo[0]].append((int(tranInfo[1]),tranInfo[3],int(tranInfo[2]),tran))
            else:
                dict[tranInfo[0]] = [(int(tranInfo[1]),tranInfo[3],int(tranInfo[2]),tran)]
        for personTran in dict:
            personTranList = dict[personTran]
            for i in range(len(personTranList)):
                invalidi = False
                (timei,cityi,amounti,trani) = personTranList[i]
                if amounti > 1000:
                    invalidi = True
                for j in range(i,len(personTranList)):
                    (timej,cityj,amountj,tranj) = personTranList[j]
                    if cityi!=cityj and abs(timei-timej)<=60:
                        invalidi = True
                        if amountj <= 1000 and tranj not in invalid:
                            invalid.append(tranj)
                if invalidi and trani not in invalid:
                    invalid.append(trani)
        return invalid

import unittest

class InvalidTranTest(unittest.TestCase):

    def testExample1(self):
        tran = ["alice,20,800,mtv","alice,50,100,beijing"]
        r = Solution().invalidTransactions(tran)
        self.assertEqual(r, ["alice,20,800,mtv","alice,50,100,beijing"])

    def testExample2(self):
        tran = ["alice,20,800,mtv","alice,50,1200,mtv"]
        r = Solution().invalidTransactions(tran)
        self.assertEqual(r, ["alice,50,1200,mtv"])

    def testExample3(self):
        tran = ["alice,20,800,mtv","bob,50,1200,mtv"]
        r = Solution().invalidTransactions(tran)
        self.assertEqual(r, ["bob,50,1200,mtv"])

    def testLeetCodeTestCase1(self):
        tran = ["bob,689,1910,barcelona",
                "alex,696,122,bangkok",
                "bob,832,1726,barcelona",
                "bob,820,596,bangkok",
                "chalicefy,217,669,barcelona",
                "bob,175,221,amsterdam"]
        r = Solution().invalidTransactions(tran)
        self.assertEqual(r, ["bob,689,1910,barcelona","bob,832,1726,barcelona",
                             "bob,820,596,bangkok"])

    def testLeetCodeTestCase2(self):
        tran = ["bob,627,1973,amsterdam",
                "alex,387,885,bangkok",
                "alex,355,1029,barcelona",
                "alex,587,402,bangkok",
                "chalicefy,973,830,barcelona",
                "alex,932,86,bangkok",
                "bob,188,989,amsterdam"]
        r = Solution().invalidTransactions(tran)
        self.assertEqual(r, ["bob,627,1973,amsterdam","alex,387,885,bangkok",
                             "alex,355,1029,barcelona"])

if __name__ == "__main__":
    unittest.main()