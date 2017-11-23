import math
class vector():
    x = 0.0
    y = 0.0
    z = 0.0

    def setvalues(s,a=0.0,b=0.0,c=0.0):
        s.x = a
        s.y = b
        s.z = c
    
    def dot(s,v):
        return s.x*v.x + s.y*v.y + s.z*v.z

    def length(s):
        return math.sqrt(s.dot(s))

    def add(s,v):
        s.x += v.x
        s.y += v.y
        s.z += v.z
    
    def väh(s,v):
        s.x -= v.x
        s.y -= v.y
        s.z -= v.z
    
    def skal(s,k):
        s.x *= k
        s.y *= k
        s.z *= k
    
    def cross(s,v):
        u = vector()
        a = s.y*v.z - s.z*v.y
        b = v.x*s.z - v.z*s.x
        c = s.x*v.y - v.x*s.y
        u.setvalues(a,b,c)
        return u

    def kulma(s,v):
        return math.acos(s.dot(v)/(s.length()*v.length()))
    
    def norm(s):
        s.skal(1/s.length())

    def copy(s):
        v = vector()
        v.setvalues(s.x,s.y,s.z)
        return v

    def values(s):
        return [s.x,s.y,s.z]
