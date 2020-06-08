#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# -*- coding: utf-8 -*-

from enum import Enum

token = "1190834838:AAGKYubjO91SaMTs-8zrNe30BJ3EK9rvWDo"
db_file = "database.vdb"


class States(Enum):
    """
    Мы используем БД Vedis, в которой хранимые значения всегда строки,
    поэтому и тут будем использовать тоже строки (str)
    """
    S_START = "0"  # Начало нового диалога
    S_GENDER = "1"
    S_MNAME = "2"
    S_FNAME = "3"

