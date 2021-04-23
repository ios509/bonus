''' Calculating salary increases '''
''' If he makes 5,000 sales, he will make 5% of the sales 
    If he makes 10,000 sales, he will make 10% of the sales '''

class c_s_i():

    def __init__(self , name, sales, salary):
        self.name = name
        self.sales = sales
        self.salary = salary

    def salary_after_bonus(self):

        if self.sales < 5000 :
            return f'Sorry Mr {self.name}, You are did not reach the desired target'

        elif 5000 <= self.sales < 10000:
            cal = 0.05 * self.salary + self.salary
            return f'Congratulations Mr {self.name}, You got a 5% bonus.\n Your salary befor bonus is : {self.salary} \n Your salary after bonus is : {cal}'

        elif 1000 <= self.sales :
            cal2 = 0.10 * self.salary + self.salary
            return f'Congratulations Mr {self.name}, You got a 10% bonus.\n Your salary befor bonus is : {self.salary} \n Your salary after bonus is : {cal2}'


employee = c_s_i('nasser', 1000,2000)
print(employee.salary_after_bonus())

employee = c_s_i('nasser', 6000,2000)
print(employee.salary_after_bonus())

employee = c_s_i('nasser', 11000,2000)
print(employee.salary_after_bonus())

'''
('nasser', 1000,2000)
Sorry Mr nasser, You are did not reach the desired target

('nasser', 6000,2000)
Congratulations Mr nasser, You got a 5% bonus.
 Your salary befor bonus is : 2000 
 Your salary after bonus is : 2100.0
 
('nasser', 11000,2000)
Congratulations Mr nasser, You got a 10% bonus.
 Your salary befor bonus is : 2000 
 Your salary after bonus is : 2200.0
'''

