from Interface import PopulateData
import tkinter
from tkintermapview import TkinterMapView

class MainWindow:

    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("1200x800")
        self.root.title("RunItUp")
        self.search = SearchBar(self.root)
        self.map = MapCanvas(self.root)
        self.filters = Filters(self.root)
        self.root.mainloop()




class Filters:

    def __init__(self, rootWindow:tkinter):
        self.filterCanvas = tkinter.Canvas(rootWindow, width=100, height=500)

        self.volState = tkinter.IntVar()
        self.volleyBallBox = tkinter.Checkbutton(self.filterCanvas, text="Volleyball", variable=self.volState)
        self.filterCanvas.create_window(50, 20, window=self.volleyBallBox)


        self.basketState = tkinter.IntVar()
        self.BasketBallBox = tkinter.Checkbutton(self.filterCanvas, text="Basketball")
        self.filterCanvas.create_window(50, 40, window=self.BasketBallBox)

        self.soccerState = tkinter.IntVar()
        self.SoccerBox = tkinter.Checkbutton(self.filterCanvas, text="Soccer")
        self.filterCanvas.create_window(50, 60, window=self.SoccerBox)

        self.tennisState = tkinter.IntVar()
        self.TennisBox = tkinter.Checkbutton(self.filterCanvas, text="Tennis")
        self.filterCanvas.create_window(50, 80, window=self.TennisBox)

        self.enterButton = tkinter.Button(text="Search", command=self.search)
        self.filterCanvas.create_window(50, 100, window=self.enterButton)


        self.filterCanvas.pack()


    def search(self):
        return 1


class SearchBar:

    def __init__(self, rootWindow: tkinter):
        self.searchCanvas = tkinter.Canvas(rootWindow, width=800, height=50)
        self.search_widget = tkinter.Entry(self.searchCanvas, width=80, justify=tkinter.LEFT)
        self.searchCanvas.create_window(450, 20, window=self.search_widget)
        self.enterButton = tkinter.Button(text="Search", command=self.updateSearch)
        self.searchCanvas.create_window(725, 20, window=self.enterButton)
        self.searchCanvas.pack()

    def updateSearch(self):
        text = self.search_widget.get()

class MapCanvas:

    def __init__(self, rootWindow: tkinter):
        self.mapCanvas = tkinter.Canvas(rootWindow, width=800, height=800)
        self.map_widget = TkinterMapView(self.mapCanvas, width=800, height=800, corner_radius=0)
        self.mapCanvas.create_window(400, 800, window=self.map_widget, anchor=tkinter.E)
        self.mapCanvas.pack(side= tkinter.RIGHT)
        self.map_widget.pack(fill='both', expand=True)
        self.map_widget.set_position(37.220090, -80.422660)
        self.map_widget.set_zoom(15)