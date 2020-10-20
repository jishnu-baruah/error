import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import csv

df1 = pd.read_csv("./sampling_111/studentMarks.csv")
dataList1 = df1["Math_score"].tolist()

fig = ff.create_distplot([dataList1], ["Math_score"], show_hist=False)
fig.show()

df2 = pd.read_csv("./sampling_111/data1.csv")
dataList2 = df2["Math_score"].tolist()

# fig2 = ff.create_distplot([dataList2], ["Math_score"], show_hist=False)
# fig2.show()

df3 = pd.read_csv("./sampling_111/data2.csv")
dataList3 = df3["Math_score"].tolist()

# fig3 = ff.create_distplot([dataList3], ["Math_score"], show_hist=False)
# fig3.show()

df4 = pd.read_csv("./sampling_111/data3.csv")
dataList4 = df4["Math_score"].tolist()

# fig4 = ff.create_distplot([dataList4], ["Math_score"], show_hist=False)
# fig4.show()


marksMean = statistics.mean(dataList1)
marksStdev = statistics.stdev(dataList1)

print("Mean of Marks: ", marksMean)
print("stdDev of Marks: ", marksStdev)


def randomSetOfMean(counter):
    dataSet = []

    for i in range(0, int(counter)):
        random_index = random.randint(0, len(dataList1)-1)
        value = dataList1[random_index]
        dataSet.append(value)

    mean = statistics.mean(dataSet)

    return mean


# def plotMean(meanList):
    df = meanList
    mean1 = statistics.mean(df)
    fig = ff.create_distplot([df], [newMeanList], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean1, mean1],
                             y=[0, 0.17], mode='lines', name='mean'))
    fig.add_trace(go.Scatter(x=[stdDevStart[0], stdDevStart[0]],
                             y=[0, 0, .17], mode='lines', name='stdDev1Start'))
    fig.add_trace(go.Scatter(x=[stdDevEnd[0], stdDevEnd[0]],
                             y=[0, 0.17], mode='lines', name='stdDev1End'))
    fig.add_trace(go.Scatter(x=[stdDevStart[1], stdDevStart[1]],
                             y=[0,  0.17], mode='lines', name='stdDev2Start'))
    fig.add_trace(go.Scatter(x=[stdDevEnd[1], stdDevEnd[1]],
                             y=[0,  0.17], mode='lines', name='stdDev2End'))
    fig.add_trace(go.Scatter(x=[stdDevStart[2], stdDevStart[2]],
                             y=[0,  0.17], mode='lines', name='stdDev3Start'))
    fig.add_trace(go.Scatter(x=[stdDevEnd[2], stdDevEnd[2]],
                             y=[0,  0.17], mode='lines', name='stdDev3End'))
    fig.show()


newMeanList = []


def setUp(counter):
    # newMeanList = []
    for i in range(0, 1000):
        setOfMeans = randomSetOfMean(counter)
        newMeanList.append(setOfMeans)

    # plotMean(newMeanList)

    # meanNewList = statistics.mean(newMeanList)
    # stDevOfNewList = statistics.stdev(newMeanList)
    print("new mean and stDev are {},{}".format(meanNewList, stDevOfNewList))


stdDevStart = []
stdDevEnd = []
setUp(100)

meanNewList = statistics.mean(newMeanList)
stDevOfNewList = statistics.stdev(newMeanList)
for i in range(0, 3):
    i = i+1
    valueStart, valueEnd = meanNewList - \
        (i*stDevOfNewList), meanNewList+(i*stDevOfNewList)
    stdDevStart.append(valueStart)
    stdDevEnd.append(valueEnd)

print(newMeanList)
fig = ff.create_distplot([newMeanList], ['Math_score'], show_hist=False)
fig.add_trace(go.Scatter(x=[meanNewList, meanNewList],
                         y=[0, 0.17], mode='lines', name='mean'))
fig.add_trace(go.Scatter(x=[stdDevStart[0], stdDevStart[0]],
                         y=[0, 0.17], mode='lines', name='stdDev1Start'))
fig.add_trace(go.Scatter(x=[stdDevEnd[0], stdDevEnd[0]],
                         y=[0, 0.17], mode='lines', name='stdDev1End'))
fig.add_trace(go.Scatter(x=[stdDevStart[1], stdDevStart[1]],
                         y=[0,  0.17], mode='lines', name='stdDev2Start'))
fig.add_trace(go.Scatter(x=[stdDevEnd[1], stdDevEnd[1]],
                         y=[0,  0.17], mode='lines', name='stdDev2End'))
fig.add_trace(go.Scatter(x=[stdDevStart[2], stdDevStart[2]],
                         y=[0,  0.17], mode='lines', name='stdDev3Start'))
fig.add_trace(go.Scatter(x=[stdDevEnd[2], stdDevEnd[2]],
                         y=[0,  0.17], mode='lines', name='stdDev3End'))
fig.show()


# plotMean(newMeanList, "Math_score")

# setUp(dataList, 100, "Math_score")
# setUp(dataList2, 100, "Math_score")
# setUp(dataList3, 100, "Math_score")
# setUp(dataList4, 100, "Math_score")

# firtstStdStart, firtstStdEnd = meanHeight - \
#     marksStdev, meanHeight+marksStdev
# secondStdStartH, secondStdEndH = meanHeight - \
#     (2*marksStdev), meanHeight+(2*marksStdev)
# thirdStdStartH, thirdStdEndH = meanHeight - \
#     (3*marksStdev), meanHeight+(3*marksStdev)


# fig = ff.create_distplot([newMeanList], ["Math_score"], show_hist=False)
# fig.add_trace(go.Scatter(x=[mean1, mean1],
#                          y=[0, 1], mode='lines', name='mean'))
# fig.show()
