lambda x: [OUTCOME IF TRUE] if [CONDITIONAL] else [OUTCOME IF FALSE]
mylambda=lambda age:"Welcome to BattleCity!" if age>=13 else "You must be over 13"
print(mylambda(13))

We could use the following code with a lambda function and the string method .split():
df['Email Provider'] = df.Email.apply(
    lambda x: x.split('@')[-1]
    )
    
lam=lambda x:True if x!='nan' else False
ad_clicks['is_click']=ad_clicks.ad_click_timestamp.apply(lam)
print(ad_clicks.head())    


import codecademylib
import pandas as pd

df = pd.read_csv('employees.csv')

# Add columns here
get_last_name = lambda x: x.split()[-1]
df['last_name'] = df.name.apply(get_last_name)

print(df)
    
    
 ** We can also operate on multiple columns at once.
 If we use apply without specifying a single column and add the argument axis=1, 
 the input to our lambda function will be an entire row, not a column.
 To access particular values of the row, we use the syntax row.column_name or row[‘column_name’].   
 
 ***applying pivot::
 import codecademylib
import numpy as np
import pandas as pd

orders = pd.read_csv('orders.csv')

shoe_counts = orders.groupby(['shoe_type', 'shoe_color']).id.count().reset_index()

shoe_counts_pivot = shoe_counts.pivot(
  columns = 'shoe_color',
  index = 'shoe_type',
  values = 'id').reset_index()

print(shoe_counts_pivot)
ex::::
import codecademylib
import pandas as pd

user_visits = pd.read_csv('page_visits.csv')

# Part 1.
print(user_visits.head(10))

# Part 2.
click_source = user_visits.groupby('utm_source').id.count().reset_index()

#Part 3.
print(click_source)

#Part 4.
click_source_by_month = user_visits.groupby(['utm_source', 'month']).id.count().reset_index()

#print(click_source_by_month)

#Part 5.
click_source_by_month_pivot = click_source_by_month.pivot(
	columns = 'month',
	index = 'utm_source',
	values = 'id').reset_index()

#Part 6.
print(click_source_by_month_pivot)

utm_source	1 - January	2 - February	3 - March
0	email	43	147	272
1	facebook	404	263	156
2	google	127	196	220
3	twitter	164	154	97
4	yahoo	262	240	255
