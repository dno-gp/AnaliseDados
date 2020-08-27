from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral9 
from bokeh.plotting import figure

local = ["1","5", "6", "7"]
qtd = [4,6,8,2]

def graph(ex, ey):
    source = ColumnDataSource(data=dict(ex=ex, ey=ey))
    p = figure(title="", plot_width= 400, plot_height=400,
                x_range=ex)

    p.vbar(x='ex', top='ey', width=0.9, source=source)
    show(p)

if __name__=='__main__':
    graph(local, qtd)