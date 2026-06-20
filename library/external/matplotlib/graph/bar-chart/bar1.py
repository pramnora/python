import matplotlib.pyplot as plt         # import pyplot from matplotlib as alias, plt

# bar chart

x=["Eggs","Tomatoes","Bread","Milk"]    # x: horizontal
y=[30,8,4,2]                            # y: vertical

plt.title("Food brought this month...") # title text
plt.xlabel("Food")                      # x label
plt.ylabel("Amount")                    # y label

plt.bar(x,y)                            # draw bar chart
# plt.plot(x,y)                           # straight line graph
plt.show()                              # show bar chart
