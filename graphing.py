import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def graph_forcast_data(forcast_data, lat, lon):
    _, ax = plt.subplots(figsize=(10, 5))
    ax.plot(forcast_data['date'], forcast_data['mintemp_f'], label='Minimum Daily Temperature', color='blue')
    ax.plot(forcast_data['date'], forcast_data['mintemp_f'], '.', color='blue', markersize=10)
    ax.plot([forcast_data['date'].min(), forcast_data['date'].max()], [45,45], 'r--', label='Bat Temp Threshold')
    ax.xaxis.set_minor_locator(mdates.DayLocator())
    ax.set_ylabel('Temperature (F)')
    ax.set_xlabel('Date')
    ax.legend()
    ax.set_title(f'Minimum Daily Temperature (F) for the Next 20 Days ({lat:.3f}, {lon:.3f})')
    for label in ax.get_xticklabels(which='major'):
        label.set(rotation=45, horizontalalignment='right')
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
    ax.grid(linestyle='--')
    return ax