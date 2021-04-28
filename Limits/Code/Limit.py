from big_ol_pile_of_manim_imports import *

class LimitOfSequence(GraphScene):

    def construct(self):
        square = Square()
        square.scale(2)
        square.set_fill(WHITE, opacity=1)
        
        square1 = Polygon(np.array([-2,2,0]),np.array([-2,-2,0]),np.array([0,-2,0]),np.array([0,2,0]))
        square1.set_fill(GREEN, opacity=1)
        square2 = Polygon(np.array([0,-2,0]),np.array([2,-2,0]),np.array([2,0,0]),np.array([0,0,0]))
        square2.set_fill(ORANGE, opacity=1)
        square3 = Polygon(np.array([0,0,0]),np.array([0,2,0]),np.array([1,2,0]),np.array([1,0,0]))
        square3.set_fill(BLUE, opacity=1)
        square4 = Polygon(np.array([1,0,0]),np.array([2,0,0]),np.array([2,1,0]),np.array([1,1,0]))
        square4.set_fill(RED, opacity=1)
        square5 = Polygon(np.array([1,1,0]),np.array([1,2,0]),np.array([1.5, 2,0]),np.array([1.5,1,0]))
        square5.set_fill(GREEN, opacity=1)
        square6 = Polygon(np.array([1.5,1,0]),np.array([1.5,1.5,0]),np.array([ 2, 1.5,0]),np.array([2,1,0]))
        square6.set_fill(ORANGE, opacity=1)
        Squares = VGroup(square,square1,square2,square3,square4,square5,square6)