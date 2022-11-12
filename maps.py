import tkinter
import tkintermapview

## Placeholder variables used in here - replace w the actual variables you're using
cityLongitude = 43.2557
cityLatitude = 79.8711

locationLongitude = 43.2609
locationLatitude = 79.9192

## Placeholder variables to demonstrate display on map
## Should be replaced by the information pulled from the weather instruments
locationTemp = 76
locationWindSpeed = 43
locationPrecipitation = 1.0
locationWindDirection = "N"
locationOceanConditions = "Clear"

## Create tkinter window
root_tk = tkinter.Tk()
root_tk.geometry(f"{800}x{600}")
root_tk.title("map_view_example.py")

# create map widget
map_widget = tkintermapview.TkinterMapView(root_tk, width=800, height=600, corner_radius=0)
map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

map_widget.set_position(cityLongitude, cityLatitude)  # City location
map_widget.set_zoom(8)

# Markers
marker_1 = map_widget.set_marker(locationLongitude, locationLatitude)
marker_1.set_text("Temperature: %s Degrees \n Wind Speed: %s km/Hr \n Precipitation: %s mm \n Wind Direction: %s \n Ocean conditions: %s" % (locationTemp, locationWindSpeed, locationPrecipitation, locationWindDirection, locationOceanConditions))

root_tk.mainloop()