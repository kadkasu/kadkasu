pfrom flask imoprt, render_templete, request
app = Flask(__name__)
#create an object of the classs flask
# url/
@app.route('/')
def index():
return render_templete('index. html')
if __name__=='_main_':
    app.run(debug=true)