import plotly.graph_objects as go
import pandas as pd
import numpy as np
import plotly
# Read data from a csv
# z_data = pd.read_csv('testData.csv')
# z = z_data.values

# y_data = pd.read_csv('testData_y.csv')
# y = y_data.values
# x_data = pd.read_csv('testData_x.csv')
# x = x_data.values



# sh_0, sh_1 = z.shape
# x, y = np.linspace(0, 1, sh_0), np.linspace(0, 1, sh_1)
# y = np.linspace(40.0, 80.0, sh_1)
# y = np.array([40.0,60.0,80.0])
# x_data = pd.read_csv('3dsieveData_x.csv')
# x = np.transpose(x_data.values)[1]
# x = np.flip(x)

x = []
y = []
z = []

data = pd.read_csv('3dsieveData2.txt',sep='\s+',header=None)
data = pd.DataFrame(data)

for i in range(1, len(data[0].values)):
	x.append(data[0].values[i])

for i in range(1, len(data.values[0])):
	y.append(data.values[0][i])

for i in range(1, len(data.values[0])):
	z_column = []
	for j in range(1, len(data[0].values)):
		z_column.append(data[i].values[j])
	z.append(z_column)

# x = np.array([200,80,12])
# y = np.array([40,50])
# z = np.array([[100,70],[100,90]])


fig = go.Figure(data=[go.Surface(
							z=z, x=x, y=y,
							contours = {
							"x": {"show": True, "start": 0, "end": 200, "color":"#1f1f1f"},
							"y": {"show": True, "start": 1, "end": 5, "size": 0.5, "color":"#1f1f1f"},
							"z": {"show": True, "start": 0, "end": 100, "size": 4, "color":"#1f1f1f"}
							}, opacity = 0.9
							)])

# fig = go.Figure(data=[go.Surface(
# 							z=z,
							# contours = {
							# "x": {"show": True, "start": 0, "end": 200, "color":"#1f1f1f"},
							# "y": {"show": True, "start": 40, "end": 80, "size": 5, "color":"#1f1f1f"},
							# "z": {"show": True, "start": 0, "end": 100, "size": 4, "color":"#1f1f1f"}
							# }
							# )])

fig.update_layout(scene = dict(
                    xaxis_title='Sieve size',
                    yaxis_title='Shape parameter',
                    zaxis_title='Percent passing'))
fig.update_layout(scene = dict(
                    xaxis = dict(
                    	autorange = "reversed",
						tickmode = "array",
						# tickvals = x,
						# tickvals = [200, 75, 50, 25, 12.5, 4.75, 1.18, 0.075],
						tickvals = [200, 31.5, 4.75, 1.18, 0.3, 0.075],
						# range = [200, 0.075],
						# tick0 = 0,
						# dtick = 0.01,
						type = "log",
						ticks = "outside",
                    	tickwidth = 2,
                    	ticklen = 10,
                    	tickcolor = "black",					
						showline = True,
						linecolor = "black",
						linewidth = 2,                 	
                        backgroundcolor="rgb(200, 200, 230)",
                        gridcolor="lightgray",
                        showbackground=False,
                        zerolinecolor="black",),
                    yaxis = dict(
                    	# range = [40, 60],
                    	tick0 = 1,
                    	dtick = 0.5,
                    	ticks = "outside",
                    	tickwidth = 2,
                    	ticklen = 10,
                    	tickcolor = "black",
                    	showline = True,
                    	linecolor = "black",
						linewidth = 2,
                        backgroundcolor="rgb(230, 200,230)",
                        gridcolor="lightgray",
                        showbackground=False,
                        zerolinecolor="black"),
                    zaxis = dict(
                    	# range = [0, 100],
                    	ticks = "outside",
                    	tickwidth = 2,
                    	ticklen = 10,
                    	tickcolor = "black",                   	
                    	showline = True,
                    	linecolor = "black",
						linewidth = 2, 
                        backgroundcolor="rgb(230, 230,200)",
                        gridcolor="lightgray",
                        showbackground=False,
                        zerolinecolor="black",),
                    aspectmode = "manual",
					aspectratio = dict(x=1,y=1,z=0.7)
                    ),
                    # width=700,
                    # margin=dict(
                    # r=10, l=10,
                    # b=10, t=10)
                  )
camera = dict(
    up=dict(x=0, y=0, z=-1),
    center=dict(x=0, y=0, z=0),
    eye=dict(x=2, y=2, z=1),
    projection=dict(type="orthographic")
)

# fig.update_xaxes(title_standoff=20)

fig.update_layout(scene_camera=camera)

fig.update_layout(title='3D Sieve Analysis', autosize=False,
                  width=650, height=650,
                  margin=dict(l=15, r=40, b=10, t=30, pad=20))


fig.update_layout(font=dict(
        family="Times New Roman",
        size=12,
        # color="RebeccaPurple"
    ))

def calculateVolume(x, y, z):
	volume = 0
	for i in range(0, len(x)-1):
		for j in range(0, len(y)-1):
			# Heights: z1, z2, z3, z4
			z1 = z[j][i]
			z2 = z[j+1][i]
			z3 = z[j][i+1]
			z4 = z[j+1][i+1]
			z_avg = (z1+z2+z3+z4)/4
			if (z_avg != 100):
				volume += (x[i+1] - x[i])*(y[j+1] - y[j])*z_avg
	return volume

volume = calculateVolume(x, y, z)

print("The volume is " + str(round(volume)))
# fig.update_traces(contours_z=dict(show=True, usecolormap=True,
#                                   highlightcolor="limegreen", project_z=False))

# fig.update_layout(yaxis = dict(
#         # tickmode = 'array',
#         # tickvals = [40, 60, 80],
#         dtick = 0.75,
#         tick0 = 0.5,
#         tickmode = "linear"
#     ))
# fig.update_layout(
#     scene = dict(
#         tickmode = 'linear',
#         tick0 = 0.5,
#         dtick = 0.75))

# fig.update_scenes(xaxis = dict(
	# title='fghttr',
	# gridcolor='grey',
	# tickmode= 'array',
	# tickvals= x,
	# tickmode= 'linear',
	# tick0=0,
	# dtick=0.1,
	# range=[0,200],
	# type='log'
	# ))

# fig.update_scenes(xaxis = dict(
	# gridcolor='grey',
	# tickmode= 'array',
	# tickvals= x))

# fig.update_scenes(yaxis = dict(
	# gridcolor='grey',
	# tickmode= 'array',
	# tickvals= y))

# fig.update_xaxes(title_font_family="Times New Roman")

# fig.update_xaxes(
#     showgrid=True,
#     ticks="outside",
#     tickson="boundaries",
#     ticklen=20
# )


# fig.update_layout(
#     title="Plot Title",
#     xaxis_title="X Axis Title",
#     yaxis_title="Y Axis Title",
#     legend_title="Legend Title",
#     font=dict(
#         family="Courier New, monospace",
#         size=18,
#         color="RebeccaPurple"
#     )
# )

# fig.show()

# fig.write_image("fig1.png")

import os, sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5 import QtWebEngineWidgets

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget


class PlotlyViewer(QtWebEngineWidgets.QWebEngineView):
    def __init__(self, fig, exec=True):
        # Create a QApplication instance or use the existing one if it exists
        self.app = QApplication.instance() if QApplication.instance() else QApplication(sys.argv)

        super().__init__()

        self.file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "temp.html"))
        plotly.offline.plot(fig, filename=self.file_path, auto_open=False)
        self.load(QUrl.fromLocalFile(self.file_path))
        self.setWindowTitle("3D Sieve Analysis")
        self.resize(700,700)
        self.show()
        w = AnotherWindow()
        w.show()

        if exec:
            self.app.exec_()

    def closeEvent(self, event):
        os.remove(self.file_path)

class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("The volume is " + str(round(volume)))
        layout.addWidget(self.label)
        self.setLayout(layout)

win = PlotlyViewer(fig)

# app = QApplication(sys.argv)

