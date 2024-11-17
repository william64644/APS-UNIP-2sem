
import numpy as np
from manim import *
config.disable_caching = True



# Note for future self: In Manim, the logic of common and reverse displacement is inverted
def GPNonLinearShift0(matrix: MobjectMatrix) -> VGroup:
    mobMatrix = matrix.get_mob_matrix()
    group = VGroup(
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
    return group


def setPairColors(matrix: MobjectMatrix):
    animations = []
    for pair in matrix.get_entries():
        if pair.text == "00":
            animations.append(pair.animate.set_color(GREEN_C))
        elif pair.text == "01":
            animations.append(pair.animate.set_color(RED_C))
        elif pair.text == "10":
            animations.append(pair.animate.set_color(YELLOW_C))
        else:
            animations.append(pair.animate.set_color(BLUE_C))
    return animations

def blockToMatrix(block):
        # Divide the 32-bit block into a 4x4 matrix with 2-bit elements
        matrix = []
        for i in range(0, 32, 8):
            row = [block[i+j:i+j+2] for j in range(0, 8, 2)]
            matrix.append(row)
        return matrix
    
def textToBinaryString(text):
        # Converts each character to its 8-bit binary value
        binary_string = ''
        for char in text:
            binary_8bits = format(ord(char), '08b')
            binary_string += binary_8bits
        return binary_string
    
def xor2Bits(bitString1, bitString2):
    xor_result = ''
    for k in range(2):
        bit_xor = str(int(bitString1[k]) ^ int(bitString2[k]))
        xor_result += bit_xor
    return xor_result

def calculateXORMatrices(matrix1, matrix2):
    # Performs element-wise XOR operation between two 4x4 matrices of 2-bit elements
    result_matrix = []
    for i in range(4):
        xor_row = []
        for j in range(4):
            xor_bits = xor2Bits(matrix1[i][j], matrix2[i][j])
            xor_row.append(xor_bits)
        result_matrix.append(xor_row)
    return result_matrix

def update_matrix_cell(matrix: MobjectMatrix, row: int, col: int, new_text: str):
    mob_matrix = matrix.get_mob_matrix()
    old_cell = mob_matrix[row][col]
    new_cell = Text(new_text).move_to(old_cell.get_center())  # Ensure new cell aligns with the old one
    matrix.add(new_cell)  # Add the new cell to the matrix group
    matrix.remove(old_cell)  # Remove the old cell
    return new_cell


def animate_xor(self: Scene, matrix1: MobjectMatrix, matrix2: MobjectMatrix, result_matrix: MobjectMatrix):
    mob_matrix1 = matrix1.get_mob_matrix()
    mob_matrix2 = matrix2.get_mob_matrix()
    mob_result = result_matrix.get_mob_matrix()

    run_time = 2.0  # Start with a slow animation
    arrL = [0, 1, 3, 0, 3, 2, 1, 1, 0, 3, 2, 1, 0, 2, 3, 2]
    arrR = [0, 2, 3, 2, 0, 2, 3, 1, 3, 2, 1, 0, 1, 0, 1, 3]
    arrL.reverse()
    arrR.reverse()
    
    for i in range(len(mob_matrix1)):
        for j in range(len(mob_matrix1[i])):
            # Compute XOR
            bit1 = mob_matrix1[i][j].text
            bit2 = mob_matrix2[i][j].text
            xor_result = xor2Bits(bit1, bit2)  # Your custom XOR function
            
            # Update result cell
            updated_cell = update_matrix_cell(result_matrix, [arrL[i]], [arrL[j]], xor_result)
            self.play(Write(mob_result[i][j]), run_time=run_time)
            run_time = max(0.1, run_time * 0.9)  # Gradually speed up


class KeyExpansion(Scene):
    def construct(self):
        # Create matrix for key 0
        keyString = "1234"
        keyMatrix0 = MobjectMatrix(
            blockToMatrix(textToBinaryString(keyString)),
            element_to_mobject=Text
        )
        
        # Add label for key 0
        lblKey0 = Text("Key 0:")
        lblKey0.move_to(keyMatrix0.get_center()).align_to(keyMatrix0, UP * 2).shift(UP * 0.8)
        self.add(lblKey0, keyMatrix0)
        self.play(*setPairColors(keyMatrix0))
        
        # Add title for non-linear shift 0
        lblExpansion = Text("Key Expansion")
        lblExpansion.to_edge(UP)
        self.play(Write(lblExpansion))
        
        # Group matrix with the label and move to the left
        gpKey0 = VGroup(keyMatrix0, lblKey0)
        self.play(gpKey0.animate.scale(0.9).to_edge(LEFT))
        
        # Copy the matrix and move it to the right
        keyMatrix1 = keyMatrix0.copy()
        self.add(keyMatrix1)
        self.play(keyMatrix1.animate.to_edge(RIGHT))
        
        # Create label for Non-Linear Shift 0
        lblNonLinearShift = Text("Non-Linear Shift 0")
        lblNonLinearShift.move_to(keyMatrix1.get_center()).align_to(keyMatrix1, UP * 2).shift(UP * 0.8).scale(0.6)
        self.play(Write(lblNonLinearShift))
        
        # Animation for Non-Linear Shift 0
        nonLinearShiftGroup = GPNonLinearShift0(keyMatrix1)
        
        arrL = [0, 1, 3, 0, 3, 2, 1, 1, 0, 3, 2, 1, 0, 2, 3, 2]
        arrR = [0, 2, 3, 2, 0, 2, 3, 1, 3, 2, 1, 0, 1, 0, 1, 3]
        
        mobMatrix = keyMatrix1.get_mob_matrix()
        previous = mobMatrix[arrL[0]][arrR[0]]
        path = TracedPath((lambda: previous.get_center() + IN), stroke_color=GRAY, stroke_width=4, stroke_opacity=0.6)
        
        self.add(path)
        for i in range(0, len(arrL) - 1):
            gp = VGroup(previous, mobMatrix[arrL[i + 1]][arrR[i + 1]])
            self.play(CyclicReplace(*gp, path_arc=0), run_time=1.5)

        path.clear_updaters()
        
        # Move path and Non-Linear Shift label to the center
        lblShift0 = Text("NLS0").scale(0.8).move_to(ORIGIN).shift(UP * 1.4)
        self.play(path.animate.move_to(ORIGIN).scale(0.8), Transform(lblNonLinearShift, lblShift0))
        
        # Create label for Pre-Key 1        
        lblKey1 = Text("Pre-Key 1")
        lblKey1.move_to(keyMatrix1.get_center()).align_to(keyMatrix1, UP * 2).shift(UP * 0.8)
        self.play(Write(lblKey1))
        
        # Group keys and move to the left
        gpKey1 = VGroup(keyMatrix1, lblKey1)
        gpKeys = VGroup(gpKey0, gpKey1)
        self.play(gpKeys.animate.shift(LEFT * 8.5))
        
        # Copy key1 and move to the right
        keyMatrix2 = keyMatrix1.copy()
        self.add(keyMatrix2)
        self.play(keyMatrix2.animate.to_edge(RIGHT))
        
        # Perform Non-Linear Shift 0
        gp = GPNonLinearShift0(keyMatrix2)
        self.play(CyclicReplace(*gp, path_arc=0, run_time=4), Indicate(path, scale_factor=1.1, color=PURE_GREEN, run_time=1))
        
        # Create Pre-Key 2 label
        lblKey2 = Text("Pre-Key 2")
        lblKey2.move_to(keyMatrix2.get_center()).align_to(keyMatrix2, UP*2).shift(UP*0.8)
        self.play(Write(lblKey2), path.animate.set_stroke(GREY_B, opacity=1))

        # Group keys and move to the left
        gpKeys += VGroup(keyMatrix2, lblKey2)

        self.play(gpKeys.animate.shift(LEFT*8.5))

        # Copy key2 and move to the right
        keyMatrix3 = keyMatrix2.copy()
        self.add(keyMatrix3)
        self.play(keyMatrix3.animate.to_edge(RIGHT))

        # Execute DNL0
        gp = GPNonLinearShift0(keyMatrix3)
        self.play(CyclicReplace(*gp, path_arc=0, run_time=4), Indicate(path, scale_factor=1.1, color=PURE_GREEN, run_time=1))

        lblKey3 = Text("Pre-Key 3")
        lblKey3.move_to(keyMatrix3.get_center()).align_to(keyMatrix3, UP*2).shift(UP*0.8)
        self.play(Write(lblKey3), path.animate.set_stroke(GREY_B, opacity=1))

        # Group keys and move to the left
        gpKeys += VGroup(keyMatrix3, lblKey3)

        self.play(gpKeys.animate.shift(LEFT*8.5))

        # Copy key3 and move to the right
        keyMatrix4 = keyMatrix3.copy()
        self.add(keyMatrix4)
        self.play(keyMatrix4.animate.to_edge(RIGHT))

        # Execute DNL0
        gp = GPNonLinearShift0(keyMatrix4)
        self.play(CyclicReplace(*gp, path_arc=0, run_time=4), Indicate(path, scale_factor=1.1, color=PURE_GREEN, run_time=1))

        # Create Pre-Key 4 label
        lblKey4 = Text("Pre-Key 4")
        lblKey4.move_to(keyMatrix4.get_center()).align_to(keyMatrix4, UP*2).shift(UP*0.8)
        self.play(Write(lblKey4), path.animate.set_stroke(GREY_B, opacity=1))

        # Group keys
        gpKeys += VGroup(keyMatrix4, lblKey4)

        # Hide the path and non-linear displacement label
        nonKeyGroup = VGroup(path, lblNonLinearShift)
        self.play(nonKeyGroup.animate.fade(1))

        self.play(gpKeys.animate.arrange_in_grid(1).move_to(ORIGIN).scale(0.55))

        self.wait(1)

        # Update title to XOR between Key 0 and Pre-Keys
        lblKeyExpansionXor = Text("Key Expansion: XOR between Key 0 and Pre-Keys").scale(0.8).to_edge(UP)
        lblKeyExpansionXor[13:].set_color(BLUE)

        self.play(TransformMatchingShapes(lblExpansion, lblKeyExpansionXor))

        newMatrixKey1 = keyMatrix1.copy()
        newMatrixKey2 = keyMatrix2.copy()
        newMatrixKey3 = keyMatrix3.copy()
        newMatrixKey4 = keyMatrix4.copy()
        newKeyGroup = VGroup(newMatrixKey1, newMatrixKey2, newMatrixKey3, newMatrixKey4)

        # Move the group of keys below the title
        preKeyGroup = gpKeys - gpKey0

        self.play(preKeyGroup.animate.shift(UP*1.9))
        
        animate_xor(self, keyMatrix0, keyMatrix1, newMatrixKey1)
        
        
        
#### CHECKPOINT