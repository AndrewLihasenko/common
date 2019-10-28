from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def get_home():
    return render_template('home.html')

@app.route('/vegetables')
def get_vegetables():
    veget_list = ['beans', 'carrot', 'beetroot', 'cucumber']
    return render_template('vegetables.html', v_list=veget_list)

@app.route('/fruits')
def get_fruits():
    fruits = ['melon', 'apple', 'strawberry', 'grape']
    return render_template('fruits.html', f_list=fruits)

if __name__ == '__main__':
    app.run(debug=True)