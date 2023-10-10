#!/usr/bin/env python
# coding: utf-8

# In[36]:


import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl
from matplotlib.colors import LinearSegmentedColormap, ListedColormap



# In[ ]:





# In[38]:


import matplotlib.cm as cm


# In[41]:


vals = ((cm.bwr(np.linspace(0,1,20)))*255).astype(int)


# In[42]:


vals.shape


# In[43]:


import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
plt.style.use('seaborn-poster')


# In[44]:


x = vals[:,0]
y = vals[:,1]
z = vals[:,2]

fig = plt.figure(figsize = (10,10))
ax = plt.axes(projection='3d')
ax.grid()

ax.scatter(x, y, z, c = (vals)/255, s = 50)
ax.set_title('3D Scatter Plot')

# Set axes label

ax.legend()
ax.set_xlim(0, 255)
ax.set_ylim(0, 255)
ax.set_zlim(0, 255)

ax.set_xlabel('Red', labelpad=20)
ax.set_ylabel('Blue', labelpad=20)
ax.set_zlabel('Green', labelpad=20)

plt.show()


# In[ ]:





# In[ ]:




