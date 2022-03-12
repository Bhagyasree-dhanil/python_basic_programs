'''

Binary search algorith using recursion

1.sort in ascending order
2.find the middle index value(len/2) check whether it is a=same, greater or lower
   if same-then value found 
   if greater -take values of list [previous middle index :len(list)]
   if smaller -take values of list [0 : previous middle index]
3 .Repeat the process until the len of list array is zero.

'''


def binary_search(s_list,s_string):
   
    
   if len(s_list)==0:
      
      print("No string found")
      return 
   
   first=0
   last=len(s_list)-1

  

   mid_value=int((first+last)/2)
   if s_list[mid_value]==s_string:
      
      print("found string",s_string)
   
   if s_list[mid_value]<s_string:
      first=mid_value+1
      last=len(s_list)
      binary_search(s_list[first:last],s_string)
   
   if s_list[mid_value]>s_string:
      first=1
      last=mid_value
      binary_search(s_list[first:last],s_string)
  
#----execute----
search_array=[2,4,8,9,5]
search_array.sort()
value=10
binary_search(search_array,value)
