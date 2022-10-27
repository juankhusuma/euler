from manim import *
from typing import Union


class EquationScene(Scene):
    path = "./math/1.tex"
    wait_time = 1

    def construct(self):
        r_eq: "list[MathTex]" = []
        r_dc: "list[Union[Tex, None]]" = []
        with open(self.path, "r") as tex:
            for line in tex:
                line = line.strip()
                equation, desc = [x.strip() for x in line.split("|")]
                r_eq.append(MathTex(*equation.split()))
                if desc:
                    r_dc.append(Tex(desc.strip()).scale(0.4).set_color("#eee"))
                r_dc.append(None)

        r_eq = [x.scale(0.8) for x in r_eq]
        self.play(Write(r_eq[0]))
        for line, desc in zip(r_eq[1:], r_dc[1:]):
            desc and self.play(FadeIn(desc.next_to(r_eq[0], DOWN*2)))
            self.play(Transform(r_eq[0], line))
            self.wait(self.wait_time)
            desc and self.play(FadeOut(desc))

        self.wait()
