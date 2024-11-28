import py5
import imageio
import numpy as np

frames = []  # Lista para almacenar los fotogramas
frame_count = 360  # Número de fotogramas para completar un ciclo

def setup():
    py5.size(800, 600)
    py5.background(255)
    py5.frame_rate(30)

def draw():
    py5.background(255)
    py5.stroke(0)
    py5.no_fill()
    py5.ellipse(py5.width / 2, py5.height / 2, 400, 400)

    current_frame = py5.frame_count % 360
    angle = py5.radians(current_frame)

    x = py5.width / 2 + 200 * py5.cos(angle)
    y = py5.height / 2 + 200 * py5.sin(angle)

    py5.stroke_weight(2)
    py5.line(py5.width / 2, py5.height / 2, x, y)

    # Captura y guarda cada fotograma
    frame = py5.get_pixels()
    frames.append(np.array(frame))  # Guarda el fotograma como un array de numpy

    # Detiene la animación cuando se alcanza el número de fotogramas deseado
    if len(frames) >= frame_count:
        py5.no_loop()

def key_pressed():
    if py5.key == 's':
        save_gif()  # Guarda el GIF cuando se presiona la tecla 's'

def save_gif():
    # Guarda los fotogramas como un GIF utilizando imageio
    with imageio.get_writer('animation.gif', mode='I', duration=0.1) as writer:
        for frame in frames:
            pil_image = py5.to_pil_image(frame)  # Convierte el fotograma en una imagen PIL
            writer.append_data(pil_image)

    print('GIF guardado como animation.gif')

# Ejecutar el sketch de py5
py5.run_sketch()
