import tkinter as tk

class Buttons():

    def __init__(self):
        self.infoText = None
        self.info = None
        self.informationFrame = None
        self.intervals = [" 1","♭2"," 2","♭3"," 3"," 4","♭5"," 5","♭6"," 6", "♭7"," 7"]
        self.triadInfo = ["A major triad is composed of the root note, a major third, and a perfect fifth. A major triad feels \nbright and stable.", 
        "A minor triad is composed of the root note, a minor third, and a perfect fifth. A minor triad feels \ndark and stable.", 
        "A diminished triad is composed of the root note, a minor third, and a diminished fifth. A \ndiminished triad feels dark and tense.", 
        "An augmented triad is composed of the root note, a major third, and an augmented fifth. An \naugmented triad feels surprising and unstable.", 
        "A sus2 chord is composed of the root note, major second, and a perfect fifth. Sus2 chords \nbuild up tension but maintain a warm quality. It is neither major nor minor.", 
        "A sus4 chord is composed of the root note, perfect fourth, and a perfect fifth. Sus4 chords \nbuild up tension but maintain a warm quality. It is neither major nor minor and has a strong pull \nto resolve."]
        self.extentionsInfo = ["The minor seventh is dissonant and wants to resolve. You can use a minor 7th with a major \ntriad to build a dominant seventh chord or pair it with a minor triad to make a minor seventh \nchord.", 
        "The major seventh is one semitone away from the root note, which can make it sound jarring, \nespecially out of context. It can add a jazz-like quality to a piece of music. It is commonly\n used with a major triad to build a major seventh chord.", 
        "The minor ninth is frequently used in European music as a suspension.", 
        "The major ninth is somewhat dissonant sounding. This extention is the same scale degree as a \nsuspended 2nd.", 
        "The perfect eleventh, when used with a minor ninth, causes the minor ninth to sound extremely \ndissonant against the major third. Eleventh chord are suposed to include the triad, 7th, and 9th, \nbut typically exclude some of those notes. This extention is the same scale degree as the \nsuspended 4th.", 
        "The major thirteenth is made of stacked major or minor thirds. Like perfect elevenths, notes are \nfrequently ommitted for ease of writing or playing."]
        self.inversionsInfo = ["This position has the root note on the bottom of the chord.", 
        " This inversion moves the second note of the chord to the bottom.",
        "This inversion moves the third note of the chord to the bottom.", "This inversion moves the fourth note of the chord to the bottom. It is only applicable if your \nchord has more than three notes. "]

    def alterScale(self, chord, scaleFrame):
        modedChord = [chord.output[i]%12 for i in range(len(chord.output))]
        modedChord.sort()
        modifier = chord.output[chord.inversion]%12 #accounts for inversions

        for i in range(0, 12):
            text = self.intervals[(i+modifier)%12]
            if ((i+modifier)%12) in modedChord:
                bgc = "white"
                font = "HiraginoSans 16 bold"
                color = "black" #"#457D0C"
            else:
                bgc = "#eeeeee"
                font = "HiraginoSans 16"
                color="black"

            scaleLabel = tk.Label(scaleFrame, text = text, font = font, borderwidth=4, bg=bgc, foreground=color,padx=12, pady=4)
            scaleLabel.grid(row=0, column=i+1)

    def checkBox(self, buttons, var, chord, inverBtns, scaleFrame):
        for i in range(len(buttons)):
            if i == var:
                btn = buttons[i]
                if btn["bg"] == "#c8f59c":
                    btn.config(bg="#d9d9d9")
                    chord.removeExtention(i)
                    if len(chord.extentions) == 0:
                        self.turnInverBoxOff(inverBtns)

                else:
                    btn.config(bg="#c8f59c")
                    self.setTextWithExtension(var)
                    chord.addExtention(i)
                    self.turnInverBoxOn(inverBtns)
        self.alterScale(chord, scaleFrame)

    def triadRadioBox(self, buttons, var, chord, scaleFrame):
        for i in range(len(buttons)):
            btn = buttons[i]
            if i == var:
                if btn["bg"] == "#d9d9d9":
                    btn.config(bg="#c8f59c")
                    chord.changeTriad(i)
                    self.setTextwithTriad(var)

            else:
                if btn["bg"] == "#c8f59c":
                    btn.config(bg="#d9d9d9")
        self.alterScale(chord, scaleFrame)

    def turnInverBoxOn(self, buttons):
        buttons[3].config(bg ="#d9d9d9")

    def turnInverBoxOff(self, buttons):
        buttons[3].config(bg ="#b7b7b7")

    def inverRadioBox(self, buttons, var, chord, scaleFrame):
        if buttons[3]["bg"] == "#b7b7b7" and var == 3:
            pass
        else:
            for i in range(len(buttons)):
                btn = buttons[i]
                if i == var and btn["bg"] != "#b7b7b7":
                    if btn["bg"] == "#d9d9d9":
                        btn.config(bg="#c8f59c")
                        chord.inversion = i
                        chord.invert()
                        if chord.on == True:
                            chord.restart(False)
                        self.setTextWithInversion(var)
                elif btn["bg"] == "#c8f59c":
                        btn.config(bg="#d9d9d9")    
        self.alterScale(chord, scaleFrame)    

    def clicked(self, btn, chord):
        if btn["text"] == "Start":
            btn.config(text = "Stop")
            btn.config(bg="#d9d9d9")
            chord.start()
        else:
            btn.config(text = "Start")
            btn.config(bg="#c8f59c")
            chord.stop()

    def setInformationText(self):
        if self.infoText is None:
            text = "This is a textbox that will display instructions for the harmonizer and information about the \nselected chord type."
            
            self.infoText = tk.Label(self.informationFrame, text=text, height=5, width=65, justify='left',anchor='nw', font = 'HiraginoSans 16', borderwidth=15, highlightthickness=0, background="white", foreground="black")
        self.info.grid(row=0, column=0, sticky="w")
        self.infoText.grid()

    def setTextwithTriad(self, var):
                self.infoText['text'] = self.triadInfo[var]
                self.setInformationText()
    
    def setTextWithExtension(self, var):
                self.infoText['text'] = self.extentionsInfo[var]
    
    def setTextWithInversion(self, var):
                self.infoText['text'] = self.inversionsInfo[var]