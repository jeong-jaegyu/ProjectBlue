
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

import plot_wrapper.plots as plots


if __name__ == '__main__':
    blue = plots.Plot(labelx="Calories Burnt", labely="Distance Ran", is_multproc=True)
    blue.set_x([0, 2, 4, 8, 10])
    blue.set_y([10, 20, 30, 40, 50])
    #blue.disp_plot()

    red = plots.Plot(labelx="Time", labely="Distance", is_multproc=True)
    red.set_x([1, 2, 3, 4, 5])
    red.set_y([10, 20, 30, 40, 50])
    #red.disp_plot()

    red.multproc.start()
    blue.multproc.start()

    red.multproc.terminate()
    blue.multproc.terminate()
