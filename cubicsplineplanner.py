import math
import numpy as np
import matplotlib.pyplot as plt

class Waypoint:
	x = None
	y = None
	interceptDegrees = None
	
	def __init__(self, x, y):
		self.x = x
		self.y = y

class StraightLine:
	pointOne = None
	pointTwo = None
	
	degrees = None
	
	def __init__(self, pointOne, pointTwo):
		self.pointOne = pointOne
		self.pointTwo = pointTwo
		
		xElevationChange = pointTwo.x - pointOne.x
		yElevationChange = pointTwo.y - pointOne.y
		
		self.degrees = math.degrees(math.atan2(yElevationChange, xElevationChange))
		
class Spline:
	waypointList = []
	
	xPositionList = []
	yPositionList = []
	
	def __init__(self, waypointList):
		self.waypointList = waypointList
		calcPath()
	
	def calcPath(self):
		self.waypointList[1].interceptDegrees = StraightLine(self.waypointList[0], waypointList[2]).degrees
		

exampleSpline = Spline([Waypoint(0,0), Waypoint(1,2), Waypoint(2, 1)])

