


def getLatFromStrPoint(strPoint):
	strPoint = strPoint.split("(")[1]
	return float(strPoint.split(",")[0])

def getLonFromStrPoint(strPoint):
	strPoint = strPoint.split("(")[1]
	strPoint = strPoint.split(",")[1]
	return float(strPoint.split(")")[0])