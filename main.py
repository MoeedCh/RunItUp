import googlemaps

from BackEnd.BootUp import *
from BackEnd.set_info import *
from Interface import Locations
from BackEnd import APIdata
from BackEnd import set_info
from Interface import PopulateData
from Testing import testGMPLOT
from Interface import GMapVis
from Testing.testing_getters import *
'''
Bootup the firebase database connection. If so desired, reload all of the default information
'''

initialize_firebase(loadDefaults=True)
print('\n\n')



#APIdata.popWithGoogleAndStoreInBackEnd((37.220090, -80.422660), "Tennis", 50)
#APIdata.popWithGoogleAndStoreInBackEnd((37.220090, -80.422660), "Basketball", 50)

#GMapVis.MainWindow()
# test_get_event({'field': 'soccer'})
create_many_events()
testGMPLOT.testGPLOT()

#test_get_location()

#GMapVis.MainWindow()