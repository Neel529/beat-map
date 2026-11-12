"""Build the single-file app: python src/build.py  ->  writes dev/index.html
Inlines Leaflet (src/leaflet.css, src/leaflet.js) and the shop data (src/stores.json) into src/template.html.
Promote to the main link by copying dev/index.html to index.html."""
import json,os
H=os.path.dirname(os.path.abspath(__file__))
t=open(os.path.join(H,'template.html'),encoding='utf-8').read()
s=json.dumps(json.load(open(os.path.join(H,'stores.json'),encoding='utf-8')),ensure_ascii=False,separators=(',',':')).replace('</','<\\/')
css=open(os.path.join(H,'leaflet.css'),encoding='utf-8').read();js=open(os.path.join(H,'leaflet.js'),encoding='utf-8').read()
o=t.replace('<!--LEAFLET_CSS-->','<style>'+css+'</style>').replace('<!--LEAFLET_JS-->','<script>'+js+'</script>').replace('__DATA__',s)
open(os.path.join(H,'..','dev','index.html'),'w',encoding='utf-8').write(o)
print('built dev/index.html')
