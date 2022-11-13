import gmaps
from Interface import PopulateData
import tkinter
from tkinter import *
from tkintermapview import TkinterMapView

def testGPLOT():
    gmaps.configure(api_key="AIzaSyA-BRYsxwC4d1mNlFOwwjJtaQI9HGLm5u0")
    populate = PopulateData.PopulateGmap((37.220090, -80.422660), 50)
    populate.getAllLocationsNearUser()
    marker_locations =[]

    for i in populate.locationsOnMap:
        marker_locations.append(i.getLocation())
        print(i.getLocation())

    #fig = gmaps.figure()
    #markers = gmaps.marker_layer(marker_locations)
    #fig.add_layer(markers)

    root_tk = tkinter.Tk()
    root_tk.geometry("500x500")
    root_tk.title("Google Maps")

    def Schedule():
        print("FUCK")

    def testPop(marker):
        global pop
        pop = Toplevel(root_tk)
        pop.title("Event List")
        pop.geometry("350x600")

        popLabel = Label(pop, text="LIST OF SCHEDULED EVENTS: ")
        popLabel.pack(pady=10)
        myFrame = Frame(pop, bg='green')
        myFrame.pack(pady=5)


        ScheduleEventButton = Button(myFrame, text="Schedule",command=Schedule)
        ScheduleEventButton.grid(row=0, column=1)
        ScheduleEventButton.pack(50)
    #map inside window
    map_widget = TkinterMapView(root_tk, width=600,height=400,corner_radius=0)
    map_widget.pack(fill='both',expand=True)
    for i in populate.locationsOnMap:
        marker = map_widget.set_marker(float(i.latitude), float(i.longitude), text=i.name, command=testPop)
    map_widget.set_position(37.220090, -80.422660)
    map_widget.set_zoom(15)

    root_tk.mainloop()


