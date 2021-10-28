import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy


# plt.plot([1, 2, 3, 4]) <-- requires "container"
# plt.ylabel('some numbers') <-- function
# plt.show() <-- end of function(??)


class Plot:
    # init
    def __init__(self, labelx="x-values", labely="y-values"):
        self.plot_labelx = labelx
        self.plot_labely = labely

    # private vars
    array_plotx = []
    list_ploty = []

    # methods
    def disp_plot(self, plot_label,
                  list_plotx, list_ploty):
        plt.plot

        plt.ylabel(self.plot_labelx)
        plt.xlabel(self.plot_labely)
        plt.show()
