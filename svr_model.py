from flask import Flask, request, render_template
from text2img_model import create_pipeline, text2img

# Initial Flask app
app = Flask(__name__)

# Define parameters
IMAGE_PATH = "static/output.jpg"

# Initial pipeline
pipeline = create_pipeline()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")
    else:
        # submit prompt -> generate image 
        user_input = request.form["prompt"]

        print("Start generate...")
        im = text2img(user_input, pipeline)
        print("Finish...")

        im.save(IMAGE_PATH)

        return render_template("index.html", image_url=IMAGE_PATH)
    
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8888, use_reloader=False)