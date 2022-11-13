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

    def ScheduleEvent():
        print('FuCk')
        
    def eventsPopUp():
        global PopUp
        PopUp = Toplevel(root_tk)
        PopUp.title('Event List')
        PopUp.geometry('400x650')

        popUpLabel = Label(PopUp, text='LIST OF EVENTS')

        ScheduleButton = Button(root_tk, text='Schedule', command=ScheduleEvent)
        ScheduleButton.grid(row=0, column=1)
        ScheduleButton.pack(pady=50)
    #map inside window
    map_widget = TkinterMapView(root_tk, width=600,height=400,corner_radius=0)
    map_widget.pack(fill='both',expand=True)
    for i in populate.locationsOnMap:
        map_widget.set_marker(float(i.latitude), float(i.longitude), text=i.name, command=eventsPopUp)

    map_widget.set_position(37.220090, -80.422660)
    map_widget.set_zoom(15)

    root_tk.mainloop()


