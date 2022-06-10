from tui import *
from process import *
from main import *

def observation_chart_23():
    thisdict = {"countries" : [] , "deads" : [] }
    for i,j in covid_records[3],[6]:
        thisdict["countries"].append(i)
        thisdict["deads"].append(j)
    print(thisdict)
observation_chart_23()
