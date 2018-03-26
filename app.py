from flask import Flask, render_template
import configmodule

app = Flask(__name__)
app.config.from_object(configmodule.DevelopmentConfig)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
