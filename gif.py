import py5
import imageio
frames = []
frame_count = 30
def setup():
py5.size(400, 400)
py5.frame_rate(10)
def draw():

    
# Tu código de animación aquí
# Captura y guarda cada fotograma
frame = py5.get_pixels()
frames.append(frame)