from flask import Flask
import configmodule

app = Flask(__name__)
app.config.from_object(configmodule.DevelopmentConfig)

@app.route('/')
def index():
    return "I love doing this!"

if __name__ == '__main__':
    app.run()
