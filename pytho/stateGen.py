# "i" : [["i+1",i%100], ["i-1",(100-i)%100]],
for i in range(100):
    print('"' , i , '" : [["' , int(i+1) , '", ' , int(i%100) ,
          '], ["', int(i-1),'", ' , int((100-i)%100),']],')
