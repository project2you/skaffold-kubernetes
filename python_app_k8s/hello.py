#author: Aniket Mukherjee
from flask import Flask
import emoji
import pyjokes

app=Flask(__name__)

@app.route('/')
def hello():
  return pyjokes.get_joke()
  

@app.route('/fun')
def fun():
  return emoji.emojize('Python development with Skaffold is :thumbs_up:')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
    
