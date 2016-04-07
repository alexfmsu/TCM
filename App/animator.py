import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import axes3d
import pickle

from mpl_toolkits.mplot3d import Axes3D

def make_plot3D(x, xmin, xmax, data, ymin, ymax, state, not_empty, max_limit = 1e-3):
	### Float parameters: 14, 8

	#------------------------------------------------------------------------------------------------------------------
	fig = plt.figure(figsize = (14, 8))
	fig.subplots_adjust(left=0.00, bottom=0.00, top=1, right=1)
	
	ax = fig.gca(projection='3d')
	#------------------------------------------------------------------------------------------------------------------
	count = np.shape(data)[1]
	
	pos_count = 0
	pos_state = []
	#------------------------------------------------------------------------------------------------------------------
	for i in range(0, count):
		elem = data[:,i]

		min = np.min(elem)
		max = np.max(elem)

		if ((not not_empty) or (not_empty and max > max_limit)) and (min>=ymin) and (max<=ymax):
			ax.plot(x, elem, zs=pos_count, zdir='x', label=r'$%s$' %state[i], linewidth = 1, antialiased = True)
			pos_state.append(state[i])
			
			pos_count += 1
	#------------------------------------------------------------------------------------------------------------------
	ax.set_xlim3d(0, pos_count)
	ax.set_ylim3d(xmin, xmax)
	ax.set_zlim3d(ymin, ymax)
	
	ax.set_xticks(np.arange(0, pos_count))
	ax.set_xticklabels(pos_state)

	# ax.set_xlabel(r'$state$', fontsize=18)
	ax.set_ylabel(r'$time$', fontsize=18)
	ax.set_zlabel(r'$|\lambda|$', fontsize=18)
	plt.setp(plt.xticks()[1], rotation=90)
	ax.zaxis.set_rotate_label(False)
	#------------------------------------------------------------------------------------------------------------------
	plt.legend(loc='upper left', shadow=True, title="States", fontsize=18)
	ax.get_legend().get_title().set_fontsize(18)
	#------------------------------------------------------------------------------------------------------------------	
	plt.show()
	
def make_plot(x, xmin, xmax, ymin, ymax, data):
	fig = plt.figure(figsize = (12,8), facecolor="white")
	fig.set_dpi(75)
	
	plt.plot(x, data, linewidth = 0.75, antialiased = True, solid_joinstyle='round')
	
	plt.axis([xmin, xmax, 0, 1])
	plt.xlim(xmin, xmax)
	plt.ylim(ymin, ymax)
	plt.xlabel(r'$t$', fontsize=20)
	plt.ylabel(r'$\psi(t)$   ', fontsize=20, rotation = 0)
	plt.xticks(np.arange(xmin, xmax, round((xmax-xmin)/10, 2)))

	plt.title(r'$Wave$ $function$', fontsize = 20)
	plt.grid(True)

	plt.show()