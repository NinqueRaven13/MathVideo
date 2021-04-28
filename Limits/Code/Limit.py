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

        formula = TexMobject(r"s_{\infty} =\sum_{n=1}^{\infty}{\frac{1}{2^{n}}} = {\frac{1}{2}}+{\frac{1}{4}}+{\frac{1}{8}}+...+{\frac{1}{2^{n}}}+...")
        formula1 = TexMobject(r"s_{1} = {\frac{1}{2}} = 0.5")
        formula2 = TexMobject(r"s_{2} = {\frac{1}{2}}+{\frac{1}{4}} = 0.75")
        formula3 = TexMobject(r"s_{3} = {\frac{1}{2}}+{\frac{1}{4}}+{\frac{1}{8}} = 0.875")
        limitDefinition = TexMobject(r"\forall",r"\epsilon>0 ",r"\quad  ", r" \exists",r" N",r":",r" \forall",r" k",r" >",r"N",r"\quad  ", r" |",r"{x}_{k}"r"-",r"{a}",r"| ",r"<", r"\epsilon")

        Colors = [ORANGE, BLUE, YELLOW]

        epsilon_value = ValueTracker(1)
        epsilon_is = TexMobject(r"\epsilon=")
        epsilon_tex = DecimalNumber(epsilon_value.get_value()).add_updater(lambda v: v.set_value(epsilon_value.get_value()))

        for i in range(len(limitDefinition)):
            a = i%3
            limitDefinition[i].set_fill(Colors[a])

        a = 2
        previous = -1
        coords = []
        for i in range(8):
            if i == 0:
                b = 2**(-1*i)
                previous += b
            else:
                b = 2**(-1*i)
                previous += b
                coords.append(( i ,previous))