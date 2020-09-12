class Employee:

    raise_amount=1.04

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@company.com'

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amount)

    @classmethod
    def from_string(cls,str):
        first,last,pay=str.split('-')
        return cls(first,last,pay)

    @staticmethod
    def is_workday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True

class Developer(Employee):
    raise_amount=1.10

    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang=prog_lang

dev_1=Developer('Sabari','Krishna',50000,'Python')
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
print(dev_1.fullname())
