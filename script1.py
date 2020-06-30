import pandas as pd
data = pd.DataFrame()
data['name'] = ['Brent','John','Sendy']
data['email'] = ['br2004@email.ru','jn.1988@gmail.com','sendy.b09@mail.ru']
data['age'] = [15,32,26]
data.at[0 , 'email'] = 'brent04@gmail.com'
print(data)
