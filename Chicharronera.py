from manim import *

class Solution(Scene):
    def construct(self):

        title = Text("La chicharronera", font_size = 38, color = YELLOW)
        title_up = Text("Derivación", font_size = 40, color = BLUE)
        title_up.to_edge(UP)
        
        eq1 = MathTex(r" {a}x^2 + {b}x + {c} = 0")
        eq2 = MathTex(r" x^2 + \frac{b}{a}x + \frac{c}{a} = 0")
        eq3 = MathTex(r" x^2 + \frac{b}{a}x = - \frac{c}{a} ")
        eq4 = MathTex(r" x^2 + 2\left(\frac{b}{2a}\right)x \qquad  = - \frac{c}{a} \qquad ")
        eq5 = MathTex(r" x^2 + 2\left(\frac{b}{2a}\right)x + \left(\frac{b}{2a}\right)^{2} = - \frac{c}{a} + \left(\frac{b}{2a}\right)^{2} ")
        #, substrings_to_isolate = r"\left(\frac{b}{2a}\right)^{2}")
        # eq5.set_color_by_tex(r"\left(\frac{b}{2a}\right)^{2}", RED)
        eq6 = MathTex(r" \left(x + \frac{b}{2a}\right)^{2} = \frac{b^{2}- 4ac}{4a^{2}} ")
        eq7 = MathTex(r" x + \frac{b}{2a} = \pm  \frac{\sqrt{b^{2}- 4ac}}{2a} ")
        eq8 = MathTex(r" x =  \frac{-b \pm \sqrt{b^{2}- 4ac}}{2a} ")

        VGroup(title, eq8).arrange(DOWN)
        self.play(Write(title), FadeIn(eq8, shift=DOWN))
        self.wait()

        self.play(Transform(title, title_up),
                  LaggedStart(*[FadeOut(obj, shift = DOWN) for obj in eq8]))
        self.wait()
        
        self.add(eq1)
        self.play(TransformMatchingShapes(eq1, eq2))
        self.wait()
        self.play(TransformMatchingShapes(eq2, eq3))
        self.wait()
        self.play(TransformMatchingShapes(eq3, eq4))
        self.wait()
        self.play(TransformMatchingShapes(eq4, eq5))
        self.wait()
        self.play(TransformMatchingShapes(eq5, eq6))
        self.wait()
        self.play(TransformMatchingShapes(eq6, eq7))
        self.wait()
        self.play(TransformMatchingShapes(eq7, eq8))
        self.wait()
