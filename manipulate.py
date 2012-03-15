from __future__ import division
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider

# TODO is dict.items() guaranteed to give the values in the same order as
# dict.values()? I assume it does :)
# TODO have this export to a javascript format too!
# TODO make it take a plotting function other than plt.plot, have *args be the
# 'data' stuff
# TODO make mplot work more like plot: use *args, assume a function list

bottom_pad = 0.1
per_slider = 0.05
bgcolor = 'lightgoldenrodyellow'

def mplot(func,x,**kwargs):
    num_params = len(kwargs)

    fig = plt.figure()
    main_ax = fig.add_subplot(111)
    fig.subplots_adjust(bottom=bottom_pad + (num_params+1)*per_slider)

    param_vals = dict((param_name,(lo+hi)/2) for param_name, (lo,hi) in kwargs.items())
    y = func(x,**param_vals)
    l, = main_ax.plot(x,y)

    def update(*args):
        for param_name, slider in zip(param_vals,sliders):
            param_vals[param_name] = slider.val
        vals = func(x,**param_vals)
        l.set_ydata(vals)

        # using autoscale_view makes the axes shrink *and* grow
        #main_ax.relim()
        #main_ax.autoscale_view()
        # setting ylim this way only lets the axes grow
        ymin, ymax = main_ax.get_ylim()
        main_ax.set_ylim(min(vals.min(),ymin),max(ymax,vals.max()))

        fig.canvas.draw()

    sliders = []
    for idx, (param_name, (lo,hi)) in enumerate(kwargs.items()):
        ax = fig.add_axes([0.25,bottom_pad+per_slider*idx,0.65,3/5*per_slider],axisbg=bgcolor)
        slider = Slider(ax, param_name, lo, hi, valinit=param_vals[param_name])
        slider.on_changed(update)
        sliders.append(slider)

    plt.axes(main_ax)

# test stuff below here
from functools import partial

def mplot_slow(func,x,**kwargs):
    def plot_func(x,axes,kwdict):
        plt.plot(x,func(x,**kwdict),axes=axes)
    from_partial(partial(plot_func,x),**kwargs)

def from_partial(plot_func,**kwargs):
    num_params = len(kwargs)

    fig = plt.figure()
    main_ax = fig.add_subplot(111)
    fig.subplots_adjust(bottom=bottom_pad + (num_params+1)*per_slider)

    param_vals = dict((param_name,(lo+hi)/2) for param_name, (lo,hi) in kwargs.items())
    plot_func = partial(plot_func,main_ax)
    plot_func(param_vals)

    def update(*args):
        for param_name, slider in zip(param_vals,sliders):
            param_vals[param_name] = slider.val
        main_ax.cla()
        plot_func(param_vals)

        # using autoscale_view makes the axes shrink *and* grow
        main_ax.relim()
        main_ax.autoscale_view()

        fig.canvas.draw()

    sliders = []
    for idx, (param_name, (lo,hi)) in enumerate(kwargs.items()):
        ax = fig.add_axes([0.25,bottom_pad+per_slider*idx,0.65,3/5*per_slider],axisbg=bgcolor)
        slider = Slider(ax, param_name, lo, hi, valinit=param_vals[param_name])
        slider.on_changed(update)
        sliders.append(slider)

    plt.axes(main_ax)

