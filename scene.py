from manim import *

class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square= Square()

        self.play(Create(square))
        self.play(square.animate.rotate(PI/4))
        self.play(Transform(square, circle))
        self.play(square.animate.set_fill(BLUE,opacity=0.5))


class DifferentRotations(Scene):
    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(2*LEFT)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(2*RIGHT)

        self.play(left_square.animate.rotate(PI/4), Rotate(right_square, angle=PI/4), run_time=2)
        self.wait()
