# app.py
import stripe
from flask import Flask, render_template, request, jsonify
from invoice import create_invoice, get_invoice_status
from mailsender import send_email

stripe.api_key = "sk_test_51QHUlh012FCv0eNDHGhjo5qL4YY1UhasR7UGRgCX1k9k3h9RpfDfqhbcAwCR01mep8EzXmrRMvPOeijm3udgpUF800rbVb6sdT"


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('invoice.html')

@app.route('/create_invoice', methods=['POST'])
def create_invoice_route():
    data = request.get_json()
    email = data.get('email')
    amount = int(data.get('amount')) * 100  # Convert dollars to cents for Stripe
    invoice = create_invoice(email, amount)
    send_email('Madhusudan@veersatech.com',invoice.hosted_invoice_url,amount,'test Invoice')
    return jsonify({'invoice_id': invoice.id, 'invoice_url': invoice.hosted_invoice_url})
    

@app.route('/invoice_status/<invoice_id>', methods=['GET'])
def invoice_status(invoice_id):
    status = get_invoice_status(invoice_id)
    return jsonify({'status': status})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
