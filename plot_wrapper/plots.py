from __future__ import annotations

from typing import Union

import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


class Plot:
    # init
    def __init__(self, labelx="x-values", labely="y-values"):
        self.plot_labelx = labelx
        self.plot_labely = labely

        # private vars
        self.array_plotx = []
        self.array_ploty = []

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
