import matplotlib.pyplot as plt
import numpy as np
from process import *
from tui import *
import matplotlib.animation as ani

"""

This module is responsible for visualising the data using Matplotlib.
"""

"""
Task 22 - 24: Write suitable functions to visualise the data as follows:

- Display the number of confirmed cases per country/region using a pie chart
- Display the top 5 countries for deaths using a bar chart
- Display a suitable (animated) visualisation to show how the number of confirmed cases, deaths and recovery change over
time. This could focus on a specific country or countries.

Each function should visualise the data using Matplotlib.
"""

# TODO: Your code here
def pychart_22(covid_records,countries):
    confirmed_plot1 = []
    confirmed_plot2 = []
    for country in countries:
        confirmed1 = 0
        confirmed2 = 0
        recovered = 0
        deads = 0
        for record in covid_records:
            if record[3] == country:
                confirmed1 += int(record[5])
            if record[3] == country and country != "Mainland China":
                confirmed2 += int(record[5])
        confirmed_plot1.append(confirmed1)
        if country != "Mainland China":
            confirmed_plot2.append(confirmed2)
    countries_strings1 = list(countries)
    countries_strings2 = countries_strings1.copy()
    countries_strings2.remove("Mainland China")
    fig, (ax1,ax2) = plt.subplots(1,2)
    ax1.pie(confirmed_plot1,labels=countries_strings1)
    ax2.pie(confirmed_plot2,labels = countries_strings2 )
    ax1.legend(loc='best',fontsize=7, bbox_to_anchor=(0.3, 0.2, 0.2, 0.7))
    ax2.legend(loc='best', fontsize=7, bbox_to_anchor=(0.8, 0.2, 0.7, 0.7))
    plt.show()

def observation_chart_23 (covid_records,countries) :
   topdeads = []
   for country in countries:
       deads = 0
       for record in covid_records:
           if record[3]==country:
               deads += int(record[6])
       topdeads.append({country : deads })
   xlist = list(countries)

   ylist = []
   for d in topdeads:
       for value in d.values():
        ylist.append(value)
   z = list(zip(xlist,ylist))
   z = sorted(z,reverse=True,key=lambda x:x[1])[0:5]
   print(z)
   fig , ax = plt.subplots()
   ax.bar(xlist,ylist)
   plt.show()







class Animator:
    all_deads = []
    all_confirmed = []
    all_recovery = []
    xdata = []
    ydata = []
    xlist = []
    records = []
    def __init__(self,covid_records):
        self.records = covid_records.copy()
        xlist = [int(record[0]) for record in covid_records if record[3] == 'Mainland China']
        deads = 0
        confirmed = 0
        recovery = 0
        for x in xlist:
            for record in covid_records:
                if int(record[0]) == x:
                    deads += int(record[6])
                    confirmed += int(record[5])
                    recovery += int(record[7])
                    self.all_deads.append(deads)
                    self.all_confirmed.append(confirmed)
                    self.all_recovery.append(recovery)
        self.n = len(self.all_deads)
        self.xlist = list(range(self.n))
        self.fig = plt.figure()
        self.axis = plt.axes(xlim=(0,self.n),ylim =(0,40000))
        self.line_dead, = self.axis.plot([],[],"b",lw = 3)
        self.line_confirmed, = self.axis.plot([], [], 'r', lw=3)
        self.line_recovery, = self.axis.plot([],[],"g",lw=3)
    def anim__init__(self):
        self.line_dead.set_data([],[])
        self.line_confirmed.set_data([], [])
        self.line_recovery.set_data([], [])
    def animate(self,idx):
        x = self.xlist[0:idx]
        y1 = self.all_deads[0:idx]
        y2 = self.all_confirmed[0:idx]
        y3 = self.all_recovery[0:idx]
        self.line_dead.set_data(x, y1)
        self.line_confirmed.set_data(x, y2)
        self.line_recovery.set_data(x, y3)
    def run(self):
        anim = ani.FuncAnimation(self.fig, self.animate, init_func=self.anim__init__, frames=self.n, interval=100)
        plt.show()



def animated_summary_24(covid_records,countries):



    animator = Animator(covid_records)
    animator.run()

