#필요한 모듈을 단계적으로 import
from flask import Flask
 
app = Flask(__name__)
 
# 테스트 기능
@app.route('/hello')
def hello_Flask():
    return 'Hello, Flask'
 
if __name__ == '__main__':
    app.run(
    host="0.0.0.0",
    port=7777,
    debug=True)
 
