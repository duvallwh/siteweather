"""
Daily Weather Forcast Graphing Module.
"""

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def format_sub_graph(ax, ylabel, ax1=None):
    """Formats each graph the same way."""
    ax.xaxis.set_minor_locator(mdates.DayLocator())
    ax.set_ylabel(ylabel)
    ax.set_xlabel('Date')
    for label in ax.get_xticklabels(which='major'):
        label.set(rotation=45, horizontalalignment='right')
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
    ax.grid(linestyle='--', which='both') 
    ax.set_title(f"Forcasted Daily {' '.join(ylabel.split(' ')[:-1])} for the Next 20 Days")
    ax.legend()
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    plt.legend(set(list(by_label.values())), set(list(by_label.keys())))
    return ax

def make_temp_graph(forcast_data, ax):
    ax.plot(forcast_data.index, forcast_data['mintemp_f'], label='Minimum Daily Temperature', color='blue')
    ax.plot(forcast_data.index, forcast_data['mintemp_f'], '.', color='blue', markersize=10)
    ax.plot(forcast_data.index, forcast_data['maxtemp_f'], label='Maximum Daily Temperature', color='green')
    ax.plot(forcast_data.index, forcast_data['maxtemp_f'], '.', color='green', markersize=10)
    ax.plot(forcast_data.index, forcast_data['avgtemp_f'], '--', color='orange', markersize=10)
    ax.plot([forcast_data.index.min(), forcast_data.index.max()], [45,45], 'r--', label='Bat Temp Threshold')
    ax = format_sub_graph(ax, 'Temperature (deg F)')
    
def make_rh_graph(forcast_data, ax):
    ax.plot(forcast_data.index, forcast_data['avghumidity'], label='Average Humidity', color='blue')
    ax.plot(forcast_data.index, forcast_data['avghumidity'], '.', color='blue')
    ax = format_sub_graph(ax, 'Humidity (%)')
    
def make_rain_and_snow_graph(forcast_data, ax):
    ax.plot(forcast_data.index, forcast_data['totalprecip_in'], label='Total Rain', color='blue')
    ax.plot(forcast_data.index, forcast_data['totalprecip_in'], '.', color='blue')
    ax.plot(forcast_data.index, forcast_data['totalsnow_cm']*0.393701, label='Total Snow', color='green')
    ax.plot(forcast_data.index, forcast_data['totalsnow_cm']*0.393701, '.', color='green')

    ax = format_sub_graph(ax, 'Snow/Rain (Inches)') 
    
def make_wind_graph(forcast_data, ax):
    ax.plot(forcast_data.index, forcast_data['maxwind_mph'], label='Maximum Windspeed', color='blue')
    ax.plot(forcast_data.index, forcast_data['maxwind_mph'], '.', color='blue')
    ax = format_sub_graph(ax, 'Maximum Wind Speed (mph)') 
    
def make_uv_graph(forcast_data, ax):
    ax.plot(forcast_data.index, forcast_data['uv'], label='UV', color='blue')
    ax.plot(forcast_data.index, forcast_data['uv'], '.', color='blue')
    ax = format_sub_graph(ax, 'UV (index)') 

def make_preds_graph(df):
    fig, axs = plt.subplots(nrows=5, figsize=(8.5, 11), sharex=True)
    make_temp_graph(df, ax=axs[0])
    make_rh_graph(df, ax=axs[1])
    make_rain_and_snow_graph(df, ax=axs[2])
    make_wind_graph(df, ax=axs[3])
    make_uv_graph(df, ax=axs[4])
    plt.tight_layout()
    return fig