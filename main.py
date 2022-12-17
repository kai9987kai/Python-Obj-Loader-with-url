import tkinter as tk
from tkinter import filedialog
from pywavefront import Wavefront

# Create a Tkinter window
window = tk.Tk()
window.title("3D Model Viewer")

# Create a canvas to display the 3D model
canvas = tk.Canvas(window, width=500, height=500, bg='white')
canvas.pack()

# Create a "Open" button to select a 3D model file
def open_model():
    filepath = filedialog.askopenfilename(filetypes=[("OBJ files", "*.obj")])
    model = Wavefront(filepath)
    for mesh in model.meshes:
        for material in mesh.materials:
            for face in material.faces:
                points = [model.vertices[i] for i in face]
                canvas.create_polygon(points, fill=material.diffuse, outline='black')

button = tk.Button(window, text="Open", command=open_model)
button.pack()

# Display the window
window.mainloop()
