import mingus.core.value as value
from mingus.containers import Note, Bar, Track, Composition
from mingus.midi import midi_file_out

def create_melody():
    # Define the melody as a list of (note, duration) tuples
    main_melody_notes = [
        ("G-4", value.eighth), ("G-4", value.eighth), ("G-4", value.eighth),
        ("G-4", value.eighth), ("G-4", value.eighth), ("G-4", value.eighth),
        ("G-4", value.eighth), ("G-4", value.eighth),
        ("A-4", value.eighth), ("A-4", value.eighth), ("A-4", value.eighth),
        ("A-4", value.eighth), ("A-4", value.eighth), ("A-4", value.eighth),
        ("A-4", value.eighth), ("A-4", value.eighth)
    ]

    # Define the change-up melody as a list of (note, duration) tuples
    change_up_melody_notes = [
        ("B-4", value.eighth), ("B-4", value.eighth), ("B-4", value.eighth),
        ("B-4", value.eighth), ("C-5", value.eighth), ("C-5", value.eighth),
        ("C-5", value.eighth), ("C-5", value.eighth),
        ("D-5", value.eighth), ("D-5", value.eighth), ("D-5", value.eighth),
        ("D-5", value.eighth), ("E-5", value.eighth), ("E-5", value.eighth),
        ("E-5", value.eighth), ("E-5", value.eighth)
    ]

    # Create a track and add the melody
    melody_track = Track()
    
    # Repeat the main melody 3 times
    for _ in range(3):
        for note, duration in main_melody_notes:
            bar = Bar()
            bar.place_notes(Note(note), duration)
            melody_track.add_bar(bar)

    # Add the change-up melody once
    for note, duration in change_up_melody_notes:
        bar = Bar()
        bar.place_notes(Note(note), duration)
        melody_track.add_bar(bar)

    # Repeat the main melody 4 times
    for _ in range(4):
        for note, duration in main_melody_notes:
            bar = Bar()
            bar.place_notes(Note(note), duration)
            melody_track.add_bar(bar)

    return melody_track

def main():
    melody_track = create_melody()

    # Create a composition and add the melody track
    composition = Composition()
    composition.add_track(melody_track)

    # Export the composition to a MIDI file
    midi_file_out.write_Composition("pop_rock_melody.mid", composition)

if __name__ == "__main__":
    main()
