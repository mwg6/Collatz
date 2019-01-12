import matplotlib.pyplot as plt
import time

start_time = time.time()
highest_analyzed = 10500000
start =1
hold=0
hold_num =0
hold_length=0
store = dict()

#plt.axis([0,highest_analyzed,0,500])

while start<=highest_analyzed:

    results = 0
    
    hold = start
    while hold!=1:

        results+=1

        if hold%2==1:
        
            hold=3*hold+1
            
        else:
            
            hold = hold/2
    
        if hold in store:
            results +=store[hold]
            hold=1
    
    if results>hold_length:
        hold_num=start
        hold_length = results

    
    if not start in store:
        store[start] = results
  
    #plt.scatter(start,results)
    
    if start%(highest_analyzed/10)==0:
        print(" " + str(start/(highest_analyzed/100)) + " percent done!")
        
    start+=1

print("--- %s seconds ---" % (time.time() - start_time))
#plt.show()

print(hold_num)
print(hold_length)