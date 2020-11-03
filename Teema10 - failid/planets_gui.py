# coding: utf-8
"""
Planeedisüsteemi simulatsiooni graafiline kasutajaliides.
Kasutab Pythoni standard kasutajaliidese-raamistikku Tkinter.

Käivitamiseks kirjutada Command Prompti:
    pythonw planets_ui.py
"""

from tkinter import *

import planets_facade


class Application(Frame):
    """Ühest aknast koosnev lihtne kasutajaliides"""

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.controller = planets_facade.PSController()
        self.po_dict = {}
        self.planet_width = 3
        self.zoom = 6
        self.auto_speed = 20
        self.auto_on = 0
        self.auto_launch_on = 0
        self.dx_box = None
        self.dy_box = None
        self.cx, self.cy = 300, 300
        self.pack()
        self.createWidgets()
        self.make_solar_system()

    def tick(self):
        """
        (Kasutaja on vajutanud Tick-nuppu.) 
        Saada sõnum kontrollerile ja kuva planeedid uutel asukohtadel.
        """
        self.controller.tick()
        self.move_planets()
        if self.auto_launch_on:
            self.launch_rockets()

    def tick100(self):
        """
        (Kasutaja on vajutanud Tick100-nuppu.) 
        Saada sõnum kontrollerile ja kuva planeedid uutel asukohtadel.
        """
        self.controller.multi_tick(100)
        self.move_planets()
        if self.auto_launch_on:
            self.launch_rockets()

    def auto_launch(self):
        self.auto_launch_on = not self.auto_launch_on

    def auto(self):
        self.auto_on = not self.auto_on
        self.auto_tick()

    def auto_tick(self):
        if self.auto_on:
            self.tick()
            self.after(self.auto_speed, self.auto_tick)
        if self.auto_launch_on:
            self.launch_rockets()

    def launch_rockets(self):
        """Rakettide tulistamine"""
        for planet_id in self.bLaunchOptions.curselection():
            planet = self.controller.get_planetary_item(planet_id)
            self.controller.add_space_ship(planet.x(), planet.y(), self.dx_box.get(), self.dy_box.get())
            self.draw_planet(len(self.po_dict), planet.x(), planet.y())

    def make_solar_system(self):
        """Planeedisüsteemi initsialiseerimine"""
        self.controller.make_solar_system()
        self.delete_planets()
        self.draw_planets()

    def createWidgets(self):
        """Erinevate kasutajaliidese vidinate tekitamine"""
        self.create_canvas()
        self.create_tick_buttons()
        self.create_auto_button()
        self.create_reset_button()
        self.create_launch_text()
        self.create_launch_options()
        self.dx_box = self.create_dx_box()
        self.dy_box = self.create_dy_box()
        self.create_launch_button()
        self.create_auto_launch_button()

    def create_dy_box(self):
        dy = StringVar()
        dy.set("dy")
        dy_label = Label(self, textvariable=dy)
        dy_label.pack(fill=X)
        dy_box = DoubleVar()
        dy_text_box = Entry(self, textvariable=dy_box)
        dy_text_box.pack(fill=X)
        return dy_box

    def create_dx_box(self):
        dx = StringVar()
        dx.set("dx")
        dx_label = Label(self, textvariable=dx)
        dx_label.pack(fill=X)
        dx_box = DoubleVar()
        dx_text_box = Entry(self, textvariable=dx_box)
        dx_text_box.pack(fill=X)
        return dx_box

    def create_canvas(self):
        self.canv = Canvas(self, background='black', width=self.cx * 2, height=self.cy * 2)
        self.canv.pack({"side": "left"})
        self.canv.create_oval(self.cx, self.cy, self.cx + self.planet_width,
                              self.cy + self.planet_width, fill="yellow")

    def create_tick_buttons(self):
        self.bTick = Button(self, text="Tick", command=self.tick)
        self.bTick.pack(fill=X)
        self.bTick100 = Button(self, text="Tick 100", command=self.tick100)
        self.bTick100.pack(fill=X)

    def create_auto_button(self):
        self.bAuto = Button(self, text="Auto", command=self.auto)
        self.bAuto.pack(fill=X)

    def create_reset_button(self):
        self.bDefault = Button(self, text="Reset", command=self.make_solar_system)
        self.bDefault.pack(fill=X)

    def create_launch_text(self):
        labelText = StringVar()
        labelText.set("Select planets\nwhere to launch a rocket from")
        self.bLaunchText = Label(self, textvariable=labelText, relief=RAISED)
        self.bLaunchText.pack(fill=X)

    def create_launch_options(self):
        self.bLaunchOptions = Listbox(self, selectmode="multiple")
        self.bLaunchOptions.insert(1, "Mercury")
        self.bLaunchOptions.insert(2, "Venus")
        self.bLaunchOptions.insert(3, "Earth")
        self.bLaunchOptions.insert(4, "Mars")
        self.bLaunchOptions.insert(5, "Jupiter")
        self.bLaunchOptions.insert(6, "Saturn")
        self.bLaunchOptions.insert(7, "Uranus")
        self.bLaunchOptions.insert(8, "Neptune")
        self.bLaunchOptions.insert(9, "Pluto")
        self.bLaunchOptions.pack(fill=X)

    def create_launch_button(self):
        self.bLaunch = Button(self, text="Launch", command=self.launch_rockets)
        self.bLaunch.pack(fill=X)

    def conv_coords(self, x, y):
        """
        Simulatsiooni koordinaatide konverteerimine kasutajaliidese jaoks sobivale kujule.
        Sõltub atribuutidest: 
        cx, cy - kuva keskpunkt
        zoom - suurendus
        planet_width - planeedi suurus
        Väljastab ovaali joonistamiseks vajalikud neli koordinaati
        """
        x0 = self.cx + x * self.zoom
        y0 = self.cy + y * self.zoom
        x1 = x0 + self.planet_width
        y1 = y0 + self.planet_width
        return x0, y0, x1, y1

    def draw_planets(self):
        """
        Joonistab ekraanile esimest korda olemasolevad planeedid,
        konverteerides koordinaadid sobivale kujule
        """
        sys = self.controller.system()
        for id in range(len(sys)):
            self.draw_planet(id, sys[id].x(), sys[id].y())

    def draw_planet(self, planet_id, x, y):
        """
        Joonistab esimest korda x, y koordinaatidega planeedi, 
        konverteerides koordinaadid sobivale kujule
        """
        x0, y0, x1, y1 = self.conv_coords(x, y)
        oval_id = self.canv.create_oval(x0, y0, x1, y1, fill="white")
        self.po_dict[planet_id] = oval_id

    def move_planets(self):
        """
        Liigutab ekraanil kõiki olemasolevaid planeete
        """
        sys = self.controller.system()
        for id in range(len(sys)):
            self.move_planet(id, sys[id].x(), sys[id].y())

    def move_planet(self, planet_id, x, y):
        """
        Liigutab ekraanil juba olemasolevat planeeti
        """
        x0, y0, x1, y1 = self.conv_coords(x, y)
        self.canv.coords(self.po_dict[planet_id], x0, y0, x1, y1)

    def delete_planets(self):
        """ Kustutab kõik kuvatud planeedid"""
        for id in self.po_dict.values():
            self.canv.delete(id)
        self.po_dict = {}

    def create_auto_launch_button(self):
        self.bAutoLaunch = Button(self, text="Auto launch", command=self.auto_launch)
        self.bAutoLaunch.pack(fill=X)


# Põhiprogramm
app = Application()
app.mainloop()
