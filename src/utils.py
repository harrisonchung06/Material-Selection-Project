from dataclasses import dataclass
import consts
import random

@dataclass 
class Material: 
    rho: float #Density
    E: float #Modulus of Elasticity 
    nu: float #Poisson's Ratio
    Sy: float #Yield Strength

@dataclass
class Design:
    mat: Material

    def critical_load(self) -> float:
        return (consts.PI**2 * self.mat.E * self.inertia()) / (consts.K * consts.L)**2
    
    def critical_stress(self) -> float:
        return consts.P/self.area()
    
    def buckling_condition(self) -> bool:
        fos = self.critical_load()/consts.P
        return consts.n > fos
    
    def yielding_condition(self) -> bool:
        fos = self.mat.Sy/self.critical_stress()
        return consts.n > fos
    
    def geometry_condition(self) -> bool:
        raise NotImplementedError
    
    def reflect_velocity(self, vel: 'Design') -> tuple['Design', 'Design']:
        raise NotImplementedError

@dataclass
class Circ_Design(Design):
    d_o: float
    t: float

    def area(self) -> float:
        if self.t >= self.d_o/2:
            self.t = 0.4*self.d_o
        A = consts.PI * self.t* (self.d_o-self.t)
        return A
    
    def vol(self) -> float:
        A = self.area()
        return A*consts.L

    def inertia(self) -> float:
        I = consts.PI/64*(self.d_o**4-(self.d_o-2*self.t)**4)
        return I
    
    def geometry_condition(self) -> bool:
        return self.d_o < self.t
    
    def __add__(self, design: 'Circ_Design') -> 'Circ_Design':
        return Circ_Design(
            mat=self.mat,
            d_o=self.d_o + design.d_o,
            t=self.t + design.t
        )
    
    def __sub__(self, design: 'Circ_Design') -> 'Circ_Design':
        return Circ_Design(
            mat=self.mat,
            d_o=self.d_o - design.d_o,
            t=self.t - design.t
        )
    
    def __scale__(self, c: float) -> 'Circ_Design':
        return Circ_Design(
            mat = self.mat, 
            d_o=self.d_o*c,
            t=self.t*c
        )
    
    def __mul__(self, c: list[float]) -> 'Circ_Design':
        return Circ_Design(
            mat = self.mat, 
            d_o=self.d_o*c[0],
            t=self.t*c[1]
        )

    def reflect(self, vel: 'Circ_Design') -> tuple['Circ_Design', 'Circ_Design']:
        lo, hi = consts.LIM

        if self.d_o < lo:
            self.d_o = lo
            vel.d_o = abs(vel.d_o)
        if self.d_o > hi:
            self.d_o = hi
            vel.d_o = -abs(vel.d_o)

        if self.t < lo:
            self.t = lo
            vel.t = abs(vel.t)
        if self.t > hi:
            self.t = hi
            vel.t = -abs(vel.t)
        return (self, vel)


@dataclass
class Rect_Design(Design):
    a_o: float
    b_o: float
    a_i: float
    b_i: float

    def area(self) -> float:
        if self.a_i >= self.a_o:
            self.a_i = 0.9*self.a_o
        if self.b_i >= self.b_o:
            self.b_i = 0.9*self.b_o
        A = self.a_o*self.b_o - self.a_i*self.b_i
        return A
    
    def vol(self)-> float:
        A = self.area()
        return A*consts.L

    def inertia(self) -> float:
        Ix = (self.a_o*self.b_o**3-self.a_i*self.b_i**3)/12
        Iy = (self.b_o*self.a_o**3-self.b_i*self.a_i**3)/12
        if Ix < Iy:
            return Ix
        else:
            return Iy
        
    def geometry_condition(self) -> bool:
        check_1 = self.a_o < self.a_i
        check_2 = self.b_o < self.b_i
        return check_1 or check_2
    
    def __add__(self, design: 'Rect_Design') -> 'Rect_Design':
        return Rect_Design(
            mat=self.mat,
            a_o=self.a_o + design.a_o,
            b_o=self.b_o + design.b_o,
            a_i=self.a_i + design.a_i,
            b_i=self.b_i + design.b_i
        )
    
    def __sub__(self, design: 'Rect_Design')-> 'Rect_Design':
        return Rect_Design(
            mat = self.mat, 
            a_o=self.a_o - design.a_o,
            b_o=self.b_o - design.b_o,
            a_i=self.a_i - design.a_i,
            b_i=self.b_i - design.b_i
        )
    
    def __scale__(self, c: float) -> 'Rect_Design':
        return Rect_Design(
            mat = self.mat, 
            a_o=self.a_o*c,
            b_o=self.b_o*c,
            a_i=self.a_i*c,
            b_i=self.b_i*c
        )
    
    def __mul__(self, c: list[float]) -> 'Rect_Design':
        return Rect_Design(
            mat = self.mat, 
            a_o=self.a_o*c[0],
            b_o=self.b_o*c[1],
            a_i=self.a_i*c[2],
            b_i=self.b_i*c[3]
        )
    
    def reflect(self, vel: 'Rect_Design') -> tuple['Rect_Design', 'Rect_Design']:
        lo, hi = consts.LIM

        for attr in ['a_o', 'b_o', 'a_i', 'b_i']:
            p = getattr(self, attr)
            v = getattr(vel, attr)
            if p < lo:
                setattr(self, attr, lo)
                setattr(vel, attr, abs(v))
            elif p > hi:
                setattr(self, attr, hi)
                setattr(vel, attr, -abs(v))

        return (self, vel)

'''
@dataclass
class Square_Design:
    a_o: float
    a_i: float
    mat: Material
'''

@dataclass
class Other_Design(Design):
    pass

def score(design: Design):
    geometry_penalty = 1e10*design.geometry_condition()
    buckling_penalty = consts.LAMBDA*design.buckling_condition()
    yielding_penalty = consts.LAMBDA*design.yielding_condition()
    return (design.mat.rho*design.vol())/design.critical_load()+buckling_penalty+yielding_penalty+geometry_penalty

@dataclass
class Particle:
    position: Design #Current position
    velocity: Design #Current velocity 
    best_position: Design #PB
    best_score: float #PB

