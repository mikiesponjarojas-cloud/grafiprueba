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
    gluPerspective(60, 1, 0.1, 100.0)  # Mejor visión

    glMatrixMode(GL_MODELVIEW)

def cube():
    glBegin(GL_QUADS)

    glColor3f(1.0, 0.0, 1.0)
    glVertex3f( 0.7, 0.7,-0.7)
    glVertex3f(-0.7, 0.7,-0.7)
    glVertex3f(-0.7, 0.7, 0.7)
    glVertex3f( 0.7, 0.7, 0.7)

    glColor3f(0.0, 1.0, 0.0)
    glVertex3f( 0.7,-0.7, 0.7)
    glVertex3f(-0.7,-0.7, 0.7)
    glVertex3f(-0.7,-0.7,-0.7)
    glVertex3f( 0.7,-0.7,-0.7)

    glColor3f(0.0, 0.0, 1.0)
    glVertex3f( 0.7, 0.7, 0.7)
    glVertex3f(-0.7, 0.7, 0.7)
    glVertex3f(-0.7,-0.7, 0.7)
    glVertex3f( 0.7,-0.7, 0.7)

    glColor3f(1.0, 1.0, 0.0)
    glVertex3f( 0.7,-0.7,-0.7)
    glVertex3f(-0.7,-0.7,-0.7)
    glVertex3f(-0.7, 0.7,-0.7)
    glVertex3f( 0.7, 0.7,-0.7)

    glColor3f(1.0, 0.0, 1.0)
    glVertex3f(-0.7, 0.7, 0.7)
    glVertex3f(-0.7, 0.7,-0.7)
    glVertex3f(-0.7,-0.7,-0.7)
    glVertex3f(-0.7,-0.7, 0.7)

    glColor3f(0.0, 1.0, 1.0)
    glVertex3f( 0.7, 0.7,-0.7)
    glVertex3f( 0.7, 0.7, 0.7)
    glVertex3f( 0.7,-0.7, 0.7)
    glVertex3f( 0.7,-0.7,-0.7)

    glEnd()

def draw_cube(x, y, z, speed):
    global angle

    glLoadIdentity()
    glTranslatef(x, y, z)

    # Rotación en los 3 ejes
    glRotatef(angle * speed, 1, 0, 0)
    glRotatef(angle * speed, 0, 1, 0)
    glRotatef(angle * speed, 0, 0, 1)

    cube()

def render():
    global angle

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # 4 cubos separados
    draw_cube(0, 0, -8, 1)
    draw_cube(-4, 0, -10, 1.5)
    draw_cube(4, 0, -10, 0.8)
    draw_cube(0, 3, -9, 1.2)

    glfw.swap_buffers(window)

    angle += 0.01 # velocidad visible

def main():
    global window

    if not glfw.init():
        sys.exit()

    window = glfw.create_window(600, 600, "4 Cubos 3D", None, None)
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