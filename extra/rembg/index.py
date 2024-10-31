from rembg import remove
from PIL import Image
inpath = 'armud.jpeg'
outpath = 'armud.png'
inp = Image.open(inpath)
# inp.show()
outp = remove(inp)
outp.save(outpath)

