import sys
import numpy as np
from manim import *
# asd

sys.path.append("/home/night/Documents/UNIP/APS-UNIP-2sem/AlgoritimoFinal/")
from SES import SES
s = SES()
class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen


class NameOfAnimation(Scene):
    def construct(self):
        box = Rectangle(stroke_color=GREEN_C,
                        stroke_opacity=0.7, height=1, width=1, fill_opacity=0.5)

        self.add(box)
        self.play(box.animate.shift(RIGHT*2), run_time=2)


class myAnim1(Scene):

    def construct(self):
        box = Rectangle(stroke_color=RED_A,
                        fill_color=RED_B, height=1, width=1, fill_opacity=0)
        self.add(box)
        self.play(box.animate.shift(RIGHT*2), run_time=2)
        self.play(box.animate.shift(UP*3), run_time=2)
        self.play(box.animate.shift(DOWN*5+LEFT*5), run_time=2)
        self.play(box.animate.shift(UP*1.5+RIGHT*1), run_time=2)


class myAnim2(Scene):
    def construct(self):
        box = Rectangle(stroke_color=ManimColor("#81ff38"), height=1, width=1)
        triangle = Triangle(stroke_color=ManimColor(
            "#81ff38"))
        box.move_to(LEFT+UP)
        self.add(box)
        self.play(box.animate.shift(RIGHT*2), run_time=2)
        self.play(box.animate.shift(DOWN*2), run_time=2)
        self.play(box.animate.shift(LEFT*2), run_time=2)
        self.play(box.animate.shift(UP*2), run_time=2)
        self.play(Transform(box, triangle))


class myAnim3(Scene):
    def construct(self):
        axes = Axes(x_range=[-3, 3, 1], y_range=[-3, 3, 1],
                    x_length=6, y_length=6)
        axes.to_edge(LEFT, buff=0.5)
        circle = Circle(stroke_width=6, stroke_color=YELLOW,
                        fill_color=RED_C, fill_opacity=0.8)
        circle.width = 2
        circle.to_edge(DR, buff=0)

        triangle = Triangle(stroke_color=ORANGE,
                            stroke_width=10, fill_color=GREY)
        triangle.height = 2
        triangle.shift(DOWN*3+RIGHT*3)

        self.play(Write(axes))
        self.play(DrawBorderThenFill(circle))
        self.play(circle.animate.scale(0.5))
        self.play(Transform(circle, triangle), run_time=6)


def matrixToMobjectMatrix(matrix):
    for i in range(4):
        for j in range(4):
            matrix[i][j] = Text(matrix[i][j], color=BLUE)
    return matrix

class prot1(Scene):
    def construct(self):
        lblChave = Text("Chave: 1234")
        lblChave.to_edge(UL)
        self.play(Write(lblChave))
        
        lblChaveBinario = Text("Chave em binário:")
        lblChaveBinario.align_to(lblChave, DL)
        lblChaveBinario.shift(DOWN)
        self.play(Write(lblChaveBinario))
        
        txtChave = Text(lblChave.text[-4:], color=BLUE)
        txtChave.move_to(lblChave[-4:])
        self.play(Indicate(txtChave, color=BLUE))

        txtBinario = Text(s.textoParaStringBinaria(txtChave.text), color=BLUE)
        txtBinario.to_edge(UL)
        txtBinario.shift(DOWN*2)
        self.play(Transform(txtChave, txtBinario), run_time=3)
        txtChave.set_color(WHITE)
        self.play(FadeToColor(txtBinario, WHITE), run_time=0.5)
        txtBinario.set_color(WHITE)
        
        matrix = MobjectMatrix(
            [['00', '11', '00', '01'], ['00', '11', '00', '10'], ['00', '11', '00', '11'], ['00', '11', '01', '00']],
            element_to_mobject=Text)
        matrix.shift(DOWN*2)
        txtBinario.color=WHITE
        self.play(TransformMatchingShapes(txtBinario, matrix), run_time=4)
        
        lblChave0 = Text("Chave 0:")
        lblChave0.move_to(matrix.get_center()).align_to(matrix, UP*2).shift(UP*0.8)
        lblChave0.add_updater(lambda m: lblChave0.move_to(matrix.get_center()).align_to(matrix, UP*2).shift(UP*0.8))
        self.play(Write(lblChave0))
        #self.play(matrix.animate.shift(LEFT*4))
        
        headerGp = VGroup(lblChave, txtChave, txtBinario, lblChaveBinario)
        self.play(headerGp.animate.shift(UP*4), matrix.animate.move_to(ORIGIN))
        
        



