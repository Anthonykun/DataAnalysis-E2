from IPython.display import display,Markdown #,HTML
import numpy as np
from scipy import stats
from matplotlib import pyplot as plt
import pandas as pd

def descriptive( df ):
    # process dataframe:
    
    def display_title(s, pref='Figure', num=1, center=False):
        ctag = 'center' if center else 'p'
        s = f'<{ctag}><span style="font-size: 1.2em;"><b>{pref} {num}</b>: {s}</span></{ctag}>'
        if pref=='Figure':
            s = f'{s}<br><br>'
        else:
            s = f'<br><br>{s}'
        display( Markdown(s) )

    def central(x, print_output=True):
        x0     = np.mean( x )
        x1     = np.median( x )
        x2     = stats.mode( x ).mode
        return x0, x1, x2
    
    def dispersion(x, print_output=True):
        y0 = np.std( x ) # standard deviation
        y1 = np.min( x )  # minimum
        y2 = np.max( x )  # maximum
        y3 = y2 - y1      # range
        y4 = np.percentile( x, 25 ) # 25th percentile (i.e., lower quartile)
        y5 = np.percentile( x, 75 ) # 75th percentile (i.e., upper quartile)
        y6 = y5 - y4 # inter-quartile range
        return y0,y1,y2,y3,y4,y5,y6

    def display_central_tendency_table(num=1):
        display_title('Central tendency summary statistics.', pref='Table', num=num, center=False)
        df_central = df.apply(lambda x: central(x), axis=0)
        round_dict = {'price': 3, 'age': 3, 'mrt': 3, 'latitude': 3, 'longitude':3}
        df_central = df_central.round( round_dict )
        row_labels = 'mean', 'median', 'mode'
        df_central.index = row_labels
        display( df_central )
    display_central_tendency_table(num=1)

    y    = df['price']
    age = df['age']
    mrt = df['mrt']
    lat = df['latitude']
    long = df['longitude']

    fig,axs = plt.subplots( 1, 4, figsize=(10,3), tight_layout=True )
    axs[0].scatter( age, y, alpha=0.5, color='b' )
    axs[1].scatter( mrt, y, alpha=0.5, color='r' )
    axs[2].scatter( lat, y, alpha=0.5, color='g' )
    axs[3].scatter( long, y, alpha=0.5, color='y' )

    xlabels = 'Age', 'MRT', 'Latitude', 'Longitude' 
    [ax.set_xlabel(s) for ax,s in zip(axs,xlabels)]
    axs[0].set_ylabel('Price')
    [ax.set_yticklabels([])  for ax in axs[1:]]
    plt.show()

    def corrcoeff(x, y):
        r = np.corrcoef(x, y)[0,1]
        return r

    def plot_regression_line(ax, x, y, **kwargs):
        a,b   = np.polyfit(x, y, deg=1)
        x0,x1 = min(x), max(x)
        y0,y1 = a*x0 + b, a*x1 + b
        ax.plot([x0,x1], [y0,y1], **kwargs)

    fig,axs = plt.subplots( 1, 4, figsize=(10,3), tight_layout=True )
    ivs     = [age, mrt, lat, long]
    colors  = 'b', 'r', 'g', 'y'
    for ax,x,c in zip(axs, ivs, colors):
        ax.scatter( x, y, alpha=0.5, color=c )
        plot_regression_line(ax, x, y, color='k', ls='-', lw=2)
        r   = corrcoeff(x, y)
        ax.text(0.7, 0.3, f'r = {r:.3f}', color=c, transform=ax.transAxes, bbox=dict(color='0.8', alpha=0.7))

    xlabels = 'Age', 'MRT', 'Latitude',' Longitude'  
    [ax.set_xlabel(s) for ax,s in zip(axs,xlabels)]
    axs[0].set_ylabel('Price')
    [ax.set_yticklabels([])  for ax in axs[1:]]
    plt.show()



    
