Sessions_Attended = {'sessions' : '1011,2344,3222,44322,555,6332,721,8789,99,1011,1124,1245,137,1499'}
myvalue = Sessions_Attended.get('sessions')
#print ("value " + str(myvalue))
myvalue_split = myvalue.split(",")
#print (str(myvalue_split))
mycount = len(myvalue_split)
print ("I have attended " + str(mycount) + " sessions")

