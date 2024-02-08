import numpy as np
from datetime import datetime
import os
from Parameters.cone_params import *
from . import date, cores, solar_wind, stations
from . import misc

def ConeInputs():
    EventDate = datetime(Year,Month,Day,Hour,Minute,Second)
    DateCreate = date.Date(EventDate)
    DateArray = DateCreate.GetDate()

    WindCreate = solar_wind.Solar_Wind(Vx, Vy, Vz, By, Bz, Density, Dst, G1, G2, G3, W1, W2, W3, W4, W5, W6)
    WindArray = WindCreate.GetWind()

    RigidityArray = [StartRigidity,EndRigidity,RigidityStep]

    MagFieldModel = np.array([Internal,External])

    EndParams = [MinAlt,MaxDist,MaxTime]

    CreateStations = stations.Stations(List, Alt, Zenith, Azimuth)
    InputtedStations = CreateStations
    if 'Custom_Locations' in locals() or 'Custom_Locations' in globals():
          CreateStations.AddLocation(Custom_Locations)
    Used_Stations_Temp = CreateStations.GetStations()
    temp = list(Used_Stations_Temp)
    Station_Array = temp


    current_directory = os.getcwd()
    result_directory = os.path.join(current_directory,"Results")
    final_directory = os.path.join(result_directory,FolderName)
    FileArray = [FileName, FolderName, final_directory]

    ParticleArray = [AtomicNum,AntiCheck]

    misc.ParamCheck(Alt,EndParams)

    ConeInputArray = [RigidityArray,DateArray,MagFieldModel,IntModel,ParticleArray,IOPT,WindArray,Magnetopause,FileArray,CoordinateSystem,MaxStepPercent,EndParams, Station_Array, InputtedStations]

    return ConeInputArray