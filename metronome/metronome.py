from pygame import mixer
import time

class Metronome:
    beats_pm = 150
    beats_ps = 1/(beats_pm/60)
    measure = 4
    mixer.init()
    beep = mixer.Sound("sounds/tap_low.wav")
    beep_high = mixer.Sound("sounds/tap.wav")
    playing = False
    beat_count = 0
    bar_count = 0

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
                time.sleep(cls.beats_ps)
            cls.bar_count += 1
    
    @classmethod
    def live_test(cls, length):
        from threading import Thread

        test = Thread(target=cls.play, args=())
        test.start()
        time.sleep(length)
        cls.playing = False
        while test.is_alive():
            time.sleep(0.1)
        return cls.beat_count, cls.bar_count

if __name__ == "__main__":
    beats, bars = Metronome.live_test(5)
    print(f"{beats} beats played, {bars} bars played")