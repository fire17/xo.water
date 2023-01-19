from pprint import pprint as pp

from services.googler import Googler
from services.shush import Shush
from services.api import *


def LoadWaterServices(water):
	print(" ::: LoadWaterServices :::")
	# print("wwwwwwwwwwwwwwwwwwwwwwwwww")
	# print("wwwwwwwwwwwwwwwwwwwwwwwwww")
	# print("wwwwwwwwwwwwwwwwwwwwwwwwww")
	# print("wwwwwwwwwwwwwwwwwwwwwwwwww")
	# print("wwwwwwwwwwwwwwwwwwwwwwwwww")
	services = {
		"shush": Shush(water),
		"googler":Googler(water)
		}
	return services

