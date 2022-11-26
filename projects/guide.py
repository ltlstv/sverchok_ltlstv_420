from PIL import Image

def Framework(fmwork=35):
    while fmwork<=1720:
        im = Image.open('C:/Users/student/Documents/122Б/Толстов/badapple-frames-main/frames/output_00%s.jpg' % (fmwork))
        im.show()
        fmwork+1
    fmwork = 35
    return fmwork 
Framework()