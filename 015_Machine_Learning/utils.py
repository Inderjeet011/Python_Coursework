import geopandas
import folium
from shapely.geometry import Point

def create_point(row):
    """Helper function to create a Point from row data."""
    return Point(row['LONGITUDE'], row['LATITUDE'])

def to_geo_dataframe(df):
    """Turn a carpark DataFrame into a GeoDataFrame."""
    
    # Option 1: Using for-loop (current implementation)
    geometry = []
    for index, row in df.iterrows():
        point = Point(row['LONGITUDE'], row['LATITUDE'])
        geometry.append(point)

    # Option 2: Using df.apply with a function (alternative approach)
    # geometry = df.apply(create_point, axis=1).tolist()

    gdf = geopandas.GeoDataFrame(df, geometry=geometry)
    gdf.crs = {'init': 'epsg:4326'}
    
    # Print out gdf to see its contents
    print("GeoDataFrame contents:")
    print(gdf)
    print("\nGeoDataFrame info:")
    print(gdf.info())
    print("\nFirst few rows:")
    print(gdf.head())
    
    return gdf


def plot_gdf(filename, gdf):
    """Save an interactive map plot."""
    
    map = folium.Map(
        location=[54.6, -5.90],
        zoom_start=10
    )
    carparks = folium.features.GeoJson(gdf)
    map.add_children(carparks)
    map.save(filename)