# invoice.py
import os
from dotenv import load_dotenv
import stripe

stripe.api_key = os.getenv("STRIPE_API_KEY")

def create_invoice(customer_email, amount):
    # Create a customer
    customer = stripe.Customer.create(email=customer_email)
       
    # Create the invoice
    invoice = stripe.Invoice.create(
        customer=customer.id,
        pending_invoice_items_behavior='exclude',
        collection_method='send_invoice',
        days_until_due=7,
    )

        # Create an invoice item
    # invoice_item = stripe.InvoiceItem.create(
    #     customer=customer.id,
    #     amount=amount,
    #     currency='usd',
    #     description='Service charge',
    # )

    invoice_item=stripe.InvoiceItem.create(
    customer=customer.id,
    invoice=invoice.id,
    currency="usd",
    amount=amount,
    description="Test Invoice"
    # price_data={
    #     'currency':'usd',
    #     'unit_amount':amount,
    #     'tax_behavior':'exclusive',
    #     'product':'prod_QzZIaT1gNFbF5J'
    # }
)
       
    invoice=stripe.Invoice.finalize_invoice(invoice.id)
     # Send the invoice
     #stripe.Invoice.send_invoice(invoice.id)
    return invoice

def get_invoice_status(invoice_id):
    #Retrieve the invoice by ID
    invoice = stripe.Invoice.retrieve(invoice_id)
    return invoice.status

