from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

# Update the base URL of your FastAPI server
FASTAPI_BASE_URL = "http://127.0.0.1:8082"

@app.route('/')
def index():
    return redirect('/add_data')

@app.route('/add_data', methods=['GET', 'POST'])
def add_data():
    if request.method == 'POST':
        # Collect form data
        data = {
            "phone_number": request.form.get("phone_number"),
            "field1": request.form.get("field1"),
            "field2": request.form.get("field2"),
            "field3": request.form.get("field3"),
            "field4": request.form.get("field4"),
            "field5": request.form.get("field5"),
            "field6": request.form.get("field6"),
            "field7": request.form.get("field7"),
            "field8": request.form.get("field8"),
            "field9": request.form.get("field9"),
            "field10": bool(request.form.get("field10"))
        }
        # Make POST request to your FastAPI endpoint
        requests.post(f"{FASTAPI_BASE_URL}/data/create", json=data)
        # return redirect('/view_data')
    return render_template('add_data.html')

@app.route('/view_data', methods=['GET', 'POST'])
def search_data():
    phone_number = request.form.get('phone_number', '').strip()  # Get phone number input
    size = request.form.get('size', '').strip()  # Get size input

    # Prepare query parameters
    query_params = {}
    if phone_number:
        query_params['phone_number'] = phone_number
    if size:
        query_params['size'] = size

    # Make the request to FastAPI
    try:
        response = requests.post(
            "http://127.0.0.1:8082/data/search",
            params=query_params  # Pass parameters as query string
        )

        # Check if the response is successful
        if response.status_code == 200:
            search_results = response.json()  # Get the results from the API
        else:
            search_results = []  # Handle cases where API fails
    except Exception as e:
        print(f"Error connecting to FastAPI: {e}")
        search_results = []

    # Render the results in the UI
    return render_template('view_data.html', data=search_results)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=8083)
