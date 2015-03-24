# utils.py

def xyY_to_XYZ(xyY):
	XYZ = []
	for colour in xyY:
		X = (colour[0] * colour[2]) / colour[1]
		Y = colour[2]
		Z = ((1 - colour[0] - colour[1]) * colour[2]) / colour[1]
		XYZ.append([X, Y, Z])
# end def xyY_to_XYZ

