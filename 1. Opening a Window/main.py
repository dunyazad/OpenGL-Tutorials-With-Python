import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders

def main():
    if not glfw.init():
        print("Failed to initialize GLFW.")
        return

    window = glfw.create_window(800, 600, "1. Opening a Window", None, None)

    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    glClearColor(0.3, 0.5, 0.7, 1.0)

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
