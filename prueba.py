from manim import *

class Hello(Scene):
    def construct(self):
        text = Text("Hola desde Manim")
        self.play(Write(text), run_time = 5)
