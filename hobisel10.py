class Salary():
    pass

payment=Salary()

payment.firstname = "Koray"
payment.lastname = "Aydın"
"""antika yöntem """
print(payment.firstname)
print(payment.lastname)

#**********************************#

firstname_key='firstname'
firstname_val='Koray'

"""ikinci yönt."""
payment.firstname_key= firstname_val
print(payment.firstname)

"""üçüncü yönt."""
setattr(payment,'firstname','Koray')
print(payment.firstname)

"""daha iyi"""
setattr(payment,firstname_key,firstname_val)
print(payment.firstname)

firstname=getattr(payment,firstname_key)
print(firstname)

"""** **"""
print("daha best..")

payment_info={'firsname':'Koray', 'lastname':'Aydın'}
for key, val in payment_info.items():
    setattr(payment,key, val)

print(payment.firstname)
print(payment.lastname)

for key in payment_info.keys():
    print(getattr(payment, key))