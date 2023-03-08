import folium

from branca.element import Template, MacroElement

from .legend import compile_legend

def plot_point(map_figure, point, icon_path, icon_square_size=6):
    
    """
    Takes a point and plots it on a folium map.
        
        args: map_figure(folium.folium.Map) - map to plot point on.
              point(list) - [lat, lon] of point.
              icon_path(str) - path to icon to use for point.

        returns: kml_df(pd.DataFrame) - df with row for each landmark from kml file.
    """
    
    icon = folium.features.CustomIcon(icon_path,icon_size=(icon_square_size, icon_square_size))
    folium.Marker(location=point,icon=icon).add_to(map_figure)
    return map_figure


def available_mesonet_data(lat, lon, data_dict):   
    m = folium.Map(location=(lat, lon), zoom_start=11, zoom_control=False)
    m = plot_point(m, (lat, lon), os.path.join(ICON_PATH, "light_blue_circle.png"), icon_square_size=10)
    for s in data_dict['STATION']:
    #     print(s)
        if s['STATUS'] == 'INACTIVE':
            m = plot_point(m, (s['LATITUDE'], s['LONGITUDE']), os.path.join(ICON_PATH, "yellow_circle.png"), icon_square_size=10)

        if s['STATUS'] == 'ACTIVE':
            m = plot_point(m, (s['LATITUDE'], s['LONGITUDE']), os.path.join(ICON_PATH, "orange_circle.png"), icon_square_size=10)
            
    template = compile_legend({'icon':[['siteweather/icons/light_blue_circle.png', 'Analysis Location'],
                                    ['siteweather/icons/orange_circle.png', 'Active Weather Station'],
                                    ['siteweather/icons/yellow_circle.png', 'Inactive Weather Station']]})

    macro = MacroElement()
    macro._template = Template(template)

    m.get_root().add_child(macro)
    return m