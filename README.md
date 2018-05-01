# viewHQ
A little, websockets-based Flask application that let's me change rendered views from a single control 'view HQ' of sorts. This is mainly a testing ground for a different application.

### Status
This test project has concluded. I have learned what I needed to learn and have transitioned the code to my other application. This repo will probably not be furthered updated.

### Who's this for?
This little application can serve as a starting ground for any Flask developer who wants to incorporate a view 'control HQ' of sorts; by that I mean, you can take this code and adapt it to your needs. You can do this by changing `app.py` to reflect your routes/views, and add your `.html` files into `templates`, and from `templates/control.html`, after you change the button values, you will be able to control the views connected clients have rendered.

### Python Requirements
* Python 3 (currently I am using v3.6.5 (Arch+ ftw), although this should work on any 3.x)
* Redis
* Flask
* Flask-SocketsIO

### Rock On
\m/

### License?
For once, I am putting this code in the public domain. Have fun.
