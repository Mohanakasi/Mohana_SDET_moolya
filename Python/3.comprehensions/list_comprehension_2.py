'''''''"""traversing through using list comprehension"""'''
# list_ = ['kasi',1008,'jmr',2020]
# res = [item for item in list_]
# print(res)

# list_ = ['kasi',1008,'jmr',2020]
# res = [list_[index] for index in range(len(list_))]
# print(res)

""""**************************************************************************"""
"""wap to print index and it's corresponding element using list comprehension"""
"""#********************************************************************************"""
"""wap to reverse the elements in the list using list comprehension"""
# list_ = ['kasi','python',1008,'happy']
# res = [item for item in reversed(list_)]
# print(res)
#
# list_ = ['kasi','python',1008,'happy']
# res = [list_[index] for index in range(-1,-(len(list_)+1),-1)]
# print(res)
#
# list_ = ['kasi','python',1008,'happy']
# res = [item for item in list_[::-1]]
# print(res)
"""*********************************************************************************"""
"""wap to preint alternate elements (even)"""
# list_ = ['python',1.58,True,'kasi','laguage0']
# res = [list_[index] for index in range(0,len(list_),2)]
# print(res)
#
# list_ = ['python',1.58,True,'kasi','laguage0']
# res = [list_[index] for index in range(len(list_)) if index % 2 == 0]
# print(res)
#
# list_ = ['python',1.58,True,'kasi','laguage0']
# res = [item for item in list_[::2]]
# print(res)
#
# list_ = ['python',1.58,True,'kasi','laguage0']
# res = [item for index,item in enumerate(list_) if index %2 == 0]
# print(res)
"""**************************************************************************"""
"""wap to print alternate elements (odd)"""
# list_ = ['python',1.58,True,'kasi','laguage0','kil']
# res = [list_[index] for index in  range(len(list_)) if index % 2 !=0]
# print(res)
#
# list_ = ['python',1.58,True,'kasi','laguage0','kil']
# res = [list_[index] for index in  range(1,len(list_),2)]
# print(res)
#
# list_ = ['python',1.58,True,'kasi','laguage0','kil']
# res = [item for item in list_[1:len(list_):2]]
# print(res)
#
# list_ = ['python',1.58,True,'kasi','laguage0','kil']
# res = [item for index,item in enumerate(list_) if index % 2 != 0]
# print(res)

"""**********************************************************************************"""
"""wap to print only integers in a list"""
# list_ = ['kasi', 2021 , 'python' , 1008, 50200037008003 , 'test yanthra', 2022]
# res = [item for item in list_ if isinstance(item,int)]
# print(res)
#
# res = [item for item in list_ if type(item) == int]
# print(res)
#
# res = [list_[index] for index in range(len(list_)) if isinstance(list_[index],int)]
# print(res)
#
# res = [list_[index] for index in range(len(list_)) if type(list_[index]) == int]
# print(res)
""""******************************************************************************************"""
"""wap to print iterable with it's length"""
# list_ = ['kasi','python', [1,2,3,'kasi'],{458,25,'a'},{'a':1,'b':1},('py','by'),True,1.8,10087]
# res = [(item,len(item)) for item in list_ if isinstance(item,(str,list,tuple,set,dict))]
# print(res)
#
# list_ = ['kasi','python','laguage','oops','iam']
# res = [(list_[index],len(list_[index])) for index in range(len(list_))]
# print(res)
#
# res = [(item,len(item)) for item in list_]
# print(res)

"""*********************************************************************************************"""
"""wap to print strings in list which are of even length"""
# list_ = ['mohan','kasi','is','a','king','before','guntur','minister']
# res = [item for item in list_ if len(item) % 2 == 0]
# print(res)
#
# res = [list_[index] for index in range(len(list_)) if len(list_[index]) % 2 == 0]
# print(res)

""""*********************************************************************************************"""
"""wap to print strings in the list if the string is of even lenth keepit as it is if it is odd lenth reverse it"""
# list_ = ['kasi','python', 'has','00a','inbuilt','modules','and','oops']
# res = [item if len(item) % 2 == 0 else item[::-1] for item in list_]
# print(res)
#
# res = [list_[index] if len(list_[index]) % 2 == 0 else list_[index] [::-1] for index in range(len(list_))]
# print(res)
""""*********************************************************************************************"""
"""wap to reverse the element if it is of type string elser keep it as it is (using list comprehension)"""
# list_ = ['kasi',True,1008,False,2021,'python','jmr',[1,4,0,80]]
# res = [item[::-1] if isinstance(item,str) else item for item in list_]
# print(res)
#
# res = [item[::-1] if type(item) == str else item for item in list_]
# print(res)
#
# res = [list_[index][::-1] if isinstance(list_[index],str) else list_[index] for index in range(len(list_))]
# print(res)

"""***********************************************************************************************"""
# list_ = ['kasi',"iam a king",'us','orange']
# res = [item for item in list_ if isinstance(item, str) and item[0].lower() in 'aeiou']
# print(res)
#
# res = [list_[index] for index in range(len(list_)) if list_[index][0].lower() in 'aeiou']
# print(res)

""""**********************************************************************************************"""
"""wap to print all the palindrome in a list"""
# list_ = ['mom','is','better','then','malayalam','dad']
# res = [item for item in list_ if item == item[::-1]]
# print(res)
#
# res = [list_[index] for index in range(len(list_)) if list_[index] == list_[index][::-1]]
# print(res)
