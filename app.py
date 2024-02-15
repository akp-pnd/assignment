from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    # Get the user agent from the request headers
    user_agent = request.headers.get('User-Agent')
    
    # Render HTML template with user agent info and styling
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Welcome</title>
        <style>
            body {
                text-align: center;
                font-size: 24px;
                background-color: lightblue;
                padding: 60px;
                color: green
            }
            .user-agent {
                font-size: 36px;
                color: red;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to 2022</h1>
        <p class="user-agent">Your user agent is: {{ user_agent }}</p>
    </body>
    </html>
    """
    
    # Render the template with user agent info
    return render_template_string(html, user_agent=user_agent)

if __name__ == '__main__':
    app.run(debug=True)
