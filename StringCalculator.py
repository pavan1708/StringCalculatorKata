from re import *
class StringCalculator:
    def __init__(self):
        pass


    def add(self,numbers):
        if(numbers==""):
            return 0

        elif(len(numbers)==1):
            self.CheckNegative([numbers])
            return int(numbers)

        else:
            num=split(",|\n",numbers) 
            sum=0
            self.CheckNegative(num)
            for i in num:
                if(i.isalpha() and i.islower()):
                    temp=ord(i)-96
                else:
                    temp=int(i)


                if(temp>1000):
                    continue
                else:
                    sum+=temp 
            
            return sum

    def CheckNegative(self,num):
        exp_msg="Negatives not allowed-"
        org_len=len(exp_msg)

        for i in num:
            if(not(i.isalpha()) and int(i)<0):
                exp_msg=exp_msg+" "+i

        if(org_len<len(exp_msg)):
            raise NegativeNumException(exp_msg)        

    

class NegativeNumException(Exception):
    def __init__(self,msg):
        super().__init__(msg)
