
def MapPlot(code):
    import csv, sys, os
    from BeautifulSoup import BeautifulSoup
    from random import randint
    from reportlab.graphics import renderPM
    from svglib.svglib import svg2rlg
    from garbledook import RoadRunner

    filters = ["Kevin Spacey"]
    queryResponse = RoadRunner(filters)
    print (queryResponse)
    static = os.path.abspath('./' + 'static' )
    randcodestat = static + '/' + str(code)
    totalnum = 0
    svgPath = os.path.abspath('.' + '/static' + '/USmap.svg')
    svg = open(svgPath, 'r').read()
    soup = BeautifulSoup(svg, selfClosingTags=['defs','sodipodi:namedview'])
    paths = soup.findAll('path')
    pathStyle = "font-size:12px;fill-rule:nonzero;stroke:#050505;stroke-opacity:1;stroke-width:0.1;stroke-miterlimit:4;stroke-dasharray:none;stroke-linecap:none;marker-start:none;stroke-linejoin:bevel;fill:"
    count = 0
    num = 0

    for elem in queryResponse:
        totalnum = totalnum + elem[1]


    for p in paths:
        num = 0
        p['style'] = pathStyle + ('#D3D3D3;')
        if p['id'] not in ['State_Lines', 'separator']:
            try:
                for entry in queryResponse:
                    if p['inkscape:label'].decode("utf-8") == entry[0]:
                        print "gay"
                        num = entry[1]
                        x =  (hex(255 - int(round((255*num/totalnum))))[2:])
                        p['style'] = pathStyle + ('#' + x + x + x + ';')
                        break
            except:
                continue

    
    x = soup.prettify()
    tempcode = '/temp' + str(code)
    tempfile = open((static + tempcode + '.svg'), 'w')
    tempfile.write(x)
    tempfile.close()
    drawing = svg2rlg((static + tempcode + '.svg'))
    renderPM.drawToFile(drawing, static + '/' + str(code) + '.png')
    os.remove((static + tempcode + '.svg'))

if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    MapPlot(args[0])

