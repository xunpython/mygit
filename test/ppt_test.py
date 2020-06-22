from pptx import Presentation

prs = Presentation(r'C:\Users\13265\Desktop\1.pptx')
for sild in prs.slides:
    print(sild)