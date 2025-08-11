from pyo import *

class harmonizer():
    s = Server(duplex=1).boot()
    # Play a melodic sound and send its signal to the left speaker.

    mic = Input().play().out()

    """
    # Half-sine window used as the amplitude envelope of the overlaps.
    env = WinTable(8)
    # Length of the window in seconds.
    wsize = 0.1

    # Amount of transposition in semitones.
    trans = -7
    # Compute the transposition ratio.
    ratio = pow(2.0, trans / 12.0)
    # Compute the reading head speed.
    rate = -(ratio - 1) / wsize
    # Two reading heads out-of-phase.
    ind = Phasor(freq=rate, phase=[0, 0.5])
    # Each head reads the amplitude envelope...
    win = Pointer(table=env, index=ind, mul=0.7)

    # Amount of transposition in semitones.
    trans2 = 4
    # Compute the transposition ratio.
    ratio2 = pow(2.0, trans2 / 12.0)
    # Compute the reading head speed.
    rate2 = -(ratio2 - 1) / wsize
    # Two reading heads out-of-phase.
    ind2 = Phasor(freq=rate2, phase=[0, 0.5])
    # Each head reads the amplitude envelope...
    win2 = Pointer(table=env, index=ind2, mul=0.7)

    # ... and modulates the delay time (scaled by the window size) of a delay line.
    # mix(1) is used to mix the two overlaps on a single audio stream.
    snd = Delay(mic, delay=ind * wsize, mul=win).mix(1).out(1)
    snd2 = Delay(mic, delay=ind2 * wsize, mul=win2).mix(1).out(1)
    """
    
    harm = Harmonizer(mic, transpo=4).out()
    harm2 = Harmonizer(mic, transpo=7).out()
    s.gui(locals())
