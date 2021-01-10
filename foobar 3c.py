test = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]
# test = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
#%%

def solution(m):
    import numpy as np
    # get rid of self references and find terminal states
    terminal_states_set = set()
    states_dict = {}
    for i in range(len(m)):
        m[i][i]=0
        states_dict[i] = list(m[i])
        if sum(m[i])==0: terminal_states_set.add(i)
    
    # calculate probabilities with systems of linear equations
    probabilities=[]
    denominators=[]
    #loop through all terminal states
    for terminalState in terminal_states_set:
        A=[]
        b=[]
        
        #loop through the other states to get A and b
        for stateNum, stateArray in enumerate(m):
            if stateNum==terminalState: continue
        
            denominator = sum(stateArray)
            if denominator==0: denominator=1
            newA=[]
            
            #loop through the state array to get numerators
            for index,numerator in enumerate(stateArray):
                if index==stateNum:
                    newA.append(denominator)
                elif index==terminalState:
                    b.append(numerator)
                else:
                    newA.append(-numerator)
            A.append(newA)
        
        #now have A and b, calculate the probability of the terminal state = x[0]
        xdenominator=round(np.linalg.det(A))
        A=np.dot(A,1/xdenominator)
        xnumerators=np.dot(np.linalg.inv(A),b)
        for n in range(len(xnumerators)): xnumerators[n]=round(xnumerators[n])
        probabilities.append(int(xnumerators[0]))
        denominators.append(xdenominator)
    
    # return answer
    for i,n in enumerate(probabilities): probabilities[i]=round(n)
    for i,n in enumerate(denominators): denominators[i]=round(n)
    answer=list(probabilities)+[denominators[0]]
    return answer





#%%
answer=solution(test)
print(answer)