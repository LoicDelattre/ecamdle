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
            "Name": 200, 
            "Sex": 100, 
            "Role": 100, 
            "Asso": 100, 
            "Club": 100, 
            "Race": 100, 
            "Taille": 100, 
            "Appreciation": 100, 
            "BG": 100}
        
        self.analogButtonsColor = "#135f80"
        self.digitalButtonColor = "#642d96"
        
        self.status = ""
        self.color = "#"
        
        self.tryNumber = 0
        
        self.setupMainFrame()
        
        self.root.mainloop()
        
        pass
    
    def createEntryInFrame(self, frame: CTkFrame, text: str = "", width: int = 100):
        entry = CTkEntry(frame, width = width)
        entry.insert(1, text) 
        
        return entry 
    
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
            label = CTkLabel(topFrame, width = self.categories[category], text = category, fg_color = ("white", self.frameBgColor), corner_radius=self.labelRad)
            label.grid(row = 1, column = columnNum, padx = self.padTableX, pady = self.padTableY)
            columnNum += 1
          
        spacerBottomFrame = CTkFrame(mainFrame, height = 40, width = 600, fg_color = self.appBg, corner_radius=5)
        spacerBottomFrame.pack(side = BOTTOM)  
          
        bottomFrame = CTkFrame(mainFrame, height = 100, width = 900, fg_color = self.appBg, corner_radius=5)
        bottomFrame.pack(side = BOTTOM)  
        
        bottomFrame.buttonNewTry = CTkButton(master = bottomFrame, text="New Try", 
                                  command= lambda : self.addNewTryRow(topFrame), fg_color = self.frameBgColor)
        bottomFrame.buttonNewTry.place(relx = 0.5, rely = 0.3, anchor = CENTER)
        
        def moreEffect():
            self.color = "#e30b16"
            self.status = "MORE"
            pass
        
        def lessEffect():
            self.color = "#e30b16"
            self.status = "LESS"
            pass
        
        def equalEffect():
            self.color = "#1e850c"
            self.status = "EQUAL"
            pass
        
        def yesEffect():
            self.color = "#1e850c"
            self.status = "YES"
            pass
        
        def noEffect():
            self.color = "#e30b16"
            self.status = "NO"
            pass
        
        buttonMore = CTkButton(master = bottomFrame, text="More", 
                                  fg_color = self.analogButtonsColor, command = lambda : moreEffect())
        buttonMore.place(relx = 0.1, rely = 0.7, anchor = CENTER)
        
        buttonEqual = CTkButton(master = bottomFrame, text="Equal", 
                                  fg_color = self.analogButtonsColor, command = lambda : equalEffect())
        buttonEqual.place(relx = 0.3, rely = 0.7, anchor = CENTER)
        
        buttonLess = CTkButton(master = bottomFrame, text="Less", 
                                  fg_color = self.analogButtonsColor, command = lambda : lessEffect())
        buttonLess.place(relx = 0.5, rely = 0.7, anchor = CENTER)
        
        buttonYes = CTkButton(master = bottomFrame, text="Yes", 
                                  fg_color = self.digitalButtonColor, command = lambda : yesEffect())
        buttonYes.place(relx = 0.7, rely = 0.7, anchor = CENTER)
        
        buttonNo = CTkButton(master = bottomFrame, text="No", 
                                  fg_color = self.digitalButtonColor, command = lambda : noEffect())
        buttonNo.place(relx = 0.9, rely = 0.7, anchor = CENTER)
        
        pass
    
    def addNewTryRow(self, frame : CTkFrame):
        self.tryNumber += 1
        nameEntry = self.createEntryInFrame(frame, width = self.categories["Name"])
        nameEntry.grid(row = 1 + self.tryNumber, column = 1, padx = self.padTableX)

        columnNum : int = 2
        for category in self.categories:
            if category != "Name":
                button = CTkButton(frame, width = self.categories[category], text = "", 
                                       fg_color = ("white", self.frameBgColor), corner_radius=self.labelRad, command = lambda : self.applyStateToButton(button))
                button.grid(row = 1 + self.tryNumber, column = columnNum, padx = self.padTableX, pady = self.padTableY)
                columnNum += 1
            pass
    
    def applyStateToButton(self, button : CTkButton):
        button.configure(fg_color = self.color, text = self.status)
        pass
    
    def clearFrame(self, frame: CTkFrame):
        for widget in frame.winfo_children():
            widget.destroy()
            
        frame.pack_forget()
           
gui = GUI() 