# coding: utf-8
"""
Planeedisüsteemi simulatsiooni graafiline kasutajaliides.
Kasutab Pythoni standard kasutajaliidese-raamistikku Tkinter.

Käivitamiseks kirjutada Command Prompti:
    pythonw points_gui.py
"""

from tkinter import *

from geom import *
from planets import PlanetarySystem
from sierpinski_triangle import SierpinskiTriangle


class Application(Frame):
    """Ühest aknast koosnev lihtne kasutajaliides"""

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.planets = PlanetarySystem()
        self.triangle = []
        self.point_dict = {}
        self.point_width = 5
        self.zoom = 7
        self.cx, self.cy = 300, 300
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        """Erinevate kasutajaliidese vidinate tekitamine"""
        self.create_canvas()
        self.create_reset_button()
        self.create_draw_planets_button()
        self.create_triangle_text()
        self.level_box = self.create_triangle_level_box()
        self.create_draw_triangle_button()

    def create_triangle_level_box(self):
        dx = StringVar()
        dx.set("Level")
        dx_label = Label(self, textvariable=dx)
        dx_label.pack(fill=X)
        dx_box = IntVar()
        dx_text_box = Entry(self, textvariable=dx_box)
        dx_text_box.pack(fill=X)
        return dx_box

    def create_canvas(self):
        self.canv = Canvas(self, background='black', width=self.cx * 2, height=self.cy * 2)
        self.canv.pack({"side": "left"})

    def create_draw_planets_button(self):
        Button(self, text="Draw planets", command=self.draw_planets).pack(fill=X)

    def create_reset_button(self):
        Button(self, text="Reset", command=self.reset).pack(fill=X)

    def create_triangle_text(self):
        labelText = StringVar()
        labelText.set("Select triangle attributes")
        Label(self, textvariable=labelText, relief=RAISED).pack(fill=X)

    def create_draw_triangle_button(self):
        Button(self, text="Draw triangle", command=self.draw_triangle).pack(fill=X)

    def conv_coords(self, x, y):
        """
        Simulatsiooni koordinaatide konverteerimine kasutajaliidese jaoks sobivale kujule.
        Sõltub atribuutidest:
        cx, cy - kuva keskpunkt
        zoom - suurendus
        planet_width - planeedi suurus
        Väljastab ovaali joonistamiseks vajalikud neli koordinaati
        """
        x0 = x * self.zoom
        y0 = y * self.zoom
        x1 = x0 + self.point_width
        y1 = y0 + self.point_width
        return x0, y0, x1, y1

    def draw_triangle(self):
        self.reset()
        p1 = Point(self.cx / self.zoom, 10 / self.zoom)
        p2 = Point(10 / self.zoom, self.cy / self.zoom * 2 - 10 / self.zoom)
        p3 = Point(self.cx / self.zoom * 2 - 10 / self.zoom, self.cy / self.zoom * 2 - 10 / self.zoom)

        triangles = SierpinskiTriangle(min(max(self.level_box.get(), 1), 7), p1, p2, p3)
        for name, triangle in enumerate(triangles):
            self.draw_point(name, triangle.x(), triangle.y())

    def draw_planets(self):
        self.reset()
        for name, planet in enumerate(self.planets):
            self.draw_point(name, self.planets[name].x() + self.cx / self.zoom,
                            self.planets[name].y() + self.cy / self.zoom)

    def draw_point(self, name, x, y):
        x0, y0, x1, y1 = self.conv_coords(x, y)
        oval_id = self.canv.create_oval(x0, y0, x1, y1, fill="white")
        self.point_dict[name] = oval_id

    def reset(self):
        for id in self.point_dict.values():
            self.canv.delete(id)
        self.point_dict = {}


app = Application()
app.mainloop()
