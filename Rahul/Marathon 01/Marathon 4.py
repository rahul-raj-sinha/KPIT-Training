EtoH={'hello':'namaskar','thank you':'shukriya','see you tomorrow': 'kal milte hai'}
HtoE={'namaskar':'hello','shukriya':'thank you', 'kal milte hai' :'see you tomorrow'}

p1=""

while(p1!="bye"):
    p1 = input("Start the convo: ")
    if p1 in EtoH.keys():
        print(EtoH[p1])
    else:
        if p1 in HtoE.keys():
            print(HtoE[p1])









