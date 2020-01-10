import module1.createData as cd

import module2.createData_1 as cd1

instance = cd.DATA(first_date = "10/10/2019", shape = 100)

df = instance.create_dataframe()

print(df)


instance1 = cd1.DATA1(first_date = "10/10/2019", shape = 100)

df = instance1.create_dataframe()

print(df)
