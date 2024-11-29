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
            else:
                color = BLUE
            dot = Dot(np.array([np.random.choice(x_a),
                                np.random.choice(x_a), 0]),
                               radius = 0.08,
                               color = color)
            self.add(dot)
            self.wait(0.5)
