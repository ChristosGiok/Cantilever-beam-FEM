# CE-UY 3013 Computing In Civil Engineering Project: FEM - Cantilever beam


This program is intended to help engineering students with projects and assignments.

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
Install the required libraries needed:
[$ pip install -r requirements.txt]



# Example inputs. 
#s,p,xp,w,E,b,d == 10,200,3,50,200000000000,0.02,0.06

#   
* IDLE(3.9.1) prf


