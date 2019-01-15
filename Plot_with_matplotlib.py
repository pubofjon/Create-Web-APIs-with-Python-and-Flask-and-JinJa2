# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np
import datetime as datetime
import pandas_datareader.data as web
from pandas_datareader import data, wb
import sys, os
import sqlite3 as db
import pandas.io.sql as pd_sql

import matplotlib.pyplot as plt

def plot_base(q_date, ticks='', do=''): #ticks =['x','y'], do(unop)
    import plotly.plotly as plty
    import plotly.graph_objs as plgo
    import matplotlib.pyplot as plt
    from matplotlib.finance import candlestick2_ohlc as cdl
    from matplotlib.dates import DateFormatter, WeekdayLocator, DayLocator, MONDAY
    import matplotlib.ticker as mticker
    import matplotlib.dates as mdates
    mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
    alldays = DayLocator()              # minor ticks on the days
    weekFormatter = DateFormatter('%b %d')  # e.g., Jan 12
    dayFormatter = DateFormatter('%d')      # e.g., 12
    import pylab
    import matplotlib
    matplotlib.use('TkAgg')
#    %matplotlib inline
    ticks = [x.upper() for x in ticks]

    p_date=q_date-datetime.timedelta(100)

    qry="SELECT * FROM tbl_pv  wHERE date BETWEEN '%s' AND '%s'" %(p_date, q_date)
    dp=read_sql(qry,q_date)
    pd.set_option('display.expand_frame_repr', False)
    for t in ticks:
        if t in dp.ticker.unique():
            dt=dp[dp.ticker == t]
            dt=dt.sort_values('date', ascending=True)
            dt=dt.tail(80)
            dt['date']=dt['date'].astype(str).apply(lambda x: x[:10])
            dt['date']=pd.to_datetime(dt['date'],format='%Y-%m-%d')# %H:%M:%S.%f')
    #        dt=dt[['date', 'close','volume']]
            dt['date']=dt['date'].map(mdates.date2num)
            dt=dt[['date','open','close','high','low','volume']]
            fig=plt.figure()
            ax1=plt.subplot2grid((5,4),(0,0),rowspan=4, colspan=4)
            plt.xlabel("date")
            cdl(ax1,dt['open'],dt['high'], dt['low'], dt['close'], width=0.6)
            plt.ylabel('stk price')
            plt.legend()

            plt.show()
           
            ax2=plt.subplot2grid((5,4),(4,0), sharex=ax1, rowspan=1, colspan=4)
            ax2.bar(dt.index,dt['volume'])
            ax2.axes.yaxis.set_ticklabels([])
            plt.subplots_adjust(hspace=0)
            plt.show()
            
#            fig.autofmt_xdate()
    pd.set_option('display.expand_frame_repr', True)  

ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
         'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
         'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
         'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
         'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)

def p1():
    import matplotlib.ticker as ticker
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    import pandas as pd
    import pandas.io.sql as pd_sql
    
    conn=sq3.connect(r'c:\Users\qli1\BNS_wspace\flask\f_trd\trd.db')
    df=pd_sql.read_sql("SELECT * FROM tbl_price_etf", conn)
    conn.close()
    df=df[['date','SPY']]
    df['date'] = pd.to_datetime(df['date'])#, unit='s')
    df['mdate'] = [mdates.date2num(d) for d in df['date']]
    df.set_index('date')

    fig, ax = plt.subplots()
    ax.plot(df['SPY'],'-')
    
#    formatter = ticker.FormatStrFormatter('$%1f')
#    ax.yaxis.set_major_formatter(formatter)
#    daysFmt = mdates.DateFormatter("'%d")
#    days = mdates.DayLocator() 
#    ax.xaxis.set_major_locator(mdates.YearLocator())
#    ax.xaxis.set_minor_locator(mdates.MonthLocator())
#  
#    yearFmt = mdates.DateFormatter("'%y")
#    ax.xaxis.set_major_formatter(yearFmt)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.xticks(rotation=60)
    
#    for tick in ax.yaxis.get_major_ticks():
#        tick.label1On = False
#        tick.label2On = True
#        tick.label2.set_color('green')
    plt.legend(loc='best')
    plt.xlabel('date')
    plt.ylabel('value')
    plt.title('demo')
    plt.tight_layout()
#    ax.set_xlime(0,10)
    plt.show()
    
def p2():
    fig5 = plt.figure(constrained_layout=True)
    widths = [2, 3, 1.5]
    heights = [1, 3, 2]
    spec5 = fig5.add_gridspec(ncols=3, nrows=3, width_ratios=widths,
                              height_ratios=heights)
    for row in range(3):
        for col in range(3):
            ax = fig5.add_subplot(spec5[row, col])
            label = 'Width: {}\nHeight: {}'.format(widths[col], heights[row])
            ax.annotate(label, (0.1, 0.5), xycoords='axes fraction', va='center')
    
def p3():
    gs_kw = dict(width_ratios=widths, height_ratios=heights)
    fig6, f6_axes = plt.subplots(ncols=3, nrows=3, constrained_layout=True,
            gridspec_kw=gs_kw)
    for r, row in enumerate(f6_axes):
        for c, ax in enumerate(row):
            label = 'Width: {}\nHeight: {}'.format(widths[c], heights[r])
            ax.annotate(label, (0.1, 0.5), xycoords='axes fraction', va='center')
            
            

def p4_blend():
    import matplotlib.transforms as transforms
    import matplotlib.patches as mpatches
    fig, ax = plt.subplots()
    x = np.random.randn(1000)
    
    ax.hist(x, 30)
    ax.set_title(r'$\sigma=1 \/ \dots \/ \sigma=2$', fontsize=16)
    
    # the x coords of this transformation are data, and the
    # y coord are axes
    trans = transforms.blended_transform_factory(
        ax.transData, ax.transAxes)
    
    # highlight the 1..2 stddev region with a span.
    # We want x to be in data coordinates and y to
    # span from 0..1 in axes coords
    rect1 = mpatches.Rectangle((-2, 0), width=1, height=1,
                             transform=trans, color='orange',
                             alpha=0.5)
    rect2 = mpatches.Rectangle((1, 0), width=1, height=1,
                             transform=trans, color='yellow',
                             alpha=0.5)    
    ax.add_patch(rect1)
    ax.add_patch(rect2)    
    plt.show()
    


    