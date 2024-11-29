# webhook.py
import stripe
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def stripe_webhook():
    payload = request.get_data(as_text=True)
    sig_header = request.headers.get('Stripe-Signature')

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, "  whsec_2df5bcbb6b764eef1bafa44ed95b895b3630e4135cf988018488c3684a7e0344"
        )
    except ValueError:
        # Invalid payload
        return jsonify({'status': 'invalid payload'}), 400
    except stripe.error.SignatureVerificationError:
        # Invalid signature
        return jsonify({'status': 'invalid signature'}), 400

    # Handle the event types
    if event['type'] == 'invoice.payment_succeeded':
        invoice = event['data']['object']
        print(f"Invoice {invoice['id']} was paid.")
    
    if event['type'] == 'invoice.payment_failed':
        invoice = event['data']['object']
        print(f"Invoice {invoice['id']} payment failed.")
    
    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    # Run the Flask app
    app.run(port=4242)
