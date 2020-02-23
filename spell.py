import cgi
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
import tempfile
import urllib
form = cgi.FieldStorage()
content = form.getvalue('filename')
fileh  = StringIO(content)
f1 = fileh.readline()
for x in f1:
    print(x)
