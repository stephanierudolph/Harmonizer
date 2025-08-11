import tkinter as tk
from buttons import Buttons
from chord import Chord

class GUI():

    def __init__(self):
        self.optionsEx = ["Minor 7th", "Major 7th", None, "Minor 9th", "Major 9th", None, None, "Perfect 11th", None, "Major 13th"]
        self.indexEx = 0
        self.buttonsEx=[]
        self.optionsInver = ["Root", "First Inversion", "Second Inversion", "Third Inversion"]
        self.indexInver = 0
        self.buttonsInver=[]
        self.scaleFrame = None
        self.root = tk.Tk()
        self.root.title("Harmonizer")

        mainFrame = tk.Frame(self.root, borderwidth=4, background="white")
        mainFrame.grid(row=0, column=0, sticky="nsew")
        mainFrame.columnconfigure(0, weight=1, minsize=500)
        mainFrame.rowconfigure(0, weight=1,  minsize=100)
        btn = Buttons()
        chord = Chord()
        self.title(mainFrame, btn, chord)
        self.scale(mainFrame, btn, chord)
        self.settings(mainFrame, btn, chord)
        self.information(mainFrame, btn)
        self.root.mainloop()

    def title(self, mainFrame, button, chord):
        #title frame
        titleFrame = tk.Frame(mainFrame, borderwidth=0)
        titleFrame.grid(row=0, column=0)
        label = tk.Label(titleFrame, text="Harmonizer", font = 'HiraginoSans 48', foreground="black", background="white", borderwidth=10)
        label.grid(row=0, column=0)


        buttonFrame = tk.Frame(mainFrame, borderwidth=0, highlightthickness=0, bg="white", pady=15)
        buttonFrame.grid(row=1, column=0, sticky="n")

        startBtn = tk.Label(buttonFrame, text = "Start", font = 'HiraginoSans 16', bg="#c8f59c", fg="black", padx=30, pady=5)
        startBtn.bind('<Button>', lambda e: button.clicked(startBtn, chord))
        startBtn.grid(column=0, row=0)

    def scale(self, mainFrame, btn, chord):
        #scale degree frame
        self.scaleFrame = tk.Frame(mainFrame, borderwidth=4, bg="#d9d9d9")
        self.scaleFrame.grid(row=2, column=0)
        self.scaleFrame.columnconfigure(0, weight=1, minsize=20)
        self.scaleFrame.rowconfigure(0, weight=1)

        scale = tk.Label(self.scaleFrame, text="Scale Degree:",font = 'HiraginoSans 16', bg="#eeeeee", fg="black", borderwidth=4, pady=4)
        scale.grid(row=0, column=0)

        btn.alterScale(chord, self.scaleFrame)

    def settings(self, mainFrame, btn, chord):
        #Settings frame
        settingsFrame = tk.Frame(mainFrame, borderwidth=2, bg="white", pady=7)
        settingsFrame.grid(row=3, column=0)
        settingsFrame.columnconfigure([0,4], weight=1)
        settingsFrame.rowconfigure([0,1], weight=1)
        self.triad(settingsFrame, btn, chord)
        self.extend(settingsFrame, btn, chord)
        self.inver(settingsFrame, btn, chord)

    def triad(self, settingsFrame, btn, chord):
        #Triad Frame
        triadFrame = tk.Frame(settingsFrame, borderwidth=5, background="white")
        triadFrame.grid()
        triadType = tk.Label(triadFrame, text="Triad Type", font = 'HiraginoSans 12', background="white", foreground="black")
        triadType.grid(row=0, column=0, sticky="w")

        optionsTri = ["Major", "Minor", "Diminished", "Augmented", "Suspended 2nd", "Suspended 4th"]
        indexTri = 0
        buttonsTri=[]

        for i in range(len(optionsTri)):
            if i == 0:
                bg="#c8f59c"
            else:
                bg='#d9d9d9'

            border = tk.Frame(triadFrame, borderwidth=2, bg="white")
            ex = tk.Label(border, text = optionsTri[i], font = 'HiraginoSans 16', bg=bg, fg="black", width=12, height=1, pady=5, padx=5)
            ex.bind('<Button>', lambda  ex=ex,index=indexTri, buttonsList=buttonsTri: btn.triadRadioBox(buttonsList, index, chord, self.scaleFrame))
            indexTri+= 1
            border.grid(column=i//4, row=i%4 + 1)
            ex.grid()
            buttonsTri.append(ex)

    def extend(self, settingsFrame, btn, chord):
        #Extensions
        extendFrame = tk.Frame(settingsFrame, borderwidth=5, background="white")
        extendFrame.grid(row=0, column=1)
        extensionsText = tk.Label(extendFrame, text="Extensions",font = 'HiraginoSans 12', background="white", foreground="black")
        extensionsText.grid(row=0, column=0, sticky="w")

        pos = 0
        for i in range(len(self.optionsEx)):
            if self.optionsEx[i] is not None:
                border = tk.Frame(extendFrame, borderwidth=2, bg="white")
                ex = tk.Label(border, text = self.optionsEx[i], font = 'HiraginoSans 16', bg="#d9d9d9", fg="black",  width=9, height=1, pady=5, padx=18)
                ex.bind('<Button>', lambda  ex=ex,index=self.indexEx, buttonsList=self.buttonsEx: btn.checkBox(buttonsList, index, chord, self.buttonsInver, self.scaleFrame))
                self.indexEx+= 1
                border.grid(column=pos//4, row=pos%4+1)
                ex.grid()
                self.buttonsEx.append(ex)
                pos+=1
    
    def inver(self, settingsFrame, btn, chord):
        #Inversions
        inverFrame = tk.Frame(settingsFrame, borderwidth=5, bg="white")
        inverFrame.grid(row=0, column=3, sticky="n")
        inversions = tk.Label(inverFrame, text="Inversions", font = 'HiraginoSans 12', background="white", foreground="black")
        inversions.grid(row=0, column=0, sticky="w")

        for i in range(len(self.optionsInver)):
            if i == 0:
                bg="#c8f59c"
            elif i == 3:
                bg="#b7b7b7"
            else:
                bg='#d9d9d9'

            border = tk.Frame(inverFrame, borderwidth=2, bg="white")
            ex = tk.Label(border, text = self.optionsInver[i], font = 'HiraginoSans 16', bg=bg, fg="black" ,width=14, height=1, pady=5, padx=5)
            ex.bind('<Button>', lambda  ex=ex,index=self.indexInver, buttonsList=self.buttonsInver: btn.inverRadioBox(buttonsList, index, chord, self.scaleFrame))
            self.indexInver+= 1
            border.grid(column=i//4, row=i%4+1)
            ex.grid()
            self.buttonsInver.append(ex)

    def information(self, mainFrame, btn):
        #Information frame
        btn.informationFrame = tk.Frame(mainFrame, borderwidth=5, background="#eeeeee", pady=7)
        btn.informationFrame.grid(row=4, column=0)
        btn.informationFrame.columnconfigure([0,1], weight=1)
        btn.informationFrame.rowconfigure(0, weight=1, minsize=10)

        btn.info = tk.Label(btn.informationFrame, text="Information                                                                                                                                                                                   ", font = 'HiraginoSans 12', background="white", foreground="black", borderwidth=5)
        btn.setInformationText()