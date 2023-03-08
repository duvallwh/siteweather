""" Module containing legend implementation """

template_start = """
{% macro html(this, kwargs) %}

<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>jQuery UI Draggable - Default functionality</title>
  <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">

</head>
<body>

<div id='maplegend' class='maplegend' 
    style='position: absolute; z-index:9999; border:2px solid black; background-color:rgba(255, 255, 255, 1);
     border-radius:6px; padding: 10px; font-size:14px; right: 20px; bottom: 20px;'>
     
<div class='legend-title'>Legend</div>
<div class='legend-scale'>
  <ul class='legend-labels'> """


template_end = """
  </ul>
</div>
</div>
<div id='northarrow' 
    style='position: absolute; z-index:9999; 
     border-radius:6px; padding: 10px; font-size:14px; right: 30px; top: 30px;'>
    <img style=float: center; padding: 15px 0px 0px 15px" src="agne_code/icons/north_arrow.png" width="40" height="80">
</div>
</body>
</html>

<style type='text/css'>
  .maplegend .legend-title {
    text-align: left;
    margin-bottom: 5px;
    font-weight: bold;
    font-size: 95%;
    }
  .maplegend .legend-scale ul {
    margin: 0;
    margin-bottom: 5px;
    padding: 0;
    float: left;
    list-style: none;
    }
  .maplegend .legend-scale ul li {
    font-weight: bold;
    font-size: 85%;
    list-style: none;
    margin-left: 0;
    line-height: 18px;
    margin-bottom: 2px;
    }
  .maplegend ul.legend-labels li span {
    display: block;
    float: left;
    height: 16px;
    width: 30px;
    margin-right: 5px;
    margin-left: 0;
    border: 1px solid #000000;
    }
   .maplegend ul.legend-labels li img {
    display: block;
    float: left;
    height: 16px;
    width: 16px;
    margin-right: 13px;
    margin-left: 7px;
    }
  .maplegend .legend-source {
    font-size: 80%;
    color: #000000;
    clear: both;
    }
  .maplegend a {
    color: #000000;
    }
</style>
{% endmacro %}"""

def add_span(color, label):
    """
    Creates a span with color and label for legend
    """
    return f"<li><span style='background:{color};opacity:1;padding-top:3px'></span>{label}</li>"

def add_icon(icon, label):
    """
    Creates an icon with label for legend
    """
    return f"""<li>
        <img src="{icon}" width="8" height="8">
        {label}
    </li>"""
    
def compile_legend(legend_dict):
    """
    Creates a legend from a dictionary of labeled lists of colors and labels for 
    each span entry. Also, creates a legend for icons from path and labels.

    legend_dict = {
        'span' = [[color, label], [color, label], ...],
        'icon' = [[icon, label], [icon, label], ...]
    }
    """
    legend = template_start
    for key, value in legend_dict.items():
        if key == "span":
            for span in value:
                legend += add_span(span[0], span[1])
        elif key == "icon":
            for icon in value:
                legend += add_icon(icon[0], icon[1])
    legend += template_end
    return legend


