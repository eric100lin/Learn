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
class Solution:
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

r = Solution().invalidTransactions(["alice,20,800,mtv","alice,50,100,beijing"])
print(r)
r = Solution().invalidTransactions(["alice,20,800,mtv","alice,50,1200,mtv"])
print(r)
r = Solution().invalidTransactions(["alice,20,800,mtv","bob,50,1200,mtv"])
print(r)

r = Solution().invalidTransactions([
"bob,689,1910,barcelona",
"alex,696,122,bangkok",
"bob,832,1726,barcelona",
"bob,820,596,bangkok",
"chalicefy,217,669,barcelona",
"bob,175,221,amsterdam"])
print(r)
#["bob,689,1910,barcelona","bob,832,1726,barcelona","bob,820,596,bangkok"]

r = Solution().invalidTransactions([
"bob,627,1973,amsterdam",
"alex,387,885,bangkok",
"alex,355,1029,barcelona",
"alex,587,402,bangkok",
"chalicefy,973,830,barcelona",
"alex,932,86,bangkok",
"bob,188,989,amsterdam"])
print(r)
#["bob,627,1973,amsterdam","alex,387,885,bangkok","alex,355,1029,barcelona"]

r = Solution().invalidTransactions([
"bob,899,1971,budapest","maybe,850,824,budapest",
"alex,505,187,tokyo","lee,953,1572,toronto","alex,622,61,frankfurt",
"lee,191,1261,madrid","iris,740,925,luxembourg","iris,681,401,moscow",
"chalicefy,298,731,madrid","maybe,549,988,moscow","alex,28,1683,singapore",
"chalicefy,894,550,rome","xnova,892,990,rome","lee,353,1522,shanghai",
"xnova,804,549,taipei","maybe,716,1727,shenzhen","chalicefy,770,1156,taipei",
"alex,957,466,munich","bob,381,1136,tokyo","alex,496,1662,luxembourg","xnova,849,354,munich",
"bob,486,1751,barcelona","xnova,350,14,moscow","iris,858,583,chicago","maybe,511,1002,toronto",
"maybe,838,585,amsterdam","bob,536,217,toronto","iris,24,1596,hongkong","chalicefy,894,1074,beijing",
"maybe,502,530,barcelona","lee,95,1916,madrid","maybe,313,1394,madrid","chalicefy,160,1591,hongkong",
"xnova,280,1023,tokyo","chalicefy,224,920,singapore","bob,725,501,prague","alex,481,35,frankfurt",
"xnova,336,423,guangzhou","xnova,535,382,istanbul","lee,806,1597,chicago","lee,124,1012,tokyo",
"iris,627,665,shenzhen","alex,160,651,amsterdam","bob,674,193,dubai","alex,290,770,tokyo",
"maybe,406,659,shenzhen","lee,493,1002,warsaw","alex,929,591,taipei","bob,456,6,luxembourg",
"iris,985,1959,newdelhi","xnova,816,1147,singapore","bob,110,73,frankfurt","chalicefy,80,85,warsaw",
"xnova,266,162,munich","xnova,295,1944,newdelhi","chalicefy,47,141,madrid","xnova,78,205,shanghai",
"bob,487,260,bangkok","bob,880,628,hongkong","maybe,162,406,mexico","xnova,390,1187,hongkong",
"chalicefy,810,289,zurich","alex,534,96,jakarta","chalicefy,768,1412,moscow","chalicefy,594,840,milan",
"xnova,844,1048,luxembourg","xnova,15,274,tokyo","alex,756,1473,hongkong","alex,54,1760,singapore",
"xnova,353,1644,zurich","lee,353,475,zurich","lee,973,1591,munich","bob,262,120,hongkong",
"alex,759,31,barcelona","bob,257,803,mexico","alex,353,1074,prague","lee,854,604,chicago",
"lee,354,140,warsaw","lee,827,521,prague","chalicefy,73,439,zurich","bob,365,899,shanghai",
"chalicefy,490,1473,beijing","lee,115,531,rome","maybe,358,774,istanbul","xnova,95,824,frankfurt",
"lee,532,712,hongkong","lee,766,616,newdelhi","lee,231,1150,zurich","maybe,237,71,bangkok",
"bob,255,747,taipei","lee,520,1825,montreal","bob,744,401,guangzhou","alex,284,877,toronto",
"maybe,129,1999,frankfurt","xnova,293,294,jakarta","chalicefy,283,901,beijing","lee,884,881,luxembourg",
"alex,168,1279,shenzhen","alex,348,1434,rome","iris,958,537,paris"])
print(r)
#["bob,899,1971,budapest","maybe,850,824,budapest","alex,505,187,tokyo","lee,953,1572,toronto","lee,191,1261,madrid","iris,740,925,luxembourg","iris,681,401,moscow","chalicefy,298,731,madrid","maybe,549,988,moscow","alex,28,1683,singapore","chalicefy,894,550,rome","xnova,892,990,rome","lee,353,1522,shanghai","xnova,804,549,taipei","maybe,716,1727,shenzhen","chalicefy,770,1156,taipei","alex,957,466,munich","bob,381,1136,tokyo","alex,496,1662,luxembourg","xnova,849,354,munich","bob,486,1751,barcelona","xnova,350,14,moscow","maybe,511,1002,toronto","maybe,838,585,amsterdam","bob,536,217,toronto","iris,24,1596,hongkong","chalicefy,894,1074,beijing","maybe,502,530,barcelona","lee,95,1916,madrid","maybe,313,1394,madrid","chalicefy,160,1591,hongkong","xnova,280,1023,tokyo","chalicefy,224,920,singapore","bob,725,501,prague","alex,481,35,frankfurt","xnova,336,423,guangzhou","lee,806,1597,chicago","lee,124,1012,tokyo","iris,627,665,shenzhen","alex,160,651,amsterdam","bob,674,193,dubai","alex,290,770,tokyo","maybe,406,659,shenzhen","lee,493,1002,warsaw","alex,929,591,taipei","bob,456,6,luxembourg","iris,985,1959,newdelhi","xnova,816,1147,singapore","chalicefy,80,85,warsaw","xnova,266,162,munich","xnova,295,1944,newdelhi","chalicefy,47,141,madrid","xnova,78,205,shanghai","bob,487,260,bangkok","bob,880,628,hongkong","maybe,162,406,mexico","xnova,390,1187,hongkong","chalicefy,810,289,zurich","alex,534,96,jakarta","chalicefy,768,1412,moscow","xnova,844,1048,luxembourg","alex,756,1473,hongkong","alex,54,1760,singapore","xnova,353,1644,zurich","lee,353,475,zurich","lee,973,1591,munich","bob,262,120,hongkong","alex,759,31,barcelona","bob,257,803,mexico","alex,353,1074,prague","lee,854,604,chicago","lee,354,140,warsaw","lee,827,521,prague","chalicefy,73,439,zurich","bob,365,899,shanghai","chalicefy,490,1473,beijing","lee,115,531,rome","maybe,358,774,istanbul","xnova,95,824,frankfurt","lee,532,712,hongkong","lee,766,616,newdelhi","lee,231,1150,zurich","bob,255,747,taipei","lee,520,1825,montreal","bob,744,401,guangzhou","alex,284,877,toronto","maybe,129,1999,frankfurt","xnova,293,294,jakarta","chalicefy,283,901,beijing","lee,884,881,luxembourg","alex,168,1279,shenzhen","alex,348,1434,rome","iris,958,537,paris"]