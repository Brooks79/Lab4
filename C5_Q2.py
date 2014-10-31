__author__ = 'Ray'

import arcpy

from arcpy import env
env.workspace = "C:\EsriPress\Python\Data\Exercise05"

arcpy.AddXY_management("hospitals.shp")

raw_input("Press enter: ")