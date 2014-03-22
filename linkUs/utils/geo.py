


def getLatFromStrPoint(strPoint):
	strPoint = strPoint.split("(")[1]
	return float(strPoint.split(",")[0])

def getLonFromStrPoint(strPoint):
	strPoint = strPoint.split("(")[1]
	strPoint = strPoint.split(",")[1]
	return float(strPoint.split(")")[0])

def getDistanceBetween(x1, y1, x2, y2):
	return ((x1-x2)**2+(y1-y2)**2)**(0.5)