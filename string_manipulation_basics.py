c="chaitanya"
print (c)
d="san"
print (d)
print ("First input is {0}".format(c))
print ("second input is {0}".format (d))
print ("Second input is {1} and first input is {0}".format (c,d))

#==========================================================
a=input("Enter a input\n")
b=input("Enter the input\n")
print(a)
print(b)
print("First input is {0} and Second input is {1}".format (a,b))
print("=======================")
print("First input is {0}\nSecond input is {1}".format(a,b))
#============================================================


a="praveenajaysankiransahil"
print(type(a))
print(len(a))
print(a.count("a"))
print(a.count("e"))
print(a.index('v'))
print(a.index('a'))

#=============================================================

a="praveenajaysankiransahil"
print('e' in a)
print('z' in a)
print('e' in a or 'z' in a)
print ('y' in a or 'z' not in a)
print ('e' in a or 'z' not in a)
print ('e' in a and 'z' in a)
 #=============================================================

a="praveen  "
print(len(a))
rem_a=a.rstrip()
print(len(rem_a))
b="  praveen"
rem_b=b.lstrip()
print(len(rem_b))
c="  pra  veen  "
print(c)
rem_c=c.strip()
print(len(rem_c))
#==================================================================


a="praveenajaysankiransahil"
print (a.split('a'))
print (a.split('e'))
print (a.split('n'))
b="praveen:ajay:san"
print(b.split(':'))
print (b)
print("=========")
c=b.split(':')
print(c)

#=======================================================================

a="praveenajaysankiransahil"
print (a[0:3:1])
print(a[0:3])
print (a[0:11])
print(a[0:11:2])
print(a[0:14:3])
#======================================================================


a="praveenajaysankiransahil"
print (a[3])
print(a[3:10:2])
print(a[-1:-10:-1])
print(a[-1:-10:-2])
print(a)
print(a[0:len(a):3])
print(a[0:3])
print(a[-1::-2])
#=========================================================================




a="praveenajaysankiransahil"
print (a[0:5]+a[8:13])
a_1=a[0:5]
a_2=a[8:13]
print (a_1,a_2)
c=a_1+a_2
print ("Concattenation of {0} and {1} is {2}".format(a_1,a_2,c))
print (c)
#==================================================

a="praveenkumar"
print (type(a))
print (a.isalpha())
print (a.isdigit())
print ("========================================")
b="20"
print (b.isdigit())
print (b.isalpha())
#print (a.isalnum())
print("=================================")
c="praveen123"
print (c.isalnum())
print (c.isalpha())
print (c.isdigit())
#==============================================================================================================================================

a="chaitanyasanmati"
print(a.islower())
print(a.isupper())
print(a.lower())
print(a.upper())
print("======")
a_conv=a.upper()
print(a_conv)
print("original string is {0} and converted string is {1}".format(a,a_conv))
#=============================================================================================================================================


a="chaitanyasanmati"
print("_".join(a))
print(":".join(a))
print("_".join(a[0:5]))
print("_".join(a[0:5])+"--------------"+":".join(a[8:13]))
#=====================================================================================================


a="chaitanyasanmati"
print(a.replace('a',":"))
#======================================================================================================


mk=input("Enter the number\n")
print (mk)
print (type(mk))
con_mk=int(mk)
print (type(con_mk))
#===========

mk=int(input("Enter the number\n"))
print (type(mk))
print (type(mk) is int)
print (type(mk) is str)
#================


