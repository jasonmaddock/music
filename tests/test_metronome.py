import pytest
from metronome.metronome import Metronome

@pytest.fixture
def expected_result(bpm, test_length=5):
    beats = ((bpm/60)*test_length)
    message = f"{int(beats)} beats played."
    return message


class TestMetronome:
    @pytest.mark.parametrize(
        "bpm,measure",
        (
            [
                60,
                4,
            ],
            [
                120,
                3,
            ],
            [
                180,
                7,
            ],
            [
                360,
                4,
            ],
        ),
    )
    def test_metronome(self, bpm, measure, expected_result):
        metro = Metronome
        metro.beat_count = 0
        metro.measure = measure
        metro.beats_pm = bpm
        result = metro.live_test()
        assert result == expected_result
