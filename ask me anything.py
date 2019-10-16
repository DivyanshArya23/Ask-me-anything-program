import wx
import wolframalpha
import wikipedia

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,
        pos=wx.DefaultPosition,size=wx.size(450,100),
        style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.caption | wx.CLOSE_BOX | wx.CLIP_CHILDREN,
        title="Ask Me Anything")
        
while(True):
    input=raw_input("Ask Me Anything:")
    try:
        #wolframalpha
        app_id='9Y5V6Q-WV96LK6TEP'
        client=wolframalpha.Client(app_id)
        res=client.query(input)
        answer=next(res.results).text
        print answer
    except:
        #wikipedia
        print (wikipedia.summary(input))
