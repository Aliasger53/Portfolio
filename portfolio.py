
from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route("/")
def my_web():
    return render_template('/index.html')


@app.route("/templates/<string:page_name>")
def contact(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('web_server\database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"\n {email},{subject},{message}")
        print(file)


def write_to_csv(data2):
    with open('web_server\database2.csv', mode='a') as database2:
        email = data2["email"]
        subject = data2["subject"]
        message = data2["message"]
        csv_writer = csv.writer(database2, delimiter=",", quotechar='|')
        csv_writer.writerow([email, subject, message])


@app.route('/templates/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data2 = request.form.to_dict()
        write_to_csv(data2)
        return redirect("/templates/thankyou.html")
    else:
        return "Something went wrong, try again"


if __name__ == '__main__':
    app.run()
