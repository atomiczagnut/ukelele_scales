import pytest
from unittest.mock import MagicMock
from GUI import draw_fretboard, draw_note

def test_draw_fretboard():
    canvas = MagicMock()
    draw_fretboard(canvas)
    # There should be 13 lines drawn (vertical and horizontal)
    assert canvas.create_line.call_count == 13
    # Check a couple of specific calls
    canvas.create_line.assert_any_call(50, 50, 50, 450)
    canvas.create_line.assert_any_call(50, 50, 200, 50, width=5)

@pytest.mark.parametrize(
    "x, y, expected_args, expected_kwargs",
    [
        (60, 40, (50, 30, 70, 50), {}),  # open string (no fill)
        (60, 60, (50, 50, 70, 70), {"fill": "black"}),  # fretted (filled)
    ]
)
def test_draw_note(x, y, expected_args, expected_kwargs):
    canvas = MagicMock()
    draw_note(x, y, canvas)
    if expected_kwargs:
        canvas.create_oval.assert_called_with(*expected_args, **expected_kwargs)
    else:
        canvas.create_oval.assert_called_with(*expected_args)
