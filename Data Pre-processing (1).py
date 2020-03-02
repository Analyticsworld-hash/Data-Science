
# coding: utf-8

# In[2]:


#import pandas, numpy, matplotlib, pickle and math


# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pickle
from math import pi


# In[4]:


#import file by using pandas


# In[5]:


data = pd.read_csv('E:\R\credit.csv')


# In[6]:


#look at the information


# In[7]:


data.head(5)


# In[8]:


data.isnull().all()  # Checking if any Null in features


# In[9]:


# So with  result of above command, Result reflects no Null in any features.


# In[10]:


data.describe()  #summary of the data


# In[11]:


# Change the data to dataframe


# In[12]:


dataf = pd.DataFrame(data)


# In[13]:


dataf.shape # Look at Dimensions of complete  data


# In[14]:


dataf.isnull().any()


# In[15]:


# Still there is no any Null 


# In[16]:


dataf.head(5)


# In[17]:


dataf['count'] = 1 # add a counter to the Dataframe for future Grouping


# In[18]:


dataf.head()  # Counter was added to Back of DataFrame


# In[19]:


dataf['count'] # Look at data column


# In[20]:


dataf.columns  # Look at all columns


# In[21]:


datame = dataf[['checking_status', 'duration', 'credit_history', 'purpose',
       'credit_amount', 'savings_status', 'employment',
       'installment_commitment', 'personal_status', 'other_parties',
       'residence_since', 'property_magnitude', 'age', 'other_payment_plans',
       'housing', 'existing_credits', 'job', 'num_dependents', 'own_telephone',
       'foreign_worker', 'class', 'count']]


# In[22]:


datame.head(100)  #Look at dataframe


# In[23]:


checkacct = []  # Adding new column checkacct with respect to existing column "checking_status".if no checking then "No" else "yes"

for row in datame.checking_status:
    if row in ['no checking']:
        checkacct.append('no')
    else:
        checkacct.append('yes')
            
datame['checkacct'] = checkacct


# In[24]:


datame.head()


# In[25]:


saveacct = []    # Adding new column saveacct with respect to existing column savings_status.if "no known savings" then "No" else "yes"


for row in datame.savings_status:
    if row in ['no known savings']:
        saveacct.append('no')
    else:
        saveacct.append('yes')
        
datame['saveacct'] = saveacct


# In[26]:


datame.head(100)


# In[27]:


datame.columns


# In[28]:


datause = datame[['count','checkacct', 'saveacct',  'credit_history', 'purpose',
       'credit_amount',  'employment',
       'installment_commitment', 'personal_status', 'residence_since', 'age',
       'housing', 'existing_credits', 'job', 'num_dependents',
       'foreign_worker', 'class']]


# In[29]:


datause.head()


# In[30]:


datause['personal_status'].unique     #look at all the data in a column


# In[31]:


gender = []

for row in datause.personal_status:
    if row in ['male single', 'male mar/wid', 'male div/sep']:
        gender.append('male')
    else:
        gender.append('female')
        
datause['gender'] = gender


# In[32]:


datause.head(100)


# In[33]:


datause = datause[['count','class','age','gender','credit_history','checkacct', 'saveacct', 'num_dependents', 'housing', 'foreign_worker',  'employment','job', 'residence_since',
       'credit_amount', 'existing_credits']]


# In[34]:


datause.head(100)


# In[35]:


datause['employment'].unique


# In[36]:


employment = []

for row in datause.employment:
    if row in ['unemployed']:
        employment.append('unemployed')
    else:
        employment.append('employed')
        
datause['employment'] = employment


# In[37]:


datause.head(15)


# In[38]:


datause['age'].unique


# In[39]:


datause['age_bins'] = pd.cut(datause['age'], 6)  #to create bins


# In[40]:


datause['agerange'] = pd.cut(x=datause['age'], bins=[20, 30, 40, 50, 60, 70, 80], labels=['20', '30', '40','50', '60','70'])

#set bins in a range


# In[41]:


datause.columns


# In[42]:


datanew= datause[['count','class','agerange','age','gender','credit_history','checkacct', 'saveacct', 'num_dependents', 'housing', 'foreign_worker',  'employment','job', 'residence_since',
       'credit_amount', 'existing_credits']]


# In[43]:


datanew.head(100)


# In[44]:


datanew['job'].unique()


# In[45]:


jobskill = []

for row in datanew.job:
    if row in ['skilled']:
        jobskill.append('skill')
    elif row in ['unskilled resident']:
        jobskill.append('unskill')
    elif row in ['high qualif/self emp/mgmt']:
        jobskill.append('high skill')        
        
    else:
        jobskill.append('unemployed')
        
datanew['jobskill'] = jobskill


# In[46]:


datanew['jobskill'].unique()


# In[47]:


datanew = datanew[['count', 'class','agerange','age','gender', 'credit_history', 'checkacct','saveacct', 'num_dependents', 'housing', 'foreign_worker', 'employment',
       'jobskill', 'residence_since', 'credit_amount', 'existing_credits']]


# In[48]:


datanew.head(100)


# In[49]:


datanew['credit_amount'].unique()


# In[50]:


datanew['credit_amount_bins'] = pd.cut(x=datanew['credit_amount'], bins=[250, 3972, 8000, 10424, 18424 ])

#datanew.describe()


# In[51]:


datanew.head(6)


# In[52]:


datanew['credit_amount_bins'].unique()


# In[53]:


datanew['credit_amount_range'] = pd.cut(x=datanew['credit_amount'], bins=[250, 3972, 8000, 10424, 18424], labels=['low', 'mid', 'high', 'very-high'])


# In[54]:


datanew['credit_amount_range'].unique()


# In[55]:


datanew = datanew[['count', 'class','agerange','age','gender', 'credit_history', 'checkacct','saveacct', 'num_dependents', 'housing', 'foreign_worker', 'employment',
       'jobskill', 'residence_since', 'credit_amount', 'credit_amount_range', 'existing_credits']]


# In[56]:


datanew.head(10)


# In[57]:


datanew['num_dependents'].unique()


# In[58]:



datanew = datanew[['count', 'class', 'agerange', 'age', 'gender', 'credit_history', 'checkacct','saveacct', 'housing', 'foreign_worker', 'employment',
       'jobskill', 'residence_since', 'credit_amount_range', 'existing_credits']]


# In[59]:


datanew.head(10)


# In[60]:


datanew['credit_history'].unique()


# In[61]:


datanew.isnull().any()  #we have nulls -- need to fix


# In[62]:


datanew.isnull().sum()  #how many nulls per column


# In[63]:


dfage = datanew.groupby(['agerange'])


# In[64]:


dfage.head(2)


# In[65]:


#datanew['agerange'] = pd.to_numeric(datanew['agerange'])


# In[66]:


datanew['agerange'].isnull().any()


# In[67]:



#fix the nulls by copy one column to another

def fx(x):
    if pd.isnull(x['agerange']):
        return x['age']
    else:
        return x['agerange']

    print(datanew) 


datanew['agerange'] = datanew.apply(lambda x : fx(x), axis = 1)

print(datanew)


# In[68]:


datanew['agerange'].isnull().any()  #now fixed


# In[69]:


datanew.head()


# In[70]:


datanew['credit_amount_range'].isnull().any()


# In[71]:


datanew = datanew.dropna(axis=0)  #since it is one record, just delete


# In[72]:


datanew['credit_amount_range'].isnull().any()


# In[73]:


data.isnull().sum()


# In[74]:


datanew['agerange'].unique()  #float - no good


# In[75]:


datanew.info(['agerange'])  #looking at the information


# In[76]:


datanew['agerange'] = np.int64(datanew['agerange'])  #change float to int64


# In[77]:


datanew.info()


# In[78]:


datanew['target'] = ''  #for machine learning


# In[79]:


datanew.columns


# In[80]:


main = datanew[['count', 'class', 'agerange',  'gender', 'credit_history',
       'checkacct', 'saveacct', 'housing', 'foreign_worker', 'employment',
       'jobskill', 'residence_since', 'credit_amount_range',
       'existing_credits', 'target']]


# In[81]:


main.columns


# In[82]:


main.groupby('class').sum()  

#grouping -- remember the counter 
#bad credit is 300
#good credit is 699


# In[83]:


main.describe()

