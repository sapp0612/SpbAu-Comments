#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math #С помощью данной команды подключается библиотека math 
import numpy # Как и в случае с предыдущей командой, данная команда подключает библиотеку, но нв сей раз - numpy
import matplotlib.pyplot as mpp #А эта команда подключает функции pyplot из библиотеки matplotlib, которая в нашей программе будет использована под именем mpp

# Эта программа рисует график функции, заданной выражением ниже

if __name__=='__main__':# С помощью данной команды мы проверяем тот факт, что программа запущена не как модуль 
    arguments = numpy.arange(0, 200, 0.1)# С помощбю данно йкоманды создается список чисел от до 200,исключая правую границу с шагом 0.1
    mpp.plot(#Эта команда задает график по значения x,которые описанны в строке 19, и по зачениям y, которые описаны в строке 20
        arguments,#значения по x
        [math.sin(a) * math.sin(a/20.0) for a in arguments]#значения по y
    )
    mpp.show()#Данная команда выводит график

