import os
from flask import Flask, render_template, request, jsonify, url_for
from dotenv import load_dotenv
import requests

load_dotenv()
app = Flask(__name__)
KHIPU_API_KEY = os.getenv('KHIPU_API_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/crear_pago', methods=['POST'])
def crear_pago():
    data = request.json
    monto = data.get('monto')
    subject = data.get('subject')
    correo = data.get('correo', 'cliente@correo.com')

    return_url = url_for('exito', _external=True)
    cancel_url = url_for('index', _external=True)

    payload = {
        'amount': float(monto),
        'currency': 'CLP',
        'subject': subject,
        'payer_email': correo,
        'return_url': return_url,
        'cancel_url': cancel_url
    }

    headers = {
        'Content-Type': 'application/json',
        'x-api-key': KHIPU_API_KEY
    }

    response = requests.post('https://payment-api.khipu.com/v3/payments', json=payload, headers=headers)

    if response.status_code == 200:
        payment_id = response.json().get('payment_id')
        return jsonify({'payment_id': payment_id})
    else:
        return jsonify({'error': response.text}), 400

@app.route('/estado_pago')
def estado_pago():
    payment_id = request.args.get('payment_id')
    return render_template('estado.html', payment_id=payment_id)

@app.route('/verificar_pago')
def verificar_pago():
    payment_id = request.args.get('payment_id')
    if not payment_id:
        return {'status': 'error', 'message': 'Falta payment_id'}

    url = f'https://payment-api.khipu.com/v3/payments/{payment_id}'
    headers = {
        'x-api-key': KHIPU_API_KEY
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        estado = response.json().get('status')
        return {'status': estado}
    else:
        return {'status': 'error', 'message': 'Error al consultar Khipu'}

@app.route('/exito')
def exito():
    return render_template('exito.html')

if __name__ == '__main__':
    app.run(debug=True)
