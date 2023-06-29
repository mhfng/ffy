from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Get the uploaded file from the request
        file = request.files['file']
        
        # Read the Excel file into a pandas DataFrame
        df = pd.read_excel(file)
        
        # Generate the pivot table
        pivot_table = df.pivot_table(index='Category', columns='Month', values='Sales', aggfunc='sum')
        
        # Convert the pivot table to HTML
        pivot_table_html = pivot_table.to_html()
        
        # Render the HTML template and pass the pivot table HTML to it
        return render_template('pivot_table.html', pivot_table=pivot_table_html)
    
    # Render the file upload form if no file is uploaded
    return render_template('upload.html')

if __name__ == '__main__':
    app.run()
