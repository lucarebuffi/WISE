__author__ = 'labx'

import sys

try:
    import matplotlib
    import matplotlib.pyplot as plt
    from matplotlib import cm
    from matplotlib import figure as matfig
    import pylab
except ImportError:
    print(sys.exc_info()[1])
    pass

class WisePlot:

    @classmethod
    def plot_histo(cls, plot_window, x, y, title, xtitle, ytitle):
        matplotlib.rcParams['axes.formatter.useoffset']='False'

        plot_window.addCurve(x, y, title, symbol='', color='blue', replace=True) #'+', '^', ','
        if not xtitle is None: plot_window.setGraphXLabel(xtitle)
        if not ytitle is None: plot_window.setGraphYLabel(ytitle)
        if not title is None: plot_window.setGraphTitle(title)
        plot_window.setInteractiveMode(mode='zoom')
        plot_window.resetZoom()
        plot_window.replot()
