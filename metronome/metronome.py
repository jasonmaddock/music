from pygame import mixer
import time
import pathlib

path = pathlib.Path(__file__).parent.resolve()._str


class Metronome:
    beats_pm = 150
    measure = 4
    mixer.init()
    beep = mixer.Sound(path + "/sounds/tap_low.wav")
    beep_high = mixer.Sound(path + "/sounds/tap.wav")
    playing = False
    beat_count = 0

    @classmethod
    def beats_ps(cls):
        return float(1/(cls.beats_pm/60))

    @classmethod
    def play(cls):
        cls.playing = True
        while cls.playing == True:
            for i in range(0, cls.measure):
                if not cls.playing:
                    break
                if i == 0:
                    cls.beep_high.play()
                cls.beep.play()
                cls.beat_count += 1
                time.sleep(cls.beats_ps())
    
    @classmethod
    def live_test(cls, length=5):
        from threading import Thread

        test = Thread(target=cls.play, args=())
        test.start()

        time.sleep(length)
        cls.playing = False
        while test.is_alive():
            time.sleep(0.1)
        return f"{cls.beat_count} beats played."

if __name__ == "__main__":
    beats = Metronome.live_test()
