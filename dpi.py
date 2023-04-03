from PIL import Image
import glob, os

jpegler=glob.glob("*.jpeg")
jpegler.extend(glob.glob("*.jpg"))

print( "İŞLEM ÖNGÖRÜLEN JPGLER:", jpegler)
for file in jpegler:
    Image.open(file).save("400dpi-"+file, dpi=(400,400))
    print("400 DPI!",  file)
    
pngler=glob.glob("*.png")
print( "İŞLEM ÖNGÖRÜLEN PNGLER:", pngler)

for file in pngler:
    print("UYUMLULUK MODU!",  file)
    im1 = Image.open(file).convert('RGB')
    new = file.replace(".png",".jpg")
    im1.save(new)
    im2 = Image.open(new)
    im2.save("400dpi-"+new, dpi=(400,400))
    print("400 DPI!",new)

    
    

