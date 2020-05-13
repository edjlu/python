html = '''
<div class="head">TYPE OF GAME:</div>
<div class="subtitle">Open World 3rd Person Shooter</div>
<div class="head">AVAILABLE ON:</div>
<div class="subtitle">PS4, PC (coming soon)</div>
<div class="head">DEVELOPER:</div>
<div class="subtitle">Guerilla Games</div>
<div class="head">RELEASE DATE:</div>
<div class="subtitle">February 28, 2017</div>
<div class="head">STRENGTHS:</div>
<div class="subtitle">Gorgeous visuals, intense and challenging combat, great enemy design and variety</div>
<div class="head">WEAKNESSES:</div>
<div class="subtitle">meh voice acting, terrible facial animations, open world is shallow</div>
<div class="head">PLAYTIME:</div>
'''.strip()

split = html.split('\n')
for i in range(0, len(split)-1, 2):
    innerHTML = '%s\n%s' % (split[i], split[i+1])
    print('<div class="info">\n%s\n</div>' % innerHTML)