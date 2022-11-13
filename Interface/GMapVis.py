from Interface import PopulateData
import tkinter
from tkintermapview import TkinterMapView

class MainWindow:

    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("1200x800")
        self.root.title("RunItUp")
        self.map = MapCanvas(self.root)

        self.root.mainloop()


class SearchBar:

    def __init__(self, rootWindow: tkinter):
        self.searchCanvas = tkinter.Canvas(rootWindow)

class MapCanvas:

    def __init__(self, rootWindow: tkinter):
        self.mapCanvas = tkinter.Canvas(rootWindow, width=600, height=600)
        self.map_widget = TkinterMapView(self.mapCanvas, width=600, height=600, corner_radius=0)
        self.mapCanvas.create_window(400, 600, window=self.map_widget, anchor=tkinter.E)
        self.mapCanvas.pack()
        self.map_widget.pack(fill='both', expand=True)