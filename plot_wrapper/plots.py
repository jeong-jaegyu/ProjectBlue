from __future__ import annotations
from typing import Union
import multiprocessing

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


class Plot:
    # init
    def __init__(self, labelx="x-values", labely="y-values", is_multproc=False):
        # private vars
        self.plot_labelx = labelx
        self.plot_labely = labely
        self.array_plotx = []
        self.array_ploty = []

        # This is used solely to display multiple graphs. Make a function for each graph definition and call it with
        # multiprocessing to increase speed.
        if is_multproc:
            self.is_multproc = True
            self.multproc = multiprocessing.Process(target=self.disp_plot)

    # methods
    def disp_plot(self):
        plt.ylabel(self.plot_labely)
        plt.xlabel(self.plot_labelx)
        plt.plot(self.array_plotx, self.array_ploty)
        plt.show()

    def add_x(self, value: Union[int, float]):
        self.array_plotx.append(value)

    def add_y(self, value: Union[int, float]):
        self.array_ploty.append(value)

    def set_x(self, xlist: list[int, float]):
        self.array_plotx = xlist

    def set_y(self, ylist: list[int, float]):
        self.array_ploty = ylist
