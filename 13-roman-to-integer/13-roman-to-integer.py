class Solution:
    def romanToInt(self, s: str) -> int:
        if len(s) < 1 or len(s) > 15:
            raise ValueError
        
        #A dict() obj to convert roman to int
        roman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        ints=[]
        s.upper()
        
        # This iteration converts roman to a list of integers
        for char in s:
            ints.append(roman[char])
        
        # First, we need to check and execute every subtraction.
        for index, number in enumerate(ints[:-1]):
            try:
                if ints[index] < ints[index+1]:
                    ints[index] = ints[index+1]-ints[index]
                    ints.pop((index+1))
            # After all subtractions are done and reflected on the shrinked list, the for iteration will not be able to finish anymore due to the list's shrinked length. So a except clause is needed.
            except:
                # Within the except clause, we can already return the final result, as every operation remaing is a sum.
                return sum(ints)
        return sum(ints)
            
            

