import matplotlib as mpl

def set_plot_style():
    '''
    Sets the common Matplotlib styles for the CMSC 6950 Final Project.
    '''
    
    mpl.rcParams['font.family'] = 'serif'
    mpl.rcParams['font.size'] = 14
   
    mpl.rcParams['figure.figsize'] = [8, 5]
    
    
    mpl.rcParams['axes.grid'] = True
    mpl.rcParams['grid.linestyle'] = '--'
    mpl.rcParams['grid.alpha'] = 0.6
    
    mpl.rcParams['lines.linewidth'] = 2.0
    
    mpl.rcParams['lines.markersize'] = 8
    
    
    mpl.rcParams['savefig.dpi'] = 300
    mpl.rcParams['savefig.bbox'] = 'tight'
    
    mpl.rcParams['legend.fontsize'] = 'medium'
    mpl.rcParams['legend.frameon'] = False