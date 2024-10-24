from manim import *
import numpy as np

class EF_graphs(Scene):
    def construct(self):

        title = Title("Finkelstein Diagram (ingoing coordinates)",
                      include_underline = False,
                      font_size = 40)
        
        axes = Axes(
                    x_range = [2.1, 5 + 2.1, 1],
                    y_range = [-10, 10, 2],
                    x_length = 10,
                    y_length = 4,
                    tips = False,
        )

        labels = axes.get_axis_labels(x_label = MathTex("r"),
                                    y_label = MathTex(r"t_{\ast}=v-r"))

        plots = VGroup()
        for n in np.arange(0, 50, 10):
            plots += axes.plot(lambda r: -2*r + n,
                               color = RED)
        #for m in np.arange(0, 100, 10):
            plots += axes.plot(lambda r: 2*r + 4*np.log(np.abs((r - 2)/2)) + n,
                               color = BLUE)
            #plots += axes.plot(lambda r: 2*r + 4*np.log((2 -r)/2) + n,
                               #color = BLUE)

        self.play(Write(title))
        self.play(Create(axes), Create(labels))
        self.play(AnimationGroup(*[Create(plot) for plot in plots],
                                 lag_ratio = 0.05))
