from manim import *

def get_sub_indexes(tex):
    ni = VGroup()
    colors = [RED,TEAL,GREEN,BLUE,PURPLE]
    for i in range(len(tex)):
        n = Text(f"{i}",color=colors[i%len(colors)]).scale(0.5)
        n.next_to(tex[i].set_color(colors[i%len(colors)]),DOWN,buff=0.01)
        ni.add(n)
    return ni

class Solution(Scene):
    def construct(self):

        title = Text("Teorema de Pitágoras", font_size = 35, color = YELLOW)
        title.shift(2*UP)
        #title_up = Text("Derivación", font_size = 48, color = BLUE)
        #title_up.to_edge(UP)

        terms = ["a^2", "a", "+", "b^2", "b", "=", "c^2", "c"]
        
        eq1 = MathTex("a^2", "+", "b^2", "=", "c^2",
                      substrings_to_isolate = terms).scale(0.8)
        eq2 = MathTex("\\sqrt{a^2 + b^2}", "=", "c",
                      substrings_to_isolate = terms).scale(0.8)

        #eq8 = MathTex("x", "=",
                      #"{-b \\pm \\sqrt{b^{2}- 4ac} \\over 2a}").scale(0.8)

        #VGroup(title, eq8)
        self.play(Write(title))

        #self.play(FadeIn(eq8, shift = DOWN))
        #self.wait()
        
        #self.play(Transform(title, title_up),
                  #LaggedStart(*[FadeOut(obj, shift = DOWN) for obj in eq8]))

        self.play(FadeIn(eq1, shift = UP))
        self.wait(1.5)
        self.play(TransformMatchingTex(eq1, eq2))
        self.wait(1.5)

class pitagoras_indx(Scene):
    def construct(self):

        eq1 = MathTex("a^2 + b^2 = c^2")[0]
        eq2 = MathTex("a^2 = c^2 - b^2")[0]
        eq3 = MathTex("a = \\sqrt{c^2 - b^2}")[0]

        group = VGroup(eq1,eq2,eq3).arrange(DOWN,buff = 1).scale(1.5)
        
        eq1_i = get_sub_indexes(eq1)
        eq2_i = get_sub_indexes(eq2)
        eq3_i = get_sub_indexes(eq3)
        
        
        self.add(eq1,eq1_i,eq2,eq2_i,eq3,eq3_i)
        
def Transform_by_term( eq_1, eq_2, indices):
    # Try replacing "ReplacementTransform" with "FadeTransform"
    transform_list = []
    for i,j in zip(*indices):
        if type(i) is int:
            transform_list.append(ReplacementTransform(eq_1[i],eq_2[j]))
        elif i[0]=="f":
            transform_list.append(FadeTransform(eq_1[int(i[1:])],eq_2[j]))
        else:
            transform_list.append(ReplacementTransform(eq_1[int(i[1:])].copy(),eq_2[j]))
    return transform_list
        
class pitagoras(Scene):
    def construct(self):

        eq1 = MathTex("a^2 + b^2 = c^2")[0]
        eq2 = MathTex("a^2 = c^2 - b^2")[0]
        eq3 = MathTex("a = \\sqrt{c^2 - b^2}")[0]

        
        transform_indices_1_2 = [[0,1,2,3,4,5,6,7],
                                 [0,1,5,6,7,2,3,4]]
        
        transform_indices_2_3 = [[0,1,"r1",2,3,4,5,6,7 ],
                                 [0,2,3,   1,4,5,6,7,8]]
        
        self.play(*[Transform_by_term(eq1, eq2, transform_indices_1_2)],
                    run_time=3)
        self.wait()
        
        self.play(*[Transform_by_term(eq2, eq3, transform_indices_2_3)],
                  run_time=3)
        self.wait()
        #self.add(eq1)
        #self.wait(2)
