import tkinter as tk
from threading import Thread
from metronome import Metronome

class MetronomeGui:
    def __init__(self, root):
        self.metronome = Metronome
        self.thread1 = Thread(target=self.metronome.play)
        self.beat_var = tk.IntVar()
        self.measure_var = tk.IntVar()
        self.beat_var.set(self.metronome.beats_pm)
        self.measure_var.set(self.metronome.measure)

        self.beat_label = tk.Label(root, text="Beats per minute: ")
        self.measure_label = tk.Label(root, text="Beats per bar ")

        self.beat_entry = tk.Entry(root, textvariable=self.beat_var)
        self.measure_entry = tk.Entry(root, textvariable=self.measure_var)

        self.update_bpm = tk.Button(root,text = 'Play', command = self.play_metronome)

        self.beat_label.grid(row=0, column=0)
        self.beat_entry.grid(row=0, column=1)
        self.measure_label.grid(row=1, column=0)
        self.measure_entry.grid(row=1, column=1)
        self.update_bpm.grid(row=2, column=0, columnspan=2) 

    def play_metronome(self):
        beat = self.beat_var.get()
        measure = self.measure_var.get()
        self.metronome.beats_pm = beat
        self.metronome.measure = measure
        if not self.thread1.is_alive():
            self.thread1.start()
        
root = tk.Tk()
metronome = MetronomeGui(root)
root.mainloop()
