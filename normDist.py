import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd
import csv
import statistics
import plotly.graph_objects as go


df=pd.read_csv("normDist.csv")

readList=df["reading score"].to_list()

rMean=statistics.mean(readList)
rMedian=statistics.median(readList)
rMode=statistics.mode(readList)

print("Mean, Median, Mode of reading score is: {}, {}, {} ".format(rMean, rMedian, rMode))

readingStandardDeviation=statistics.stdev(readList)

firstReadSTDDEV_start, firstReadSTDDEV_end=rMean-readingStandardDeviation, rMean+readingStandardDeviation
secondReadSTDDEV_start, secondReadSTDDEV_end=rMean-(2*readingStandardDeviation), rMean+(2*readingStandardDeviation)
thirdReadSTDDEV_start, thirdReadSTDDEV_end=rMean-(3*readingStandardDeviation), rMean+(3*readingStandardDeviation)


listOfDataInRead1=[result for result in readList if result>firstReadSTDDEV_start and result<firstReadSTDDEV_end]
listOfDataInRead2=[result for result in readList if result>secondReadSTDDEV_start and result<secondReadSTDDEV_end]
listOfDataInRead3=[result for result in readList if result>thirdReadSTDDEV_start and result<thirdReadSTDDEV_end]

print("Standard deviation of this data is ", readingStandardDeviation)
print("{}% of data for reading score lies within 1 standard deviation".format(len(listOfDataInRead1)*100.0/len(readList)))
print("{}% of data for reading score lies within 2 standard deviation".format(len(listOfDataInRead2)*100.0/len(readList)))
print("{}% of data for reading score lies within 3 standard deviation".format(len(listOfDataInRead3)*100.0/len(readList)))

fig=ff.create_distplot([readList], ["reading score"], show_hist=False)
fig.add_trace(go.Scatter(x=[rMean, rMean], y=[0,0.17], mode="lines", name="mean"))
fig.add_trace(go.Scatter(x=[firstReadSTDDEV_start, firstReadSTDDEV_start], y=[0,0.17], mode="lines", name="Standard Deviation 1"))
fig.add_trace(go.Scatter(x=[firstReadSTDDEV_end, firstReadSTDDEV_end], y=[0,0.17], mode="lines", name="Standard Deviation 1"))
fig.add_trace(go.Scatter(x=[secondReadSTDDEV_start, secondReadSTDDEV_start], y=[0,0.17], mode="lines", name="Standard Deviation 2"))
fig.add_trace(go.Scatter(x=[secondReadSTDDEV_end, secondReadSTDDEV_end], y=[0,0.17], mode="lines", name="Standard Deviation 2"))
fig.add_trace(go.Scatter(x=[thirdReadSTDDEV_start, thirdReadSTDDEV_start], y=[0,0.17], mode="lines", name="Standard Deviation 3"))
fig.add_trace(go.Scatter(x=[thirdReadSTDDEV_end, thirdReadSTDDEV_end], y=[0,0.17], mode="lines", name="Standard Deviation 3"))

fig.show()


