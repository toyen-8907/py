# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 17:34:42 2021

@author: jerry
"""

#globals locals nonlocals global
var_global = 1
var_nonlocal = 2
def local_fun():
    var_nonlocal = 22
   
    def local_inner():
        global var_global
        nonlocal var_nonlocal
        var_global = 111
        var_nonlocal = 222
    local_inner()
    print('localfun輸出 var_global =',var_global)
    print('localfun輸出 var_nonlocal =',var_nonlocal)
    
    
var_global = 1
var_nonlocal = 2
print('主程式輸出 var_global =',var_global)
print('主程式輸出 var_nonlocal = ',var_nonlocal)
print()
local_fun()
print()
print('主程式輸出 var_global =',var_global)
print('主程式輸出 var_nonlocal = ',var_nonlocal)
