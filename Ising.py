from manim import *
import numpy as np

class Ising_grid(Scene):
    def construct(self):
        x_a = np.arange(-3, 4)
        for x in x_a:
            for y in  x_a:
                dot = Dot(np.array([x, y, 0]) , radius = 0.08)
                self.add(dot)

        dot = Dot(point = ORIGIN, radius = 0.08, color = YELLOW)
        self.add(dot)
        self.wait(0.5)

        samples = 10
        for s in range(samples):
            r = np.random.rand()
            if r < 0.5:
                color = RED
                arr = "UP"
            else:
                color = BLUE
                arr = "DOWN"
            x_r = np.random.choice(x_a)
            y_r = np.random.choice(x_a)
            xy_p = Text(f"({x_r},{y_r})")
            xy_arr = Text(f"{arr}", color = color)
            xy_p.to_corner(UP + LEFT)
            xy_arr.to_corner(2.5*UP + LEFT).scale(0.8)
            dot = Dot(np.array([x_r, y_r, 0]), radius = 0.08, color = color)
            self.add(dot)
            self.add(xy_p, xy_arr)
            self.wait(0.8)
            self.remove(xy_p, xy_arr)

class rand_choice(Scene):
    def construct(self):
        samples = 5
        r_l = np.random.rand(samples)

        for r in r_l:
            r_n = MathTex("%.5f" % r)
            self.add(r_n)
            self.wait(0.2)
            self.remove(r_n)
            self.wait(0.2)

        r_0 = "0.68348"
        r_choice = MathTex(f"{r_0}")
        self.add(r_choice)
        self.wait(0.5)

        exp = "e^{\\Delta S}"
        eq1 = MathTex(f"{exp}")
        eq1.shift(UP)
        self.play(FadeIn(eq1))
        self.wait(0.5)

        terms = [r_0, "<" , exp]
        
        eq2 = MathTex(r_0, "<", exp, substrings_to_isolate = terms)
        eq2.set_color_by_tex("<", RED)

        self.play(TransformMatchingShapes(r_choice, eq2[0]),
                  TransformMatchingShapes(eq1, eq2[2]))
        self.wait(0.5)

        self.add(eq2)
        self.wait(0.5)

        #dot = Dot(point = ORIGIN, radius = 0.08, color = YELLOW)
        #self.add(dot)
        #self.wait(0.5) 

        #self.add(MathTex("<", color = RED).shift(ORIGIN))
        #self.wait(0.5)
