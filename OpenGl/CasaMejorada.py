import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def draw_house():
    # Base
    glPushMatrix()
    glColor3f(0.8, 0.5, 0.2)
    glScalef(2, 1, 2)
    glutSolidCube(1)
    glPopMatrix()

    # Techo (cono)
    glPushMatrix()
    glColor3f(0.9, 0.1, 0.1)
    glTranslatef(0, 1, 0)
    glRotatef(-90, 1, 0, 0)
    quad = gluNewQuadric()
    gluCylinder(quad, 1.2, 0, 1.5, 20, 20)
    gluDeleteQuadric(quad)
    glPopMatrix()

# -------- ÁRBOL --------
def draw_tree():
    quad = gluNewQuadric()

    # Tronco
    glPushMatrix()
    glColor3f(0.5, 0.3, 0.1)
    glRotatef(-90, 1, 0, 0)
    gluCylinder(quad, 0.2, 0.2, 1.5, 20, 20)
    glPopMatrix()

    # Hojas
    glPushMatrix()
    glColor3f(0, 0.8, 0)
    glTranslatef(0, 1.8, 0)
    glutSolidSphere(0.7, 20, 20)
    glPopMatrix()

# -------- PRIMITIVAS --------
def draw_primitives():
    # Esfera
    glPushMatrix()
    glColor3f(1, 0, 0)
    glTranslatef(-3, 0.5, 3)
    glutSolidSphere(0.5, 20, 20)
    glPopMatrix()

    # Toro
    glPushMatrix()
    glColor3f(1, 1, 0)
    glTranslatef(3, 0.5, 3)
    glutSolidTorus(0.2, 0.5, 20, 20)
    glPopMatrix()

    # Tetera
    glPushMatrix()
    glColor3f(1, 0, 1)
    glTranslatef(0, 0.5, -3)
    glutSolidTeapot(0.5)
    glPopMatrix()


def draw_ground():
    glColor3f(0.3, 0.3, 0.3)
    glBegin(GL_QUADS)
    glVertex3f(-10, 0, 10)
    glVertex3f(10, 0, 10)
    glVertex3f(10, 0, -10)
    glVertex3f(-10, 0, -10)
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Cámara (IMPORTANTE)
    gluLookAt(8, 6, 8,
              0, 0, 0,
              0, 1, 0)

    draw_ground()

    # Casa
    glPushMatrix()
    glTranslatef(0, 0.5, 0)
    draw_house()
    glPopMatrix()

    # Árbol izquierdo
    glPushMatrix()
    glTranslatef(-3, 0, -2)
    draw_tree()
    glPopMatrix()

    # Árbol derecho
    glPushMatrix()
    glTranslatef(3, 0, -2)
    draw_tree()
    glPopMatrix()

    # Primitivas extra
    draw_primitives()

    glutSwapBuffers()


def reshape(w, h):
    if h == 0:
        h = 1

    glViewport(0, 0, w, h)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, w / h, 0.1, 100)

    glMatrixMode(GL_MODELVIEW)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Casa 3D con Primitivas")

    glClearColor(0.5, 0.8, 1.0, 1)
    glEnable(GL_DEPTH_TEST)

    glutDisplayFunc(display)
    glutReshapeFunc(reshape)

    glutMainLoop()

if __name__ == "__main__":
    main()