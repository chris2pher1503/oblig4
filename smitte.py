# -*- coding: utf-8 -*-
"""Created on 20.10.2023"""
__author__ = "Christopher Ljosland Strand"
__email__ = "christopher.ljosland.strand@nmbu.no"
import csv
import matplotlib.pyplot as plt 

#funksjonoen regner ut neste dag sine SIR verdier. 
def updateSIR(s_y, i_y, r_y, b, k):
    s = s_y - b * s_y * i_y
    i = i_y + b * s_y * i_y - k * i_y
    r = r_y + k * i_y
    return s, i, r


#koden starter her
def main(): 
    # konstanter
    b = 1/3
    k = 1/10

    # startsverdier
    s = 1
    i = 10/(5*10**6)
    r = 0
    
    grafS = [1]
    grafI = [10/(5*10**6)]
    grafR = [0]
    dager= [0]
#skriver til csv filen
    with open('pan.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([f"{'Day':<18}", f"{'S@day':<18}", f"{'I@day':<18}", f"{'R@day':<18}"])
        writer.writerow([1, "{:15.3e}".format(s), "{:15.3e}".format(i), "{:15.3e}".format(r)])

        for day in range(120):
            days = day + 1
            s, i, r = updateSIR(s, i, r, b, k)
            grafS.append(s)
            grafI.append(i)
            grafR.append(r)
            dager.append(days)
            writer.writerow([days, "{:15.3e}".format(s), "{:15.3e}".format(i), "{:15.3e}".format(r)])

    #plotter grafen (oppgaven sier simuler, vet ikke om man da også skal plotte)
    plt.figure(figsize=(10, 6))  
    plt.plot(dager, grafS, label="S", color='blue')
    plt.plot(dager, grafI, label="I", color='red')
    plt.plot(dager, grafR, label="R", color='green')

    plt.xlabel('Dayer')
    plt.ylabel('Personer')
    plt.title('SIR Modell')
    plt.legend()  
    plt.grid(True)  
    plt.tight_layout()  
    plt.show()
    

if __name__ == "__main__":
    main()
