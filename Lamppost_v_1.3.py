#Python3 Lamppost model
import csv
import matplotlib.pyplot as plt
import getopt
import sys
from numpy import *
from matplotlib import cm, colors
from mpl_toolkits.mplot3d import Axes3D
from random import *
from math import radians, degrees, sqrt

#phi is the longitudinal angle
#theta is the altitude angle

def magnitude(x,y,z):
    return sqrt(((x**2.0)+(y**2.0)+(z**2.0)))

#randomnes.....+ angle choice
def foo():
    print("This is the foo option")

def bar(number):
    print(number)

def main():
    
    
    #passing of arguments
    debug = str(sys.argv[8])
    CSV = str(sys.argv[9])
    hpng = str(sys.argv[10])
    lpng = str(sys.argv[11])

    nor = int(sys.argv[1])
    nob = int(sys.argv[4])
    h = float(sys.argv[2])
    radius = float(sys.argv[3])

    obsx = int(sys.argv[5])
    obsy = int(sys.argv[6])
    obsz = int(sys.argv[7])
    




    print()
    print("Height = " + str(h) + " " + "Radius = " + str(radius) + "OBS POS = " + str(obsx) + " " + str(obsy) + " " + str(obsz))
    #print("START OF MAIN")
    #debug option if yes then graphs will be generated
    #debug = "N"
    #debug = "Y"
    #CSV option if yes then will produce a csv of hist data
    #CSV = "N"
    #CSV = "Y"
    #hpng = histogram png option if yes then will save histogram as png
    #hpng = "Y"
    #hpng = "N"
    #lpng = lamppost model png option if yes then will save graph of lamppost model as png
    #lpng = "Y"
    #lpng = "N"
    
    #nor = number of rays
    #nor = 100000
    #nob = number of bins
    #nob = 20
    
    #constants for height and radius in meters
    #h = 1000
    #radius = 1000


    hypo = sqrt(h**2.0+radius**2.0)
    JP = hypo
    angle = arccos(h/hypo)
    
    #angle = radians(60)
    thetamin = radians(0)

    r = 1
    xx = []
    yy = []
    zz = []
    
    if (degrees(angle) == 90):
        print("IMPOSSIBLE")
        exit()
    
    angle = pi - angle
    thetamax = cos(angle)
    thetamin = -cos(thetamin)
    test = []
    iss = []
    finallist = []
    for i in range(0, nor):
        phi = uniform(0, 2*pi)
        costheta = uniform(thetamax, thetamin)
        theta = arccos( costheta )
        test.append(degrees(theta))
        xx.append(r*sin(theta)*cos(phi))
        yy.append(r*sin(theta)*sin(phi))
        zz.append(r*thetamax)

    #obs = [0,0,1]
    mobs = magnitude(obsx, obsy, obsz)
    alpha = obsx/mobs
    beta = obsy/mobs
    gamma = obsz/mobs
    magnitudes = []
    cosT = []
    delays = []
    tdelays = []
    #c is the speed of light in m/s
    C = 299792458
    #print("THIS IS CALCS")
    for i in range(0, len(xx)):
        magnitudes.append(magnitude(xx[i], yy[i], zz[i]))
        #calcs the cos(Theta) term
        cosT.append(((xx[i]*alpha)+(yy[i]*beta)+(zz[i]*gamma))/magnitudes[i])
        #calcs the delays
        delays.append(magnitudes[i]*(1.0-cosT[i]))
        tdelays.append((delays[i]*JP)/C)
        #print(tdelays[i])
 
###OUTPUT###

###CSV###
    if (CSV == "Y" or CSV == "y"):
        #print("This is csv")
    #output delays as a csv
    #npb = number per bin
    #bins = the value for the delay in each of the bins
    #patches can be ignored. Just states that its basically a histogram
        filename = "output_" + str(h) + "_" + str(radius) + ".csv"
        npb, bins, patches = plt.hist(tdelays, bins=nob)
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(["# of rays" , nor, "height", h, "radius", radius, "angle", 180-degrees(angle)])
            writer.writerow(["Bin(delay time(s))", "npb"])
            for i in range(0, len(bins)-1):
                writer.writerow([bins[i], npb[i]])
###PNGS###

    if ((hpng == "Y") or (hpng == "y")):
        #print("this is histo")
        plt.figure(figsize=(10,6))
        plt.hist(tdelays, bins= nob, color='b')
        plt.xlabel("Delay (s)")
        plt.ylabel("Number of delays")
        titlestring = "Delays of Light Echos with # of rays = " + str(nor)
        plt.title(titlestring)
        plt.tight_layout()
        plt.savefig('delays_hist_'+str(h) + '_' + str(radius)+ '_' + 'obs position'+ '_' + str(obsx) + '_' + str(obsy) + '_' + str(obsz) + '.png')

    if ((lpng == "Y") or (lpng == "y")):
        #print("This is lamppy")
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(0,0,0, color='k')
        ax.scatter(xx,yy,zz)
        ax.set_xlim([-1,1])
        ax.set_ylim([-1,1])
        ax.set_zlim([-1,1])
        ax.set_xlabel("x-axis")
        ax.set_ylabel("Y-axis")
        ax.set_zlabel("Z-axis")
        ax.set_aspect("equal")
        titlestring = "Lamppost Model with # of rays = " + str(nor)
        plt.title(titlestring)
        plt.tight_layout()
        plt.savefig('lamppost_model_'+str(h)+'_'+str(radius) + 'obs position'+ '_' + str(obsx) + '_' + str(obsy) + '_' + str(obsz) + '.png')

###DEBUGING###


    if ((debug == "Y") or (debug =="y")):
        print("THIS IS DEBUGGING")
        plt.figure(figsize=(10,6))
        #plt.hist(delays, bins= nob, color='b')
        plt.hist(tdelays, bins= nob, color='b')
        plt.xlabel("Delay (s)")
        plt.ylabel("Number of delays")
        titlestring = "Delays of Light Echos with # of rays = " + str(nor)
        plt.title(titlestring)
        plt.tight_layout()
        
        # Create a sphere
        r = 1
        phi, theta = mgrid[0.0:2.0*pi:100j, 0.0:pi:100j]
        x = r*sin(theta)*cos(phi)
        y = r*sin(theta)*sin(phi)
        z = r*cos(theta)

        #Set colours and render
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        #ENABLES SPHERE TO BE DRAWN VERY RESOURCE HEAVY
        #ax.plot_surface(x, y, z,  rstride=1, cstride=1, color='lightgrey', alpha=0.3, linewidth=0)
    
        #origin
        ax.scatter(0,0,0, color='k')
    
        ax.scatter(xx,yy,zz)

        ax.set_xlim([-1,1])
        ax.set_ylim([-1,1])
        ax.set_zlim([-1,1])
        ax.set_xlabel("x-axis")
        ax.set_ylabel("Y-axis")
        ax.set_zlabel("Z-axis")
        ax.set_aspect("equal")
        titlestring = "Lamppost Model with # of rays = " + str(nor)
        plt.title(titlestring)
        plt.tight_layout()
        
        plt.show()
    
    print("DONE")
main()
