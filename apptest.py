from flask import Flask
import requests, os

app = Flask(__name__)

# Set the URL of your Heroku app
heroku_app_url = "https://philonet-7f9320692cfa.herokuapp.com/"  # Replace with your app's URL

# Send a GET request to the root URL
response = requests.get(heroku_app_url)

# Check if the response status code is 200 (OK)
if response.status_code == 200:
    print("Success! The app is running.")
    print("Response content:")
    print(response.text)
else:
    print(f"Failed to access the app. Status code: {response.status_code}")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    app.run(debug=False)
