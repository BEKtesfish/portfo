from flask import Flask,render_template,request,redirect
import csv

app = Flask(__name__)
print(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')
  
@app.route("/<string:page_name>")
def html_pages(page_name):
    return render_template(page_name)

def writefile_to(data):
	with open('database.txt', 'a') as  database:
		email=data['email']
		subject=data['subject']
		message=data['message']
		file= database.write(f'\n{email},{subject},{message}')

def writefile_to_csv(data):
	with open('database.csv', 'a', newline='') as  database2:
		email=data['email']
		subject=data['subject']
		message=data['message']
		csv_writer=csv.writer(database2, delimiter=',' , quotechar='"',quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method=='POST':
    	try:
	    	data=request.form.to_dict()
	    	writefile_to_csv(data)
	    	return redirect('/thank_you.html')
	    except:
	    	return 'did not save to database'
    else:
    	return'sumething went wrong. try again!'
  