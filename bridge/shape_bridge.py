from abc import ABC

class Renderer(ABC):
    @property
    def what_to_render_as(self):
        return None

# TODO: reimplement Shape, Square, Triangle and Renderer/VectorRenderer/RasterRenderer
class Shape:
    def __init__(self, renderer):
        self.renderer = renderer
        self.name = None
    def __str__(self):
        return f'Drawing {self.name} as {self.renderer.what_to_render_as}'

class VectorRenderer(Renderer):
    @property
    def what_to_render_as(self):
        return 'lines'

class RasterRenderer(Renderer):
    @property
    def what_to_render_as(self):
        return 'pixels'

class Square(Shape):
    def __init__(self, renderer):
        super().__init__(renderer)
        self.name = 'Square'

class Triangle(Shape):
    def __init__(self, renderer):
        super().__init__(renderer)
        self.name = 'Triangle'
