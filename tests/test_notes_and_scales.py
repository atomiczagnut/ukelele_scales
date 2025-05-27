import pytest
import notes_and_scales

def test_scaleDict_contains_expected_scales():
    # Check that all expected scales are present
    for scale in ["C Major", "C Minor", "C Blues", "C Spanish"]:
        assert scale in notes_and_scales.scaleDict

def test_scaleDict_notes_are_midi_numbers():
    # Check that all notes in all scales are integers (MIDI numbers)
    for notes in notes_and_scales.scaleDict.values():
        assert all(isinstance(n, int) for n in notes)

def test_noteDict_contains_expected_notes():
    # Check that some known MIDI notes are present
    for midi_note in [60, 64, 67, 72]:
        assert midi_note in notes_and_scales.noteDict

def test_noteDict_values_are_tuples():
    # Check that all noteDict values are (x, y) tuples of ints
    for coords in notes_and_scales.noteDict.values():
        assert isinstance(coords, tuple)
        assert len(coords) == 2
        assert all(isinstance(c, int) for c in coords)