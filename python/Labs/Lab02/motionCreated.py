# -*- coding: utf-8 -*-
"""
Created on 9/10/2023

@author: Eugene Kozlakov
@description: Given a duration of time, this program computes 
the velocity, average velocity, and displacement of an object.
"""

# Useful values:
acceleration = 5.25
initialVelocity = 8.25

# Initialize the radius:
time = 10.0

# Calculate the properties of the object:

calculatedVelocity = initialVelocity + (acceleration * time) #v = v0 + a*t
avgVelocity = initialVelocity + 0.5*(acceleration * time) #vAvg = v0 + 0.5*a*t
displacement = time * avgVelocity #x = v0*t + 0.5*a*(t^2) = vAvg * t


# Print the results:
print(f"time = {time} \n ")
print(f"velocity \t = {calculatedVelocity}")
print(f"average velocity = {avgVelocity}")
print(f"displacement \t = {displacement}")

quit() # to prevent terminal lockout