def rgb(r, g, b):
    round = lambda x: min(255, max(0, x))
    hex = ("{:02X}" * 3).format(round(r), round(g), round(b))
    return hex

rgb(0,0,0)
rgb(1,2,3)
rgb(255,255,255)
rgb(254,253,252)
rgb(-20,275,125)