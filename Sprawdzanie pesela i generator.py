from datetime import date
import random
class Pesel():
    PESEL_WEIGHTS = (9, 7, 3, 1, 9, 7, 3, 1, 9, 7)
    MONTH_CORRECTIONS = {
        (81, 92): (80, 1800),
        (1, 12): (0, 1900),
        (21, 32): (20, 2000),
        (41, 52): (40, 2100),
        (61, 72): (60, 2200)
    }
    def __init__(self,pesel):
        self.pesel=pesel
    @property
    def date_of_birth(self):
        return self.date_from_pesel(self.pesel)
    @property
    def sex(self):
        return 'M' if int(self.pesel[9]) % 2 else 'F'
    @classmethod
    def date_from_pesel(cls, pesel):
        year, month, day = cls._extract_date_components(pesel)
        return date(year, month, day)
    @classmethod
    def _pesel_control_sum(cls, pesel):
        digits = [int(char) for char in pesel]
        return sum(weight * digit for weight, digit in zip(cls.PESEL_WEIGHTS, digits)) % 10
    
    @classmethod
    def _extract_date_components(cls, pesel):
        year, month, day = int(pesel[0:2]), int(pesel[2:4]), int(pesel[4:6])
        for lower, upper in cls.MONTH_CORRECTIONS:
            if lower <= month and month <= upper:
                m_offset, y_offset = cls.MONTH_CORRECTIONS[(lower, upper)]
                return (year + y_offset, month - m_offset, day)
        raise InvalidPersonalInfoError('Invalid date in PESEL - unknown month.')
    @property
    def __str__(self):
        return self.pesel
    
    @classmethod
    def generate(cls,year,month,day,sex):
        MONTH_LENGHTS = [31,28,31,30,31,30,31,31,30,31,30,31]
        if year < 1800:
            raise ValueError('Year error')
        if month < 1 or month > 12:
            raise ValueError('month error')
        for i in range(1,12):
            if i==month:
                
                max_day=MONTH_LENGHTS[i]
        if month == 2 and (year % 400 == 0 or (year % 4 == 0 and not year % 100 == 0)):
            max_day = 29
        
        print(max_day)    
        if day < 1 or day > max_day:
            raise ValueError('day error')
        while True:
            sumakontrolnatemp=0
            peseltemp=''
            peseltab=[]
            if year>=1800 and year<1900:
                peseltemp=str(year-1800)
                peseltemp=peseltemp+str(month+80)
            elif year>=1900 and year<2000:
                peseltemp=str(year-1900)
                if month<10:
                    peseltemp=peseltemp+'0'+str(month)
                else:
                    peseltemp=peseltemp+str(month)
            elif year>=2000 and year<2100:
                peseltemp=str(year-2000)
                peseltemp=peseltemp+str(month+20)
            elif year>=2100 and year<2200:
                peseltemp=str(year-2100)
                peseltemp=peseltemp+str(month+40)
            elif year>=2200 and year<2300:
                peseltemp=str(year-2200)
                peseltemp=peseltemp+str(month+60)
            peseltemp=peseltemp+str(day)
        
            for x in range(0, 3):
                rand = random.randint(0, 9)
                peseltemp=peseltemp+str(rand)
            if sex=='M':
                rand = random.randint(0, 9)
                if rand%2==0:
                    peseltemp=peseltemp+str(rand+1)
                else:
                    peseltemp=peseltemp+str(rand)
            elif sex=='F':
                rand = random.randint(1, 9)
                if rand%2==1:
                    peseltemp=peseltemp+str(rand-1)
                else: 
                    peseltemp=peseltemp+str(rand)
            for i in range(0, 10):
                sumakontrolnatemp=sumakontrolnatemp+cls.PESEL_WEIGHTS[i]*int(peseltemp[i])
            i=sumakontrolnatemp%10
            peseltemp=peseltemp+str(i)
            peseltab=peseltemp
            return cls(peseltab)
