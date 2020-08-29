
import wx
import os, sys
from random import randint


cards=[
    ["img\\2H.png","You"],["img\\2S.png","You"],["img\\2C.png","You"],["img\\2D.png","You"],
    ["img\\3H.png","Me"],["img\\3S.png","Me"],["img\\3C.png","Me"],["img\\3D.png","Me"],
    ["img\\4H.png","Never Have I Ever"],["img\\4S.png","Never Have I Ever"],["img\\4C.png","Never Have I Ever"],["img\\4D.png","Never Have I Ever"],
    ["img\\5H.png","Guys"],["img\\5S.png","Guys"],["img\\5C.png","Guys"],["img\\5D.png","Guys"],
    ["img\\6H.png","Chicks"],["img\\6S.png","Chicks"],["img\\6C.png","Chicks"],["img\\6D.png","Chicks"],
    ["img\\7H.png","Moosemaster"],["img\\7S.png","Moosemaster"],["img\\7C.png","Moosemaster"],["img\\7D.png","Moosemaster"],
    ["img\\8H.png","Date"],["img\\8S.png","Date"],["img\\8C.png","Date"],["img\\8D.png","Date"],
    ["img\\9H.png","Whine (roast)"],["img\\9S.png","Whine (roast)"],["img\\9C.png","Whine (roast)"],["img\\9D.png","Whine (roast)"],
    ["img\\10H.png","Pick 10 People to drink"],["img\\10S.png","Pick 10 people to drink"],["img\\10C.png","Pick 10 people to drink"],["img\\10D.png","Pick 10 people to drink"],
    ["img\\JH.png","Ring Master (rule maker)"],["img\\JS.png","Ring Master (rule maker)"],["img\\JC.png","Ring Master (rule maker)"],["img\\JD.png","Ring Master (rule maker)"],
    ["img\\QH.png","Hostess"],["img\\QS.png","Hostess"],["img\\QC.png","Hostess"],["img\\QD.png","Hostess"],
    ["img\\KH.png","Host"],["img\\KS.png","Host"],["img\\KC.png","Host"],["img\\KD.png","Host"],
    ["img\\AH.png","Make a toast"],["img\\AS.png","Make a toast"],["img\\AC.png","Make a toast"],["img\\AD.png","Make a toast"]]


players=["Player 1", "Player 2", "Player 3", "Player 4","Player 5"]

num_player=5;
player_id=0;
num_cards=51;
class mainpage(wx.Frame): # bluetooth option
    def __init__(self,parent,id,title):
        global num_cards, num_player;
        global players, cards,player_id;
        screenSize=wx.DisplaySize()
        screenWidth=screenSize[0]
        screenHeight=screenSize[1]
        super(mainpage,self).__init__(parent,title=title,size=screenSize)
        
        panelR = 0
        panelG = 0
        panelB = 0

        panel = wx.Panel(self)
        panel.SetBackgroundColour(wx.Colour(panelR,panelG,panelB))
        
        
        labelTitlePosX = screenWidth*0.45
        labelTitlePosY = screenHeight*0.05
        
        labelTitle=wx.StaticText(panel,-1,players[player_id],pos=(labelTitlePosX,labelTitlePosY))
        labelTitleFont = wx.Font(50, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        labelTitle.SetFont(labelTitleFont)
        labelTitle.SetForegroundColour((255,255,255))
        

        player_id=player_id+1
        player_id = player_id%num_player

        imagePosX = screenWidth*0.2
        imagePosY = screenHeight/2-200
        

        ## Add stuff for image file 

        r = randint(0,num_cards)

        a=cards[r];
        cards.remove(a);

        num_cards=num_cards-1;

        if num_cards == 0:
             print("Deck over")
             

        png = wx.Image(a[0], wx.BITMAP_TYPE_ANY)

        png = png.Scale(200, 300, wx.IMAGE_QUALITY_HIGH)
        png = wx.BitmapFromImage(png)
                
        wx.StaticBitmap(panel, -1, png, (imagePosX, imagePosY), (200,300 ))

        ## Stuff for Rules:

        labelPosX = screenWidth*0.5
        labelPosY = screenHeight*0.5-50
        
        label=wx.StaticText(panel,-1,a[1],pos=(labelPosX,labelPosY))
        labelFont = wx.Font(20, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        label.SetFont(labelFont)
        label.SetForegroundColour((255,255,255))
        


        buttonFont = wx.Font(22, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Consolas')
        resetPosX = 0.55*screenWidth
        resetPosY = 0.8*screenHeight
        connectButtonPosX = 0.45*screenWidth
        connectButtonPosY = 0.8*screenHeight
        connectButtonWidth = 100
        connectButtonHeight = 50

        self.Button =wx.Button(panel,label='Randomize ',pos=(connectButtonPosX ,connectButtonPosY), size=(connectButtonWidth,connectButtonHeight),id=9)
        self.reset =wx.Button(panel,label='Reset ',pos=(resetPosX ,resetPosY), size=(connectButtonWidth,connectButtonHeight),id=10)
                
        self.Bind(wx.EVT_BUTTON,self.Connectbtn,id=9)
        self.Bind(wx.EVT_BUTTON,self.resetbtn,id=10)
        self.Maximize(True)
        self.Show()
        self.Fit()


    def Connectbtn(self,event):
            
            child=mainpage(parent=None,id=-1,title='Main again')
            self.Destroy()

    def resetbtn(self,event):
            global cards, num_cards
            num_cards=52;
            cards=[ ["img\\2H.png","You"],["img\\2S.png","You"],["img\\2C.png","You"],["img\\2D.png","You"],
                    ["img\\3H.png","Me"],["img\\3S.png","Me"],["img\\3C.png","Me"],["img\\3D.png","Me"],
                    ["img\\4H.png","Never Have I Ever"],["img\\4S.png","Never Have I Ever"],["img\\4C.png","Never Have I Ever"],["img\\4D.png","Never Have I Ever"],
                    ["img\\5H.png","Guys"],["img\\5S.png","Guys"],["img\\5C.png","Guys"],["img\\5D.png","Guys"],
                    ["img\\6H.png","Chicks"],["img\\6S.png","Chicks"],["img\\6C.png","Chicks"],["img\\6D.png","Chicks"],
                    ["img\\7H.png","Moosemaster"],["img\\7S.png","Moosemaster"],["img\\7C.png","Moosemaster"],["img\\7D.png","Moosemaster"],
                    ["img\\8H.png","Date"],["img\\8S.png","Date"],["img\\8C.png","Date"],["img\\8D.png","Date"],
                    ["img\\9H.png","Whine (roast)"],["img\\9S.png","Whine (roast)"],["img\\9C.png","Whine (roast)"],["img\\9D.png","Whine (roast)"],
                    ["img\\10H.png","Pick 10 People to drink"],["img\\10S.png","Pick 10 people to drink"],["img\\10C.png","Pick 10 people to drink"],["img\\10D.png","Pick 10 people to drink"],
                    ["img\\JH.png","Ring Master (rule maker)"],["img\\JS.png","Ring Master (rule maker)"],["img\\JC.png","Ring Master (rule maker)"],["img\\JD.png","Ring Master (rule maker)"],
                    ["img\\QH.png","Hostess"],["img\\QS.png","Hostess"],["img\\QC.png","Hostess"],["img\\QD.png","Hostess"],
                    ["img\\KH.png","Host"],["img\\KS.png","Host"],["img\\KC.png","Host"],["img\\KD.png","Host"],
                    ["img\\AH.png","Make a toast"],["img\\AS.png","Make a toast"],["img\\AC.png","Make a toast"],["img\\AD.png","Make a toast"]]

            child=mainpage(parent=None,id=-1,title='Main again')
            self.Destroy()


def main():

    app = wx.App()
    ex = mainpage(parent=None,id=-1,title='Main again')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()