
# Define a function called plot_timeseries that plot a timeseries data.
# args:
#axes: ax of an subplot
#x: time-series index for data for the 'x' axis (datetime series)
#y: the column to plot on 'y' axis (pandas series)
#color: 'color' to use on ticks, ylabel and for the plot (str)
#xlabel: the name of xlabel (str)
#ylabel: the name of y label (str)
def plot_timeseries(axes, x, y, color, xlabel, ylabel):

  # Plot the inputs x,y in the provided color
  axes.plot(x, y, color=color)

  # Set the x-axis label
  axes.set_xlabel(xlabel)

  # Set the y-axis label
  axes.set_ylabel(ylabel, color=color)

  # Set the colors tick params for y-axis
  axes.tick_params('y', colors=color)
