import sys
import numpy as np
from manim import *
config.disable_caching = True
sys.path.append("/home/night/Documents/UNIP/APS-UNIP-2sem/AlgoritimoFinal/")
from SES import SES
s = SES()


class chave0(Scene):
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
            s.blocoParaMatriz(txtBinario.text),
            element_to_mobject=Text)
        matrix.shift(DOWN*2)
        txtBinario.color=WHITE
        self.play(TransformMatchingShapes(txtBinario, matrix), run_time=4)
        
        lblChave0 = Text("Chave 0:")
        lblChave0.move_to(matrix.get_center()).align_to(matrix, UP*2).shift(UP*0.8)
        lblChave0.add_updater(lambda m: lblChave0.move_to(matrix.get_center()).align_to(matrix, UP*2).shift(UP*0.8))
        self.play(Write(lblChave0))
        headerGp = VGroup(lblChave, txtChave, txtBinario, lblChaveBinario)
        self.play(headerGp.animate.shift(UP*4), matrix.animate.move_to(ORIGIN))

# Importante: No Manim a lógica do descocamento comum e reverso é invertida
def GPdnl0(matrix: MobjectMatrix) ->VGroup:
    mobMatrix = matrix.get_mob_matrix()
    gp = VGroup(
        mobMatrix[2][3],
        mobMatrix[3][1],
        mobMatrix[2][0],
        mobMatrix[0][1],
        mobMatrix[1][0],
        mobMatrix[2][1],
        mobMatrix[3][2],
        mobMatrix[0][3],
        mobMatrix[1][1],
        mobMatrix[1][3],
        mobMatrix[2][2],
        mobMatrix[3][0],
        mobMatrix[0][2],
        mobMatrix[3][3],
        mobMatrix[1][2],
        mobMatrix[0][0]
    )
    return gp




def setPairsColors(matrix: MobjectMatrix):
    animations = []
    for pair in matrix.get_entries():
        if pair.text == "00":
            animations.append(pair.animate.set_color(GREEN_C))
            #pair.set_color(GREEN_C)
        elif pair.text == "01":
            animations.append(pair.animate.set_color(RED_C))
            #pair.set_color(RED_C)
        elif pair.text == "10":
            animations.append(pair.animate.set_color(YELLOW_C))
            #pair.set_color(YELLOW_C)
        else:
            animations.append(pair.animate.set_color(BLUE_C))
            #pair.set_color(BLUE_C)
    return animations

class expansaoChave(Scene):
    def construct(self):
        # Criar matriz da chave 0
        chaveString = "1234"
        matrixChave1 = MobjectMatrix(
        s.blocoParaMatriz(s.textoParaStringBinaria(chaveString)),
        element_to_mobject=Text)
        
        
        # Adicionar label da chave 0
        lblChave0 = Text("Chave 0:")
        lblChave0.move_to(matrixChave1.get_center()).align_to(matrixChave1, UP*2).shift(UP*0.8)
        self.add(lblChave0, matrixChave1)
        self.play(*setPairsColors(matrixChave1))
        
        # Adicionar título do deslocamento não linear 0
        lblExpansao = Text("Expansão de Chave")
        lblExpansao.to_edge(UP)
        self.play(Write(lblExpansao))
        
        # Agrupar matriz com o label e mover para esquerda
        gpChave0 = VGroup(matrixChave1, lblChave0)
        self.play(gpChave0.animate.scale(0.9).to_edge(LEFT))
        
        
        
        # Copiar a matriz e mover para direita
        matrixChave1 = matrixChave1.copy()
        self.add(matrixChave1)
        self.play(matrixChave1.animate.to_edge(RIGHT))
        
        # Criar label Deslocamento Não Linear 0
        lblDeslocamento = Text("Deslocamento Não Linear 0")
        lblDeslocamento.move_to(matrixChave1.get_center()).align_to(matrixChave1, UP*2).shift(UP*0.8).scale(0.6)
        self.play(Write(lblDeslocamento))
        
        # Animação DNL0
        gpdnl0 = GPdnl0(matrixChave1)
        
        arrL = [0,1,3,0,3,2,1,1,0,3,2,1,0,2,3,2]
        arrR = [0,2,3,2,0,2,3,1,3,2,1,0,1,0,1,3]

        mobMatrix = matrixChave1.get_mob_matrix()
        previous = mobMatrix[arrL[0]][arrR[0]]
        path = TracedPath((lambda: previous.get_center() + IN), stroke_color=GRAY, stroke_width=4, stroke_opacity=0.6)
        
        self.add(path)
        for i in range(0, len(arrL)-1):
            gp = VGroup(previous, mobMatrix[arrL[i+1]][arrR[i+1]])
            self.play(CyclicReplace(*gp, path_arc=0), run_time = 1.5)

        path.clear_updaters()
        
        
        # Mover path e label DNL0 para o centro
        lblDnl0 = Text("DNL0").scale(0.8).move_to(ORIGIN).shift(UP*1.4)
        self.play(path.animate.move_to(ORIGIN).scale(0.8), Transform(lblDeslocamento, lblDnl0))
        
        # Criar label Pré-Chave 1        
        lblChave1 = Text("Pré-Chave 1")
        lblChave1.move_to(matrixChave1.get_center()).align_to(matrixChave1, UP*2).shift(UP*0.8)
        self.play(Write(lblChave1))
        
        # Agrupar chaves e mover para esquerda
        gpChave1 = VGroup(matrixChave1, lblChave1)
        
        gpChaves = VGroup(gpChave0, gpChave1)
        
        self.play(gpChaves.animate.shift(LEFT*8.5))
        
        # Copiar chave1 e mover para direita
        matrixChave2 = matrixChave1.copy()
        self.add(matrixChave2)
        self.play(matrixChave2.animate.to_edge(RIGHT))
        
        # Executar DNL0
        gp = GPdnl0(matrixChave2)
        self.play(CyclicReplace(*gp, path_arc=0, run_time = 4), Indicate(path, scale_factor=1.1, color=PURE_GREEN, run_time=1))
        
        # Criar label Pré-Chave 2
        lblChave2 = Text("Pré-Chave 2")
        lblChave2.move_to(matrixChave2.get_center()).align_to(matrixChave2, UP*2).shift(UP*0.8)
        self.play(Write(lblChave2), path.animate.set_stroke(GREY_B, opacity=1))
        
        # Agrupar chaves e mover para esquerda
        gpChaves += VGroup(matrixChave2, lblChave2)
        
        self.play(gpChaves.animate.shift(LEFT*8.5))
        
        # Copiar chave2 e mover para direita
        matrixChave3 = matrixChave2.copy()
        self.add(matrixChave3)
        self.play(matrixChave3.animate.to_edge(RIGHT))
        
        # Executar DNL0
        gp = GPdnl0(matrixChave3)
        self.play(CyclicReplace(*gp, path_arc=0, run_time = 4), Indicate(path, scale_factor=1.1, color=PURE_GREEN, run_time=1))
        
        lblChave3 = Text("Pré-Chave 3")
        lblChave3.move_to(matrixChave3.get_center()).align_to(matrixChave3, UP*2).shift(UP*0.8)
        self.play(Write(lblChave3), path.animate.set_stroke(GREY_B, opacity=1))
        
        # Agrupar chaves e mover para esquerda
        gpChaves += VGroup(matrixChave3, lblChave3)
        
        self.play(gpChaves.animate.shift(LEFT*8.5))
        
        # Copiar chave3 e mover para direita
        matrixChave4 = matrixChave3.copy()
        self.add(matrixChave4)
        self.play(matrixChave4.animate.to_edge(RIGHT))
        
        # Executar DNL0
        gp = GPdnl0(matrixChave4)
        self.play(CyclicReplace(*gp, path_arc=0, run_time = 4), Indicate(path, scale_factor=1.1, color=PURE_GREEN, run_time=1))
        
        # Criar label Pré-Chave 4
        lblChave4 = Text("Pré-Chave 4")
        lblChave4.move_to(matrixChave4.get_center()).align_to(matrixChave4, UP*2).shift(UP*0.8)
        self.play(Write(lblChave4), path.animate.set_stroke(GREY_B, opacity=1))
        
        # Agrupar chaves
        gpChaves += VGroup(matrixChave4, lblChave4)
        
        # Esconder o path e o label do deslocamento não linear
        gpNaoChave = VGroup(path, lblDeslocamento)
        self.play(gpNaoChave.animate.fade(1))
        
        self.play(gpChaves.animate.arrange_in_grid(1).move_to(ORIGIN).scale(0.55))
        
        self.wait(1)
        
        # Atualizar título para XOR entre Chave 0 e Pré-Chaves
        lblExpansaoXor = Text("Expansão de Chave: XOR entre Chave 0 e Pré-Chaves").scale(0.8).to_edge(UP)
        lblExpansaoXor[16:].set_color(BLUE)
        
        self.play(TransformMatchingShapes(lblExpansao, lblExpansaoXor))
        
        
        novaMatrixChave1 = matrixChave1.copy()
        novaMatrixChave2 = matrixChave2.copy()
        novaMatrixChave3 = matrixChave3.copy()
        novaMatrixChave4 = matrixChave4.copy()
        gpNovasChaves = VGroup(novaMatrixChave1, novaMatrixChave2, novaMatrixChave3, novaMatrixChave4)
        
        
        # Mover o grupo de chaves para embaixo do título
        gpPreChaves = gpChaves - gpChave0
        
        self.play(gpPreChaves.animate.shift(UP*1.9))

        novaMatrixChave1[0][0].text = "XX"
        self.play(Write(novaMatrixChave1))
        
class dnl0(Scene):
    def construct(self):
        # make a dot moving from left to right while tracing it's path
        dot = Dot(color=BLUE)
        path = TracedPath(dot.get_center, stroke_color=BLUE)
        self.add(dot, path)
        self.play(dot.animate.shift(RIGHT*2))
        self.play(dot.animate.shift(UP*2))
        self.play(dot.animate.shift(LEFT*2))
        
        
