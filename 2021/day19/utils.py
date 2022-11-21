from math import cos,sin,pi
import numpy as np


def Rx(theta):
    return np.matrix([[1, 0, 0],
                      [0, cos(theta), -sin(theta)],
                      [0, sin(theta), cos(theta)]])


def Ry(theta):
    return np.matrix([[cos(theta), 0, sin(theta)],
                      [0, 1, 0],
                      [-sin(theta), 0, cos(theta)]])


def Rz(theta):
    return np.matrix([[cos(theta), -sin(theta), 0],
                      [sin(theta), cos(theta), 0],
                      [0, 0, 1]])


def R(psi, theta, phi):
    return Rz(psi) * Ry(theta) * Rx(phi)

def getRotations():
    Rotations = []
    for i in range(4):
        for j in range(4):
            for k in range(4):
                phi   = i*np.pi/2
                theta = j*np.pi/2
                psi   = k*np.pi/2
                Rot = np.array(np.round(R(psi,theta,phi),decimals=2),dtype=int)
                unique = True
                for Rot0 in Rotations:
                    if (Rot==Rot0).all():
                        unique = False
                if unique:
                    Rotations.append(Rot)
    return Rotations

Rotations = getRotations()

