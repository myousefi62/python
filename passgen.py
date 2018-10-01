#!/usr/bin/env python
# -*- coding: utf-8 -*-
import  string
from random import *
char = u'ضصثقفغعهخحجچگکمنتالبیسشظطزرذدپو'
char += string.ascii_letters+string.punctuation+string.digits
password = "".join((choice(char)for x in range(randint(18,20))))
print password