#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Find the closest carparks to the Computer Science building

@author: Phil Weir <phil.weir@flaxandteal.co.uk>
@license: MIT
"""

import pandas
from sklearn.neighbors import NearestNeighbors

import utils

def closest_carpark(gdf, target):
    # Find the closest car parks to a target location
    # gdf = car park data with map coordinates
    # target = [latitude, longitude] of where we want to find car parks near
    
    # List to store all car park coordinates
    X = []
    
    # Helper function to get coordinates from each car park row
    def extract_points(row):
        # Get lat/lon from the geometry (map location)
        X.append([row.geometry.y, row.geometry.x])
        
    # Go through each car park and extract its coordinates
    gdf.apply(extract_points, axis=1)
    
    # Use machine learning to find the 4 closest car parks
    nbrs = NearestNeighbors(n_neighbors=4).fit(X)
    
    # Put our target location in a list (the algorithm expects a list)
    Y = [target]
    
    # Find the 4 nearest car parks to our target
    # Returns distances and which rows they correspond to
    distances_per_Y_row, row_numbers_per_Y_row = nbrs.kneighbors(Y)
    
    # Get the results for our single target (first row)
    distances = distances_per_Y_row[0]
    row_numbers = row_numbers_per_Y_row[0]
    
    # Distance to the closest car park (our reference point)
    reference_distance = distances[0]
    
    # Check each of the 4 closest car parks
    for distance, row_i in zip(distances, row_numbers):
        # Calculate how much further this one is compared to the closest
        relative_distance = 100 * (distance / reference_distance - 1)
        
        # Get the car park details (name, etc.)
        row = gdf.iloc[row_i]
        
        # Show the result
        print(row['NAME'], " is ", relative_distance, "percent further than the closest")

        
def run():
    # Load data into variable called "df"
    df = pandas.read_csv('car-park-locations-data.csv', encoding='latin1')
    
    # Because why not?
    # print(df.describe())
    
    # Get a geopandas dataframe, from a normal pandas one
    gdf = utils.to_geo_dataframe(df)
    
    # Create a plot
    utils.plot_gdf("output.html", gdf)
    
    # CompSci Building 54.5817428 -5.9374874
    closest_carpark(gdf, [54.5817428, -5.9374874])
    
if __name__ == "__main__":
    run()