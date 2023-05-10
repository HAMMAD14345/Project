import torch
import pickle
from flask import Flask, render_template
from flask import Flask, request
from transformers import BertTokenizer, BertForSequenceClassification, BertModel




# load the tokenizer
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

app = Flask(__name__)

#app.secret_key = 'your_secret_key'
# load the model from the pickle file
with open('model3.pkl', 'rb') as f:
    model = pickle.load(f)

# set the device to GPU if available
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

from transformers import BertTokenizer, BertLMHeadModel


def generate_summary(text):
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BertLMHeadModel.from_pretrained('bert-base-uncased')
    input_ids = tokenizer.encode(text, return_tensors='pt', max_length=128)
    outputs = model.generate(input_ids=input_ids, max_length=50, early_stopping=True)
    summary = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return summary

   
    # generate a summary from the model
    with torch.no_grad():
        input_ids = inputs['input_ids'].to(device)
        attention_mask = inputs['attention_mask'].to(device)
        outputs = model.generate(input_ids=input_ids, attention_mask=attention_mask, max_length=50, early_stopping=True)
        summary = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return summary


@app.route("/")
def display():
    return render_template('front.html')


# get user input
@app.route('/summarize', methods=['POST'])
def summarize():
    text = request.form['input-text']
    summary = generate_summary(text)
    return render_template('front1.html',summary=summary)


if __name__ == "__main__":
    app.run(debug=True, port=7000) # change port to any available port number




