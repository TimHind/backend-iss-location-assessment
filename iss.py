#!/usr/bin/env python

__author__ = 'Tim'

import requests
import turtle
import time

ar = requests.get('http://api.open-notify.org/astros.json')
nr = requests.get('http://api.open-notify.org/iss-now.json')
pr = requests.get('http://api.open-notify.org/iss-pass.json?lat=39.791000&lon=-86.148003')

iss_icon = "iss.gif"
screen = turtle.Screen()
screen.setworldcoordinates(-180, -180, 180, 180)
screen.bgpic("map.gif")
screen.setup(720, 360)

def pass_time(pr):
    passtime = pr.json()['response'][0]['risetime']
    return time.ctime(passtime)

def current_list(ar):
    """Full names, the spacecraft they are currently on board, and the total number of astronauts in space"""
    people_onboard = ar.json()['people']
    return people_onboard

def current_location(nr):
    location_list = []
    long_lat = nr.json()['iss_position']
    location_list.append("LONG/ LAT: " + str(long_lat))
    time_stamp = nr.json()['timestamp']
    location_list.append("TIMESTAMP: " + str(time_stamp))
    return location_list


def main():
    print("CURRENT ASTRONAUTS: " + str(current_list(ar)))
    print("TOTAL NUMBER ONBOARD: " + str(len(current_list(ar))))
    print(current_location(nr))
    print("INDY PASSTIME: " + pass_time(pr))
    screen.register_shape(iss_icon)
    iss = turtle.Turtle(iss_icon)
    indy = turtle.Turtle()
    indy.shape("circle")
    indy.color("yellow")
    indy.penup()
    indy.goto(-86.148003, 39.791000)
    indy.write(pass_time(pr))
    iss.shape(iss_icon)
    iss.penup()
    iss.goto(-73.93, 40.73)
    turtle.done()
   



if __name__ == '__main__':
    main()
