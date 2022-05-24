import os


def generate_svg(n, m):
    with open("video/svg/res/stream.svg", "r") as f:
        graphics = f.read()

    y = max(8.08, min(8.08+(26-(26*n/m)), 33.3))
    arrow = '<path d="M 8 {} l 0.5 -0.3 l -0.5 -0.3 Z" fill="black" />'.format(y)
    graphics = graphics.replace("<!-- ARROW -->", arrow)

    number = '<text x="7.8" y="{0}" font-size="2" text-anchor="end" >{1}</text>'.format(y, n)
    graphics = graphics.replace("<!-- NUMBER -->", number)

    money = []
    for i in range(42, max(0, 41-int(42*n/m)), -1):
        if i % 2:
            money.append('<use xlink:href="#moneylevel0" width="10" height="10" x="7.5" y="{}" />'.format(i/2))
        else:
            money.append('<use xlink:href="#moneylevel1" width="10" height="10" x="7.5" y="{}" />'.format(i/2))

    graphics = graphics.replace("<!-- INSERT COINS -->", "\n".join(money))
    with open("video/svg/out.svg", "w") as f:
        f.write(graphics)

def render_svg():
    os.system("inkscape -f video/svg/out.svg -e video/svg/out.png")

if __name__ == '__main__':
    generate_svg(10000, 100000)
