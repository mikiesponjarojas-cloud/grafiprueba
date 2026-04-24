import glfw
from OpenGL.GL import *
from OpenGL.GLU import gluPerspective, gluLookAt, gluNewQuadric, gluCylinder, gluSphere
import sys

def init():
    glClearColor(0.5, 0.8, 1.0, 1.0)
    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_PROJECTION)
    gluPerspective(60, 1.0, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def draw_cube():
    glBegin(GL_QUADS)
  
    glColor3f(0.8, 0.5, 0.2)
     
    # Frente
    glVertex3f(-1, 0, 1)
    glVertex3f(1, 0, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(-1, 1, 1)

    # Atrás
    glVertex3f(-1, 0, -1)
    glVertex3f(1, 0, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(-1, 1, -1)

    # Izquierda
    glVertex3f(-1, 0, -1)
    glVertex3f(-1, 0, 1)
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, 1, -1)

    # Derecha
    glVertex3f(1, 0, -1)
    glVertex3f(1, 0, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(1, 1, -1)

    # Segundo piso
    glVertex3f(-1, 1, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(1, 2, 1)
    glVertex3f(-1, 2, 1)

    glVertex3f(1, 1, -1)
    glVertex3f(1, 1, 1)
    glVertex3f(1, 2, 1)
    glVertex3f(1, 2, -1)

    glVertex3f(-1, 1, -1)
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, 2, 1)
    glVertex3f(-1, 2, -1)

    glVertex3f(-1, 1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(1, 2, -1)
    glVertex3f(-1, 2, -1)

    # Puerta
    glColor3f(0.1,0.1,0.8)
    glVertex3f(-0.5, 0, 1)
    glVertex3f(0.5, 0, 1)
    glVertex3f(0.5, 1, 1)
    glVertex3f(-0.5, 1, 1)

    # Ventana
    glColor3f(0.2, 0.8, 0.9)
    glVertex3f(-0.5, 1.5, 1)
    glVertex3f(0.5, 1.5, 1)
    glVertex3f(0.5, 2.0, 1)
    glVertex3f(-0.5, 2.0, 1)

    glEnd()

def draw_roof():
    glBegin(GL_TRIANGLES)
    glColor3f(0.9, 0.1, 0.1)

    glVertex3f(-1, 2, 1)
    glVertex3f(1, 2, 1)
    glVertex3f(0, 4, 0)

    glVertex3f(-1, 2, -1)
    glVertex3f(1, 2, -1)
    glVertex3f(0, 4, 0)

    glVertex3f(-1, 2, -1)
    glVertex3f(-1, 2, 1)
    glVertex3f(0, 4, 0)

    glVertex3f(1, 2, -1)
    glVertex3f(1, 2, 1)
    glVertex3f(0, 4, 0)

    glEnd()

def draw_second_house():
    glPushMatrix()
    glTranslatef(3, 0, 0)
    draw_cube()
    draw_roof()
    glPopMatrix()

#ÁRBOL
def draw_trunk():
    glPushMatrix()
    glColor3f(0.6, 0.3, 0.1)
    glRotatef(-90, 1, 0, 0)
    quadric = gluNewQuadric()
    gluCylinder(quadric, 0.2, 0.2, 1.5, 32, 32)
    glPopMatrix()

def draw_foliage():
    quadric = gluNewQuadric()

    glPushMatrix()
    glColor3f(0.1, 0.8, 0.1)
    glTranslatef(0, 2, 0)
    gluSphere(quadric, 0.8, 32, 32)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0, 2.7, 0)
    gluSphere(quadric, 0.5, 32, 32)
    glPopMatrix()

def draw_tree():
    draw_trunk()
    draw_foliage()

def draw_ground():
    glBegin(GL_QUADS)
    glColor3f(0.3, 0.3, 0.3)

    glVertex3f(-10, 0, 10)
    glVertex3f(10, 0, 10)
    glVertex3f(10, 0, -10)
    glVertex3f(-10, 0, -10)

    glEnd()

def draw_house():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    gluLookAt(6, 5, 10, 0, 1, 0, 0, 1, 0)

    draw_ground()

    # Casas
    draw_cube()
    draw_roof()
    draw_second_house()

    # Árboles
    glPushMatrix()
    glTranslatef(-3, 0, 0)
    draw_tree()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(2, 0, -3)
    draw_tree()
    glPopMatrix()

    glfw.swap_buffers(window)

def main():
    global window

    if not glfw.init():
        sys.exit()
    
    width, height = 800, 600
    window = glfw.create_window(width, height, "Casas con arboles", None, None)
    if not window:
        glfw.terminate()
        sys.exit()

    glfw.make_context_current(window)
    glViewport(0, 0, width, height)
    init()

    while not glfw.window_should_close(window):
        draw_house()
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()