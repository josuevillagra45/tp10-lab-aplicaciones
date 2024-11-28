import py5

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

    if py5.frame_count >= 360:
        py5.no_loop()
        py5.exit_sketch()

py5.run_sketch()