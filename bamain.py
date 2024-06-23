import tkinter as tk
from tkinter import PhotoImage, Canvas
import random
import sys

class Banana:
    def __init__(self, scene, x=0, y=0):
        self.scene = scene
        self.image = PhotoImage(file='banana1.png')
        self.image = self.image.subsample(16)
        self.image_bomb = PhotoImage(file='bomb.png')
        self.image_bomb = self.image_bomb.subsample(8)
        self.imageRef = scene.canvas.create_image(x, y, image=self.image)
        self.bomb_status = False

    def update(self):
        x, y = 500, 500  # You may need to adjust this based on your screen resolution
        ban_x, ban_y = self.scene.canvas.coords(self.imageRef)
        dist = (abs(x-ban_x)+abs(y-ban_y))
        if self.bomb_status:
            self.scene.canvas.move(
                self.imageRef,
                random.choice((-30, 30)),
                random.choice((-30, 30))
            )
            self.scene.canvas.itemconfig(self.imageRef, image=self.image)
            for _ in range(10):
                self.scene.new_banana(
                    random.randint(0, self.scene.screen_width),
                    random.randint(0, self.scene.screen_height),
                )
            self.bomb_status = False
        elif dist < 5:
            self.scene.canvas.itemconfig(self.imageRef, image=self.image_bomb)
            self.bomb_status = True
        else:
            numero = random.choice((1,2,5))
            self.scene.canvas.move(
                self.imageRef,
                numero if x > ban_x else -numero,
                numero if y > ban_y else -numero
            )

class Scene:
    def __init__(self, window: tk.Tk):
        self.window = window
        self.screen_width = window.winfo_screenwidth()
        self.screen_height = window.winfo_screenheight()
        self.canvas = Canvas(
            window,
            width=self.screen_width,
            height=self.screen_height,
            highlightthickness=0,
            bg='white'
        )
        self.canvas.pack(fill=tk.BOTH, expand=tk.YES)
        self.bananas = []

    def update(self):
        for banana in self.bananas:
            banana.update()

    def new_banana(self, x, y):
        banana = Banana(self, x, y)
        self.bananas.append(banana)

class Game:
    def __init__(self):
        self.window = self.create_window()
        self.scene = Scene(self.window)
        self.window.bind("<KeyPress>", self.key_press_handler)

    def key_press_handler(self, event):
        if event.char == 'q':
            sys.exit()

    def update(self):
        self.scene.update()
        self.window.after(5, self.update)

    def create_window(self):
        window = tk.Tk()
        window.attributes('-alpha', 0.8)  # Establecer transparencia al 80%
        window.wm_attributes("-topmost", True)
        window.attributes("-fullscreen", True)
        window.overrideredirect(True)
        return window

    def start(self):
        self.update()
        self.window.mainloop()

game = Game()
game.scene.new_banana(100, 100)
game.start()
