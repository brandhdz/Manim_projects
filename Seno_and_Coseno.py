from manim import *

class PlotSenoCoseno(Scene):
    def construct(self):
        plot_axes = Axes(
            x_range=[0, 2*PI, 1.0],
            y_range=[-1, 1, 1.0],
            x_length=9,
            y_length=6,
            axis_config={
                "numbers_to_include": np.arange(0, 2*PI, 0.5),
                "font_size": 24,
            },
            tips=False,
        )

        y_label = plot_axes.get_y_axis_label("y", edge=LEFT, direction=LEFT)
        x_label = plot_axes.get_x_axis_label("x")
        plot_labels = VGroup(x_label, y_label)

        plots = VGroup()
        plots += plot_axes.plot(lambda x: np.sin(x), color=WHITE)
        plots += plot_axes.plot(lambda x: np.cos(x), color=WHITE, use_smoothing=False)

        extras = VGroup()
        extras += plot_axes.get_horizontal_line(plot_axes.c2p(2*PI, 1, 0), color=BLUE)
        extras += plot_axes.get_horizontal_line(plot_axes.c2p(2*PI, -1, 0), color=BLUE)
        extras += Dot(point=plot_axes.c2p(PI/4, np.sin(PI/4), 0), color=YELLOW)
        extras += Dot(point=plot_axes.c2p(5*PI/4, np.sin(5*PI/4), 0), color=YELLOW)
        title = Title(
            r"Graphs of $\sin(x)$ and $\cos(x)$ and their intersections",
            include_underline=False,
            font_size=40,
        )
        
        self.play(Write(title))
        self.play(Create(plot_axes), Create(plot_labels), Create(extras))
        self.play(AnimationGroup(*[Create(plot) for plot in plots], lag_ratio=0.05))

class PlotSenotoCoseno(Scene):
    def construct(self):
        plot_axes = Axes(
            x_range=[0, 2*PI, 1.0],
            y_range=[-1, 1, 1.0],
            x_length=9,
            y_length=6,
            axis_config={
                "numbers_to_include": np.arange(0, 2*PI, 0.5),
                "font_size": 24,
            },
            tips=False,
        )

        y_label = plot_axes.get_y_axis_label("y", edge=LEFT, direction=LEFT, buff=0.4)
        x_label = plot_axes.get_x_axis_label("x", buff=0.4)
        plot_labels = VGroup(x_label, y_label)

        plot_s = plot_axes.plot(lambda x: np.sin(x), color=WHITE)
        plot_c = plot_axes.plot(lambda x: np.cos(x), color=WHITE, use_smoothing=False)

        extras = VGroup()
        extras += plot_axes.get_horizontal_line(plot_axes.c2p(2*PI, 1, 0), color=BLUE)
        extras += plot_axes.get_horizontal_line(plot_axes.c2p(2*PI, -1, 0), color=BLUE)
        extras += Dot(point=plot_axes.c2p(PI/4, np.sin(PI/4), 0), color=YELLOW)
        extras += Dot(point=plot_axes.c2p(5*PI/4, np.sin(5*PI/4), 0), color=YELLOW)
        title = Title(
            r"Graph of $\sin(x)$ to $\cos(x)$",
            include_underline=False,
            font_size=40,
        )
        
        self.play(Write(title))
        self.play(Create(plot_axes), Create(plot_labels), Create(extras))
        self.play(Create(plot_s))
        self.wait()

        self.play(Transform(plot_s, plot_c))
        self.wait()
