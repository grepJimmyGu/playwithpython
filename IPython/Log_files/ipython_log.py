# IPython log file

a = 5
a
from numpy.random import randn
data = {i : randn() for i in range(7)}
print data
an_apple = 1.12321
an_pear = 1321.123
get_ipython().magic(u'pinfo an_apple')
# %run any .py code on the ipython 
get_ipython().magic(u'run Entertainment_center')
import webbrowser
import time

def take_break(x):
    """Take INPUT number of breaks by watching STEPHEN CURRY highlight!!"""
    i = 1
    total_breaks = x
    print("This program starts at"+time.ctime())
    while (i <= total_breaks):
        time.sleep(2)
        webbrowser.open("https://www.youtube.com/watch?v=SevHZgBnfF0")
        i = i+1
    print ("number of breaking time:"+str(i-1))
get_ipython().magic(u'pinfo take_break')
# Magic command: any command starting with %
import numpy as np
a = np.random.randn(100,100)
get_ipython().magic(u'timeit np.dot(a,a)')
# %reset
get_ipython().magic(u'hist')
# %pwd
# %qtconsole
t = np.array([[1,1,1],[1,1,1]])
print t
# cumsum
t.cumsum()
# sum of row
print t.cumsum(axis=0)
# sum of col
print t.cumsum(axis = 1)
# sum of height
# print t.cumsum(axis = 2)
from matplotlib import pyplot as plt
plt.plot(randn(1000).cumsum())
plt.show()
_i13
_i13
_
-
2*10
-
2*10
_i1
_
2*10
_
_i13
get_ipython().magic(u'logstart')
from numpy.random import randn
# %pwd
# %qtconsole
t = np.array([[1,1,1],[1,1,1]])
print t
# cumsum
t.cumsum()
# sum of row
print t.cumsum(axis=0)
# sum of col
print t.cumsum(axis = 1)
# sum of height
# print t.cumsum(axis = 2)
from matplotlib import pyplot as plt
plt.plot(randn(1000).cumsum())
plt.show()
# refer the imput of line 13 _i13
2*10
# '_' refer the last input
get_ipython().magic(u'logstate')
data = {i : randn() for i in range(7)}
print data
get_ipython().magic(u'logoff #created log file')
get_ipython().magic(u'logstate #created log file')
get_ipython().magic(u'logstop #created log file')
