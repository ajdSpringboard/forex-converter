import requests
from flask import Flask, render_template, redirect, request
from forms import CurrencyForm


app = Flask(__name__)
app.config["SECRET_KEY"] = "BlahBlahBlah"

@app.route('/', methods=['GET', 'POST'])
def home():
    form = CurrencyForm()
    result = request.args.get('result')
    if form.validate_on_submit():
        curr_from = form.curr_from.data
        curr_to = form.curr_to.data
        amt = form.curr_amt.data
        url = f'https://api.exchangerate.host/convert?from={curr_from.upper()}&to={curr_to.upper()}&amount={amt}'
        
        response = requests.get(url)
        data = response.json()
        
        if data.get('result') != None:
            result=data['result']
            return redirect(f'/?result={result}')
        else:
            return redirect('/')
    return render_template('/home.html', form=form, result=result)


if __name__ == '__main__':
    app.run()