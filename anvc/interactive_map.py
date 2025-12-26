import geopandas as gpd
import pandas as pd
import unidecode
from bokeh.io import show
from bokeh.models import GeoJSONDataSource, LinearColorMapper, ColorBar, HoverTool, Select, CustomJS
from bokeh.plotting import figure
from bokeh.palettes import OrRd9
from bokeh.layouts import column

def clean_text(text):
    if not isinstance(text, str): 
        return ""
    return unidecode.unidecode(text).upper().replace("'", "").replace("-", " ").strip()

def show_election_map(geojson_url=None, csv_url=None):
    if geojson_url is None:
        geojson_url = "https://github.com/wmgeolab/geoBoundaries/raw/main/releaseData/gbOpen/MRT/ADM2/geoBoundaries-MRT-ADM2.geojson"
    if csv_url is None:
        csv_url = "https://raw.githubusercontent.com/binorassocies/rimdata/refs/heads/main/data/results_elections_rim_2019-2024.csv"

    gdf = gpd.read_file(geojson_url).to_crs(epsg=3857)
    gdf['moughataa_key'] = gdf['shapeName'].apply(clean_text)

    df_2024 = pd.read_csv(csv_url).query("year == 2024").copy()
    df_2024['moughataa_key'] = df_2024['moughataa'].apply(clean_text)

    df_pivot = df_2024.pivot_table(index='moughataa_key', columns='candidate', values='nb_votes', aggfunc='sum').fillna(0)
    candidats = sorted(df_pivot.columns.tolist())

    merged = gdf.merge(df_pivot, on='moughataa_key', how='left').fillna(0)
    geosource = GeoJSONDataSource(geojson=merged.to_json())

    palette = OrRd9[::-1]
    mapper = LinearColorMapper(palette=palette, low=0, high=merged[candidats[0]].max())

    p = figure(title=f"Résultats Électoraux 2024 : {candidats[0]}", height=600, width=800, tools="pan,wheel_zoom,reset", x_axis_location=None, y_axis_location=None)

    renderer = p.patches('xs', 'ys', source=geosource, fill_color={'field': candidats[0], 'transform': mapper}, line_color='black', line_width=0.5, fill_alpha=0.8)

    hover = HoverTool(tooltips=[("Moughataa", "@shapeName"), ("Voix", f"@{candidats[0]}{{0,0}}")])
    p.add_tools(hover)

    color_bar = ColorBar(color_mapper=mapper, label_standoff=12, location=(0,0), title="Nombre de voix")
    p.add_layout(color_bar, 'right')

    select = Select(title="Choisir un candidat :", value=candidats[0], options=candidats)
    callback = CustomJS(args=dict(renderer=renderer, hover=hover, mapper=mapper, geosource=geosource, p=p), code="""
        const cand = cb_obj.value;
        renderer.glyph.fill_color.field = cand;
        hover.tooltips = [["Moughataa", "@shapeName"], ["Voix", "@" + cand + "{0,0}"]];
        p.title.text = "Résultats Électoraux 2024 : " + cand;
        const data = geosource.data[cand];
        const max_val = Math.max.apply(null, data);
        mapper.high = max_val;   
        renderer.data_source.change.emit();
    """)
    select.js_on_change('value', callback)

    show(column(select, p))
