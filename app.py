from flask import Flask
import os


app = Flask(__name__)


def read_count():
    try:
        with open('data/count.txt', 'r') as f:
            count = int(f.read())
        return count
    except IOError:
        return 0


def save_count(count):
    # ensure the directory exists
    os.makedirs('data', exist_ok=True)
    with open('data/count.txt', 'w') as f:
        f.write(str(count))


@app.route("/")
def hello():
    count = read_count()    
    count += 1
    save_count(count);
    return "<h1 style='color:blue'>Hello World! {}</h1>".format(count)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
