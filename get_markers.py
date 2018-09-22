import xml.etree.ElementTree
import numpy as np

filename='CellCounter_ARBc_#4_Li+VPA_37C_4110_C10_IlluminationCorrected_stitched_color.xml'
e=xml.etree.ElementTree.parse(filename).getroot()

coord_dict={}

for i in range(1,len(e.find('Marker_Data'))):
	type=e.find('Marker_Data')[i][0].text
	print(type)
	list_of_coords=[]
	for j in range(1,len(e.find('Marker_Data')[i])):
		x_coord=int(e.find('Marker_Data')[i][j][0].text)
		y_coord=int(e.find('Marker_Data')[i][j][1].text)
		list_of_coords.append((x_coord,y_coord))
	coord_dict[type]=list_of_coords

np.save('marker_coordinates.npy',coord_dict)
