from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from spellchecker import SpellChecker
app = Flask(__name__)
spell = SpellChecker()
@app.route('/upload')
def upload_file():
   return render_template('index.html')
	
@app.route('/uploader', methods = ['POST'])
def upload_files():
   if request.method == 'POST':
      l  =  list()
      m = list()
      f = request.files['file']
      f1 = f.readlines()
      z=list()
      x = str()
      for r in f1:
         p = r.decode("utf-8")
         p = p.replace('\n','')
         l.append(p.split(' '))
   for a in l:
      for n in a:
         m.append(n)
         #m.append(b)
   misspelled= spell.unknown(m)
   for word in m:
      z.append(spell.correction(word))
   #b = str(spell.correction(str(misspelled)))
   ans=""
   for y in range(0,len(z)):
      ans=ans+z[y] + " "
   return ans

		
if __name__ == '__main__':
   app.run(debug = True)
