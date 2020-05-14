import matplotlib.pyplot as plt
import shapefile
import os

shape = shapefile.Reader("crime_data/crime_dt.shp", encoding="ISO-8859-1")
shapeRecords = shape.shapeRecords()

# x's are -73.59 (west) to -79.53 (east)
x_list = []
# y's are 45.53 (north) to 49.49 (south)
y_list = []

for i in range(len(shapeRecords)):
    x = shapeRecords[i].shape.__geo_interface__["coordinates"][0]
    x_list.append(x)
    y = shapeRecords[i].shape.__geo_interface__["coordinates"][1]
    y_list.append(y)

plt.scatter(x_list, y_list)
plt.show()
print("Done")
