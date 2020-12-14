# CE-UY 3013 Computing In Civil Engineering Project: FEM - Cantilever beam


This program is intended to help engineering students with projects and assignments using the finite element method.

### FEM based analysis of cantilever beam:
It takes values s, p, xp, w, E, b, d of a cantilever beam and calculates the deflection, shear force and bending moments at each node.

** In future this method can be modified for other mboundary conditions for generalized solution for beams

#  Program inputs: 
* S: The length of the beam.
* P: The applied force acting on the beam.
* xp: The distance from the fixed end to the applied force P.
* w: The distributed load on the beam. Wself.
* E: The modulus of elasticity of the chosen material.
* b: The width of the beam.
* d: The depth of the beam.
* Please see Inputs/Sketch.png for input details

# Setup
In order to use the program u have to download the repository, navigate to the local directory and create a virtual environment with:
[$ python3 -m venv venv]

Then activate the virtual environment:
For Linux/Mac OS:
[$ source venv/bin/activate]

For Windows:
[> venv\Scripts\activate]

Install the required libraries needed for this program with:
[$ pip install -r requirements.txt]

#Detailed comments on how to use

# Solved Example. 
#s,p,xp,w,E,b,d == 10,200,3,50,200000000000,0.02,0.06

#   
* IDLE(3.9.1)
* Image does not open on googlecollab

