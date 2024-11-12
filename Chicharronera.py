from manim import *

class Solution(Scene):
    def construct(self):

        title = Text("La chicharronera", font_size = 38, color = YELLOW)
        title.shift(2*UP)
        title_up = Text("Derivación", font_size = 48, color = BLUE)
        title_up.to_edge(UP)

        sqr_term = MathTex("+", "\\left(", "{b \\over 2a}", "\\right)^2",
                           color = RED)
        sqr_term.to_edge(DOWN)

        terms = ["a", "x^2", "+", "b", "x", "+", "c", "=", "0", "2"]
        
        eq1 = MathTex("a", "x^2", "+", "b", "x", "+", "c", "=", "0",
                      substrings_to_isolate = terms)
        eq2 = MathTex("x^2", "+", "{b \\over a}", "x", "+", "{c \\over a}", "=", "0",
                      substrings_to_isolate = terms)
        eq3 = MathTex("x^2", "+", "{b \\over a}", "x", "=", "-", "{c \\over a}",
                      substrings_to_isolate = terms)
        eq4 = MathTex("x^2", "+", "2\\left(", "{b \\over 2a}", "\\right)", "x", "=",
                      "-", "{c \\over a}")
                      #substrings_to_isolate = terms)
        eq5 = MathTex("x^2", "+", "2\\left(", "{b \\over 2a}", "\\right)", "x",
                      "+", "\\left(", "{b \\over 2a}", "\\right)^2", "=", "-",
                      "{c \\over a}", "+", "\\left(", "{b \\over 2a}", "\\right)^2")
                      #substrings_to_isolate = terms )
        
        eq6 = MathTex("\\left(", "x", "+", "{b \\over 2a}", "\\right)^2", "=", "{b^{2}- 4ac \\over 4a^{2}}")
        eq7 = MathTex("x", "+", "{b \\over 2a}", "=", "\\pm", "{\\sqrt{b^{2}- 4ac} \\over 2a}")
        eq8 = MathTex("x", "=",  "{-b \\pm \\sqrt{b^{2}- 4ac} \\over 2a}")

        VGroup(title, eq8)
        self.play(Write(title))

        self.play(FadeIn(eq8, shift=DOWN))
        self.wait()
        
        self.play(Transform(title, title_up),
                  LaggedStart(*[FadeOut(obj, shift = DOWN) for obj in eq8]))

        self.play(FadeIn(eq1, shift = UP))
        self.wait(1.5)
        self.play(TransformMatchingTex(eq1, eq2))
        self.wait(1.5)
        self.play(TransformMatchingTex(eq2, eq3))
        self.wait(1.5)
        self.play(TransformMatchingShapes(eq3, eq4))
        self.wait(1.5)

        self.play(ReplacementTransform(eq4[0:6], eq5[0:6]),
                  ReplacementTransform(eq4[6], eq5[10]),
                  ReplacementTransform(eq4[7:], eq5[11:13]))
        self.wait(1.5)
        
        self.play(FadeIn(sqr_term))
        self.wait(1.5)

        self.play(ReplacementTransform(sqr_term[0:4].copy(), eq5[6:10]),
                  ReplacementTransform(sqr_term[0:4], eq5[13:17]))
        self.wait(1.5)

        self.play(TransformMatchingShapes(eq5[:], eq6[:]))
        self.wait(1.5)
        self.play(TransformMatchingShapes(eq6[:], eq7[:]))
        self.wait(1.5)
        self.play(TransformMatchingShapes(eq7[:], eq8[:]))
        self.wait(1.5)

class quadratic(Scene):
    def construct(self):

        isolate = ["x^2","x","a","c","-","=","b"]

        add = MathTex("+","\\left(","{ b \\over 2a }","\\right)^2",
                     # substrings_to_isolate = ["b","2a","\\left(","\\right)"]
                      ).to_edge(2*UP).set_color(YELLOW)
        
        eq1 = MathTex("a","x^2","+","b","x","+","c","=","0",
                      substrings_to_isolate = [*isolate,"0"]
                      )
        eq1copy = MathTex("ax^2 + bx + c = 0")[0]
        eq2 = MathTex("a","x^2","+","b","x","=","-","c",
                      substrings_to_isolate = [*isolate])
        eq2copy = MathTex("ax^2+bx=-c")[0]
        eq3 = MathTex("x^2","+","{ b \\over a }","x", #0 1 2 3
                      "=",
                      "-","{ c \\over a }") # 5 6
        eq3b = MathTex("x^2","+","{ b \\over a }","x", # 0 1 2 3
                       "=", # 4
                       "-","{ c \\over a }", # 5 6
                       substrings_to_isolate=isolate)
        eq4 = MathTex("x^2","+","{ b \\over a }","x","+", #0 1 2 3 4
                      "\\left(","{ b \\over 2a }","\\right)^2", # 5 6 7  
                      "=", # 8
                      "\\left(","{ b \\over 2a }","\\right)^2", # 9 10 11
                      "-","{ c \\over a }", # 12 13
                      #substrings_to_isolate=[*isolate,
                      #                       "\\left(","\right)","2a"]
                      )
        eq5 = MathTex("\\left(","x", "+", "{ b \\over 2a }","\\right)^2", # 0 1 2 3 4
                      "=", # 5
                      "\\left(","{ b \\over 2a }","\\right)^2", # 6 7 8
                      "-","{ c \\over a }" # 9 10
                      )
        eq5b=MathTex("\\left(","x", "+", "{ b \\over 2a }","\\right)^2", # 0 1 2 3 4
                      "=", # 5
                      "\\left(","{ b \\over 2a }","\\right)^2", # 6 7 8
                      "-","{ c \\over a }", # 9 10
                      substrings_to_isolate=[])
        eq6 = MathTex("\\left(","x", "+", "{ b \\over 2a }","\\right)^2", # 0 1 2 3 4
                      "=", # 5
                      "{ b^2 \\over 4a^2 }", # 6 
                      "-","{ c \\over a }"#, # 7 8
                      #substrings_to_isolate=isolate
                      )
     
        self.play(Write(eq1))
        self.wait()
        self.play(TransformMatchingTex(eq1,eq2))
        self.wait()
        self.play(TransformMatchingTex(eq2,eq3b))
        self.wait()
        self.clear()

        self.play(ReplacementTransform(eq3[0:4],eq4[0:4]),
                  ReplacementTransform(eq3[4],eq4[8]),
                  ReplacementTransform(eq3[5:7],eq4[12:14])
                  )
        self.wait()
        
        self.play(FadeIn(add))
        self.wait()
        self.play(ReplacementTransform(add[0],eq4[4]),
                  ReplacementTransform(add[1].copy(),eq4[5]),
                  ReplacementTransform(add[2].copy(),eq4[6]),
                  ReplacementTransform(add[3].copy(),eq4[7]),
                  ReplacementTransform(add[1],eq4[9]),
                  ReplacementTransform(add[2],eq4[10]),
                  ReplacementTransform(add[3],eq4[11])
                
                  )
        self.wait()

        nothing = MathTex(".")
        self.play(TransformMatchingTex(eq4,eq5))
        self.wait()
        self.play(ReplacementTransform(eq5[8][1],eq6[6][1]),ReplacementTransform(eq5[6][0],nothing[0]))
        self.play(ReplacementTransform(eq5,eq6))
        self.wait()
        #self.clear()
