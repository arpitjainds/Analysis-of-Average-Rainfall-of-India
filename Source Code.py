
# coding: utf-8

# In[10]:

import pandas as pd
import matplotlib.pyplot as plt

get_ipython().magic('matplotlib notebook')
plt.style.use('seaborn-colorblind')


# In[3]:

data = pd.read_csv('Rainfall_India1901-2015.csv')
data.head()


# In[4]:

list(pd.read_csv('Rainfall_India1901-2015.csv').columns.values)


# In[5]:

years = pd.read_csv('Rainfall_India1901-2015.csv', index_col='YEAR').transpose().columns.values
years


# In[6]:

january = pd.read_csv('Rainfall_India1901-2015.csv', index_col='JAN').transpose().columns.values
february = pd.read_csv('Rainfall_India1901-2015.csv', index_col='FEB').transpose().columns.values
march = pd.read_csv('Rainfall_India1901-2015.csv', index_col='MAR').transpose().columns.values
april = pd.read_csv('Rainfall_India1901-2015.csv', index_col='APR').transpose().columns.values
may = pd.read_csv('Rainfall_India1901-2015.csv', index_col='MAY').transpose().columns.values
june = pd.read_csv('Rainfall_India1901-2015.csv', index_col='JUN').transpose().columns.values
july = pd.read_csv('Rainfall_India1901-2015.csv', index_col='JUL').transpose().columns.values
august = pd.read_csv('Rainfall_India1901-2015.csv', index_col='AUG').transpose().columns.values
september = pd.read_csv('Rainfall_India1901-2015.csv', index_col='SEP').transpose().columns.values
october = pd.read_csv('Rainfall_India1901-2015.csv', index_col='OCT').transpose().columns.values
november = pd.read_csv('Rainfall_India1901-2015.csv', index_col='NOV').transpose().columns.values
december = pd.read_csv('Rainfall_India1901-2015.csv', index_col='DEC').transpose().columns.values
annual = pd.read_csv('Rainfall_India1901-2015.csv', index_col='ANNUAL').transpose().columns.values

janfeb = pd.read_csv('Rainfall_India1901-2015.csv', index_col='Jan-Feb').transpose().columns.values
marmay = pd.read_csv('Rainfall_India1901-2015.csv', index_col='Mar-May').transpose().columns.values
junsep = pd.read_csv('Rainfall_India1901-2015.csv', index_col='Jun-Sep').transpose().columns.values
octdec = pd.read_csv('Rainfall_India1901-2015.csv', index_col='Oct-Dec').transpose().columns.values


# In[94]:

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.figure()
plt.plot(years, annual, '-o', c='navy', alpha=0.4)
plt.xlabel('Years')
plt.ylabel('Rainfall Density in mm')
plt.title('Rainfall Variation of India (1901-2015)')
plt.legend(['Average of Year'])


# In[112]:

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
cmap = matplotlib.cm.viridis
plt.figure()
plt.scatter(years, janfeb, cmap=cmap)
plt.scatter(years, marmay, cmap=cmap)
plt.scatter(years, junsep, cmap=cmap)
plt.scatter(years, octdec, cmap=cmap)
plt.xlabel('Years (1901-2015)')
plt.ylabel('Rainfall Density in mm')
plt.title('Average Rainfall(Various Phases of the Year)')
plt.legend(['Jan-Feb','Mar-May','Jun-Sep','Oct-Dec'])


# In[102]:

# create a 3x3 grid of subplots
fig, ((ax1,ax2),(ax3,ax4),(ax5,ax6),(ax7,ax8),(ax9,ax10),(ax11,ax12)) = plt.subplots(6, 2, sharex=False, sharey=False, figsize=(9,20)) 

ax2.scatter(years, february, c=february, s=february)
ax2.set_title("Rainfall in February") 
ax2.set_xlabel('Years (1901-2015)') 
ax2.set_ylabel('Av. Rainfall in mm')

ax1.scatter(years, january, c=january, s=january)
ax1.set_title("Rainfall in January") 
ax1.set_xlabel('Years (1901-2015)') 
ax1.set_ylabel('Av. Rainfall in mm')

ax3.scatter(years, march, c=march, s=march)
ax3.set_title("Rainfall in March") 
ax3.set_xlabel('Years (1901-2015)') 
ax3.set_ylabel('Av. Rainfall in mm')

ax4.scatter(years, april, c=april, s=april)
ax4.set_title("Rainfall in April") 
ax4.set_xlabel('Years (1901-2015)') 
ax4.set_ylabel('Av. Rainfall in mm')

ax5.scatter(years, may, c=may, s=may)
ax5.set_title("Rainfall in May") 
ax5.set_xlabel('Years (1901-2015)') 
ax5.set_ylabel('Av. Rainfall in mm')

ax6.scatter(years, june, c=june, s=june)
ax6.set_title("Rainfall in June") 
ax6.set_xlabel('Years (1901-2015)') 
ax6.set_ylabel('Av. Rainfall in mm')

ax7.scatter(years, july, c=july, s=july)
ax7.set_title("Rainfall in July") 
ax7.set_xlabel('Years (1901-2015)') 
ax7.set_ylabel('Av. Rainfall in mm')

ax8.scatter(years, august, c=august, s=august)
ax8.set_title("Rainfall in August") 
ax8.set_xlabel('Years (1901-2015)') 
ax8.set_ylabel('Av. Rainfall in mm')

ax9.scatter(years, september, c=september, s=september)
ax9.set_title("Rainfall in September") 
ax9.set_xlabel('Years (1901-2015)') 
ax9.set_ylabel('Av. Rainfall in mm')

ax10.scatter(years, october, c=october, s=october)
ax10.set_title("Rainfall in October") 
ax10.set_xlabel('Years (1901-2015)') 
ax10.set_ylabel('Av. Rainfall in mm')

ax11.scatter(years, november, c=november, s=november)
ax11.set_title("Rainfall in November") 
ax11.set_xlabel('Years (1901-2015)') 
ax11.set_ylabel('Av. Rainfall in mm')

ax12.scatter(years, december, c=december, s=december)
ax12.set_title("Rainfall in December") 
ax12.set_xlabel('Years (1901-2015)') 
ax12.set_ylabel('Av. Rainfall in mm')


# In[ ]:



