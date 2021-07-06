from typing import List


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        tableList = dict()
        tableTittle = set()
        for t in orders:
            tableTittle.add(t[2])
            if t[1] in tableList:
                if t[2] in tableList[t[1]]:
                    tableList[t[1]][t[2]] += 1
                else:
                    tableList[t[1]][t[2]] = 1
            else:
                tableList[t[1]] = dict()
                tableList[t[1]][t[2]] = 1
        tt = sorted(list(tableTittle))
        tableList = sorted(tableList.items(), key=lambda x: int(x[0]))
        ans = list()
        ans.append(['Table'] + tt)
        for table in tableList:
            curTable = list()
            curTable.append(table[0])
            for food in tt:
                if food in table[1]:
                    curTable.append(str(table[1][food]))
                else:
                    curTable.append('0')
            ans.append(curTable)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.displayTable([["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]))
