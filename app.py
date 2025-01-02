# main entry point
# Contains Flask server setup and routes for request handling
from flask import Flask, render_template, request, jsonify
from summarize import Summarizer
from scrape import fetchArticle

app = Flask(__name__)
summarizer = Summarizer()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarizePage():
    try:
        url = request.form.get('url')
        num_sentences = int(request.form.get('num_sentences', 3))
    
        article_text = fetchArticle(url)
        if "Content not found" in article_text or "error" in article_text.lower():
            return render_template('summarize.html', error=article_text)
        
        summary = summarizer.summarize_text(article_text, num_sentences)
    
        return render_template('summarize.html', summary=summary, url=url)
    except Exception as e:
        return render_template('summarize.html', error=f"An error occurred: {e}")

    


if __name__ == '__main__':
    app.run(debug=True, port=8000)
