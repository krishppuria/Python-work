# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 16:16:13 2018

@author: Krishna
"""

import hashlib
name=input()
md5_hash=hashlib.md5(name.encode())
print("Hash using MD5: ",md5_hash.hexdigest())
sha1_hash=hashlib.sha1(name.encode())
print("Hash using SHA1: ",sha1_hash.hexdigest())