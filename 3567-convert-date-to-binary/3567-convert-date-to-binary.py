class Solution:
    def convertDateToBinary(self, date: str) -> str:
        
        dates = [int(char) for char in date if char != '-']

        year = int(''.join(map(str, dates[:4]))) 
        month = int(''.join(map(str, dates[4:6]))) 
        day = int(''.join(map(str, dates[6:])))
        year_bin = bin(year)[2:]   
        month_bin = bin(month)[2:]
        day_bin = bin(day)[2:]

        s_year=str(year_bin)
        s_month=str(month_bin)
        s_day=str(day_bin)
        s=s_year +'-'+ s_month + '-' + s_day
        return s

        
