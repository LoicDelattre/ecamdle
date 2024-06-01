from customtkinter import *

from threading import *

class GUI:
    
    def __init__(self) -> None:
        self.root = CTk()
        self.windowTitle = "ECAMDLE"
        self.root.title(self.windowTitle)
        self.root.geometry('1080x820')
        
        self.labelBgColor = "#3e3261"
        self.frameBgColor = "#29276e"
        self.appBg = "#2b2b2b"
        self.blackBg = "#000000"
        self.labelRad = 4
        self.padTableX = 3
        self.padTableY = 3
        
        self.categories = {
            "Name": [200], 
            "Sex": [100, True], 
            "Role": [100, True], 
            "Asso": [100, True], 
            "Club": [100, True], 
            "Race": [100, True], 
            "Taille": [100, False], 
            "Appreciation": [100, False],
            "BG": [100, False]}
        
        self.analogButtonsColor = "#135f80"
        self.digitalButtonColor = "#642d96"

        self.validColor = "#1e850c"
        self.invalidColor = "#e30b16"
        
        self.tryNumber = 0
        self.currentTryButtonsStates = []
        
        self.digitalStates = ["YES", "NO"]
        self.analogStates = ["MORE", "LESS", "EQUAL"]
        
        self.setupMainFrame()
        
        self.root.mainloop()
        
        pass
    
    def createEntryInFrame(self, frame: CTkFrame, text: str = "", width: int = 100):
        entry = CTkEntry(frame, width = width)
        entry.insert(1, text) 
        
        return entry 
    
    def newBoard(self, frame : CTkFrame):
        self.clearFrame(frame)
        self.setupMainFrame()
        pass
    
    def setupMainFrame(self):
        mainFrame = CTkFrame(self.root)
        set_appearance_mode("dark")
        mainFrame.pack(side="top", expand=True, fill="both")
        
        spacerTopFrame = CTkFrame(mainFrame, height = 40, width = 600, fg_color = self.appBg, corner_radius=5)
        spacerTopFrame.pack(side = TOP)
        
        topFrame = CTkFrame(mainFrame, height = 100, width = 900, fg_color = self.appBg, corner_radius=5)
        topFrame.pack(side = TOP)
        
        #top categories
        columnNum : int = 1
        
        for category in self.categories:
            label = CTkLabel(topFrame, width = self.categories[category][0], text = category, fg_color = ("white", self.frameBgColor), corner_radius=self.labelRad)
            label.grid(row = 1, column = columnNum, padx = self.padTableX, pady = self.padTableY)
            columnNum += 1
          
        spacerBottomFrame = CTkFrame(mainFrame, height = 40, width = 600, fg_color = self.appBg, corner_radius=5)
        spacerBottomFrame.pack(side = BOTTOM)  
          
        bottomFrame = CTkFrame(mainFrame, height = 100, width = 900, fg_color = self.appBg, corner_radius=5)
        bottomFrame.pack(side = BOTTOM)  
        
        bottomFrame.buttonNewTry = CTkButton(master = bottomFrame, text="New Try", 
                                  command= lambda : self.addNewTryRow(topFrame), fg_color = self.frameBgColor)
        bottomFrame.buttonNewTry.place(relx = 0.3, rely = 0.7, anchor = CENTER)
        
        bottomFrame.buttonNewGame = CTkButton(master = bottomFrame, text="New Game", 
                                  command= lambda : self.newBoard(mainFrame), fg_color = self.frameBgColor)
        bottomFrame.buttonNewGame.place(relx = 0.7, rely = 0.7, anchor = CENTER)
             
        pass
    
    def addNewTryRow(self, frame : CTkFrame):
        self.currentTryButtonsStates = []
        self.tryNumber += 1
        nameEntry = self.createEntryInFrame(frame, width = self.categories["Name"][0])
        nameEntry.grid(row = 1 + self.tryNumber, column = 1, padx = self.padTableX)

        columnNum : int = 2
        for category in self.categories:
            if category != "Name":
                self.currentTryButtonsStates.append(0)
                button = CTkButton(frame, width = self.categories[category][0], text = "", 
                                       fg_color = ("white", self.frameBgColor), corner_radius=self.labelRad, hover = False)
                buttonNum = columnNum - 1
                button.configure(command = lambda button = button, buttonNum = buttonNum : self.applyStateToButton(button, buttonNum))
                button.grid(row = 1 + self.tryNumber, column = columnNum, padx = self.padTableX, pady = self.padTableY)
                columnNum += 1
            pass
    
    def applyStateToButton(self, button : CTkButton, buttonNum : int):
        categoryNum = 0
        maxToggleNum = 0
        isDigital = False
        for category in self.categories:
            if categoryNum == buttonNum:
                isDigital = self.categories[category][1]
                if isDigital:
                    maxToggleNum = 2
                else:
                    maxToggleNum = 3
                break
            categoryNum += 1
        
        buttonToggleValue = self.currentTryButtonsStates[buttonNum-1]
        
        if buttonToggleValue == maxToggleNum:
            self.currentTryButtonsStates[buttonNum-1] = 1
        else:
            self.currentTryButtonsStates[buttonNum-1] += 1
        
        color = ""
        status = ""
        if isDigital:
            status = self.digitalStates[buttonToggleValue - 1]
            if status == "YES":
                color = self.validColor
            else:
                color = self.invalidColor
        else:
            status = self.analogStates[buttonToggleValue - 1]  
            if status == "EQUAL":
                color = self.validColor
            else:
                color = self.invalidColor  
        
        button.configure(fg_color = color, text = status)
       
        pass
    
    def clearFrame(self, frame: CTkFrame):
        for widget in frame.winfo_children():
            widget.destroy()
            
        frame.pack_forget()
           
gui = GUI() 