import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import sys

window = None
angle = 0

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 1, 0.1, 50.0)

    glMatrixMode(GL_MODELVIEW)

def cube():
    glBegin(GL_QUADS)

    # Colores verdes tipo imagen
    glColor3f(1.0, 0.0, 1.0)  # Rojo
    glVertex3f( 1, 1,-1)
    glColor3f(0.4, 1.0, 1.0)  # Verde
    glVertex3f(-1, 1,-1)
    glColor3f(0.4, 1.0, 1.0)  # Verde
    glVertex3f(-1, 1, 1)
    glColor3f(0.3, 0.8, 0.1)  # Verde
    glVertex3f( 1, 1, 1)

    glColor3f(0.0, 1.0, 0.0)  # Verde
    glVertex3f( 1,-1, 1)
    glVertex3f(-1,-1, 1)
    glVertex3f(-1,-1,-1)
    glVertex3f( 1,-1,-1)

    glColor3f(0.0, 0.0, 1.0)  # Azul
    glVertex3f( 1, 1, 1)
    glVertex3f(-1, 1, 1)
    glVertex3f(-1,-1, 1)
    glVertex3f( 1,-1, 1)

    glColor3f(1.0, 1.0, 0.0)  # Amarillo
    glVertex3f( 1,-1,-1)
    glVertex3f(-1,-1,-1)
    glVertex3f(-1, 1,-1)
    glVertex3f( 1, 1,-1)

    glColor3f(1.0, 0.0, 1.0)  # Magenta
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, 1,-1)
    glVertex3f(-1,-1,-1)
    glVertex3f(-1,-1, 1)

    glColor3f(0.0, 1.0, 1.0)  # Cyan
    glVertex3f( 1, 1,-1)
    glVertex3f( 1, 1, 1)
    glVertex3f( 1,-1, 1)
    glVertex3f( 1,-1,-1)

    glEnd()

def draw_cube(x, y, z, rot_speed):
    global angle

    glLoadIdentity()
    glTranslatef(x, y, z)

    glRotatef(angle * rot_speed, 1, 0, 0)
    glRotatef(angle * rot_speed, 0, 1, 0)
    glRotatef(angle * rot_speed, 0, 0, 1)

    cube()

def render():
    global angle

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # 4 cubos en diferentes posiciones
    draw_cube(0, 0, -5, 1)      # Centro
    draw_cube(-3, 0, -7, 1.5)   # Izquierda
    draw_cube(3, 0, -7, 0.7)    # Derecha
    draw_cube(0, 2, -6, 1.2)    # Arriba

    glfw.swap_buffers(window)

    angle += 0.01  # Movimiento global

def main():
    global window

    if not glfw.init():
        sys.exit()

    window = glfw.create_window(900, 900, "4 Cubos en Movimiento", None, None)

    if not window:
        glfw.terminate()
        sys.exit()

    glfw.make_context_current(window)

    glViewport(0, 0, 600, 600)
    init()

    while not glfw.window_should_close(window):
        render()
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()