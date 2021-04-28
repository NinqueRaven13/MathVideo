from big_ol_pile_of_manim_imports import *

class LimitOfSequence(GraphScene):

    CONFIG={
        "y_max" : 1,
        "y_min" : 0,
        "X_max" : 10,
        "X_min" : 1,
        "y_axis_label": "$s_{N}$",
        "x_axis_label" : "$N$",    
    }
    
    def get_points_from_coords(self,coords):
        return [
            
            self.coords_to_point(px,py)
            
            for px,py in coords
        ]

    def get_dots_from_coords(self,coords,radius=0.1):
            points = self.get_points_from_coords(coords)
            dots = VGroup(*[
                Dot(radius=radius).move_to([px,py,pz])
                for px,py,pz in points
                ]
            )
            return dots

    def setup_axes(self):
        # Add this line
        GraphScene.setup_axes(self) 
        # Parametters of labels
        #   For x
        init_label_x = 1
        end_label_x = 8
        step_x = 1
        #   For y
        init_label_y = 0
        end_label_y = 1
        step_y = 0.25
        value = init_label_y
        values_y =[]
        while value <= end_label_y:
            a = (value, str(value))
            values_y.append(a)
            value += step_y
        # Position of labels
        #   For x
        self.x_axis.label_direction = DOWN #DOWN is default
        #   For y
        self.y_axis.label_direction = LEFT
        # Add labels to graph
        #   For x
        self.x_axis.add_numbers(*range(
                                        init_label_x,
                                        end_label_x+step_x,
                                        step_x
                                    ))
        #   For y
        self.y_axis_labels = VGroup()
        for y_val, y_tex in values_y:
            tex = TexMobject(y_tex) # Convert string to tex
            tex.scale(0.7) 
            tex.next_to(self.coords_to_point(0,y_val), LEFT) #Put tex on the position
            self.y_axis_labels.add(tex) #Add tex in graph
        
        #   Add Animation
        self.play(
            Write(self.y_axis_labels),
            ShowCreation(self.x_axis),
            ShowCreation(self.y_axis)
        )

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
        
        Areas = TexMobject(r"\\1","\\frac{1}{2}","\\frac{1}{4}","\\frac{1}{8}","\\frac{1}{16}",
                           "\\frac{1}{32}","\\frac{1}{64}")
        for i in range(len(Squares)):
            self.play(DrawBorderThenFill(Squares[i]),run_time = 2)
            valueOfArea = Areas[i].move_to(Squares[i].get_center()+np.array([0,0,0])).set_fill(BLACK, opacity=1)
            if i == 4 or i == 5:
                valueOfArea.scale(1-(2/i))
            elif i == 6:
                valueOfArea.scale((1/2)-(1/i))
            self.play(Write(valueOfArea))
        self.play(FadeOut(Areas),FadeOut(Squares))
        self.play(Write(formula))
        self.play(ApplyMethod(formula.move_to, UP))
        self.play(Write(formula1))
        self.play(FadeOut(formula))
        self.play(ApplyMethod(formula1.move_to, UP))
        self.play(Write(formula2))
        self.play(FadeOut(formula1))
        self.play(ApplyMethod(formula2.move_to, UP))
        self.play(Write(formula3))
        self.play(FadeOut(formula2))
        self.play(ApplyMethod(formula3.move_to, UP))
        self.play(FadeOut(formula3))