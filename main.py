from manim import *
from manim_onlinetex import *

class Test(Scene):
  def construct(self):
    self.add(Tex("Hello World"))
    self.wait(1)