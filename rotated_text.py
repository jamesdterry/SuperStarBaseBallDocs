# rotated_text.py

from reportlab.platypus.flowables import Flowable

class RotatedText(Flowable):
    def __init__(self, text, fontname='Helvetica', fontsize=9, textcolor=None):
        Flowable.__init__(self)
        self.text = text
        self.fontname = fontname
        self.fontsize = fontsize
        self.textcolor = textcolor

    def draw(self):
        canvas = self.canv
        canvas.setFont(self.fontname, self.fontsize)
        if self.textcolor:
            canvas.setFillColor(self.textcolor)
        canvas.rotate(90)
        canvas.drawString(0, -1 * self.fontsize, self.text)
