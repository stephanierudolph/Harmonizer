import pyo as pyo
import copy

class Chord():
    def __init__(self):
        self.chord = [0, 4, 7]
        self.inversion = 0
        self.extentions = []
        self.output =[0, 4, 7]
        
        self.on = False
        self.server = None
        self.mic = None
        self.jobs = None

        self.extentionsList = [10, 11, 13, 14, 17, 21]
        self.chordsList = [[0, 4, 7], [0, 3, 7], [0, 3, 6], [0, 4, 8], [0, 2, 7], [0, 5, 7]]

    def start(self):
        self.on = True
        self.jobs = []
        print("\nChord: " + str(self.chord) + "\nInversions: "+ str(self.inversion) + "\nExtentions: "+ str(self.extentions) + "\nOutput: "+ str(self.output))
       
        self.server = pyo.Server(duplex=1, nchnls=1)
        self.server.deactivateMidi()
        self.server.boot().start()
        self.mic = pyo.Input().out(0)

        for i in range(len(self.output)):
            if self.output[i] != 0:
                self.jobs.append(pyo.Harmonizer(self.mic, transpo=self.output[i]).out(1))

    def changeTriad(self, i):
        self.chord = self.chordsList[i] 
        self.output = self.chord
        for i in range(len(self.extentions)):
            if i not in self.extentions:
                self.output.append(self.extentions[i])
        if self.on == True:
            self.restart(True)

    def invert(self):
        if self.inversion == 0:
            self.output = copy.copy(self.chord)
        else:
            for i in range(len(self.chord)):
                if not (i < self.inversion):
                    self.output[i] = self.chord[i] - 12
                else:
                    temp = copy.deepcopy(self.chord[i])
                    self.output[i] = temp

    def addExtention(self, index):
        if self.extentionsList[index] not in self.extentions:
            self.extentions.append(self.extentionsList[index])
            self.chord.append(self.extentionsList[index])
            self.output.append(self.extentionsList[index])
            if self.on == True:
                self.restart(True)

    
    def removeExtention(self, index):
        if self.extentionsList[index] in self.extentions:
            self.extentions.remove(self.extentionsList[index])
            self.output.pop(self.chord.index(self.extentionsList[index]))
            self.chord.remove(self.extentionsList[index])
            if self.on == True:
                self.restart(True)

    def stop(self):
        self.server.stop()
        self.on = False

    def restart(self, i): # i = does it need to be inverted?
        if i: self.invert()
        self.stop()
        self.start()