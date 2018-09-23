from PIL import Image
import numpy as np

filename='all_not_pcna.tif'
img=Image.open(filename)

coord_dict=np.load('marker_coordinates.npy').item()

crop_size=75

for i in range(1,6):
	x_coords=[]
	y_coords=[]
	for coord in coord_dict[str(i)]:
		x_coords.append(coord[0])
		y_coords.append(coord[1])
		area=(coord[0]-crop_size,coord[1]-crop_size,coord[0]+crop_size,coord[1]+crop_size)
		img_crop=img.crop(area)
		img_crop.save('all/'+str(i)+'_'+str(coord[0])+'_'+str(coord[1])+'.png')
