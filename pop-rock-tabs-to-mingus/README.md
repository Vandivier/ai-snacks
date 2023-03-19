# pop-rock-tab-to-mingus

This Python project was generated with GPT-4 and prompts described below.

The result is a runnable file, `main.py`, that plays a pop rock tune.

Install dependencies and run the program with the following two lines:

```
chmod +x install_and_run.sh && ./install_and_run.sh
python midi_to_wav.py pop_rock_melody.mid ./FPD.sf2 pop_rock_melody.wav
```

## Prompts

1. `Please write a 16 bar melody using tab notation for a song in the style of pop rock.`
2. `Please convert the melody into a Python program.`
3. `Can you generate a poetry script that will install poetry dependencies and run main.py?`
4. `Update the Python code to resolve the error "mingus.containers.mt_exceptions.NoteFormatError: Invalid note representation: 'G4'"`
5. `Are you able to directly convert the MIDI file to wav, mp3, or another runnable format using only Python?`
6. `Please update pyproject.toml to include the new dependencies.`
7. `Update pyproject.toml to ensure a version of numpy is used that is compatible with installation on a Windows computer.`
8. `Please make the melody 8 times longer and include at least one change-up.`

## Other Adjustments

1. Update `pyproject.toml` to:
   a. Include my information as author
   b. Remove empty dev deps
   c. Include license, readme, and packages lines
2. Remove unused imports in generated code.
3. Search and find a permissively licensed `.sf2` file.
4. After trying Prompt 7, decide that getting `wav` generation to work on Windows 11 is not feasible through prompting with time and training data constraints.
   a. Remove the `midi_to_wav.py` file, the `.sf2` file, and related dependencies.
   b. Apply Prompt 8 and convert the MIDI to mp3 via a free online service, [audio-online-convert.com](https://audio.online-convert.com/convert/midi-to-mp3).
