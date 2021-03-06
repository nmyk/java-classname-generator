from flask import Flask, render_template
from random import choice, sample
import yaml

app = Flask(__name__)
with open('data.yaml', 'r') as data_file:
    data = yaml.load(data_file)


@app.route("/")
def main():
    class_name = generate_class_name()
    return render_template('index.html', class_name=class_name)


def generate_class_name():
    first = choice(data['firsts'])
    middle = ''.join(sample(data['middles'], 4))
    last = choice(data['lasts'])
    return first + middle + last


if __name__ == "__main__":
    app.run(host='0.0.0.0')
