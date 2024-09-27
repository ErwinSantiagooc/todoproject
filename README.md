# todoproject

## Members

Erwin Santiago Ortiz Calderon - 1151965

Luis Fernando Serrano Moreno  - 1151982

Cristian Alejandro Vega Cruz  - 1151963

# Django Product Management System


This project is a Django-based application designed to manage products, clients, credits, and payments. The project includes five primary models: ProductType, Product, Client, Credit, and Payment. These models are interconnected to provide a comprehensive management system for businesses.

Features

- ProductType: Represents different categories of products, with a status (active or inactive).

- Product: Stores information about products and links them to a ProductType.

- Client: Represents customers with attributes like name, email, and other contact details.

- Credit: Manages credit information, linking clients and products.

- Payment: Handles payments made towards credits by clients.

## Table of contents

- Installation

- Usage

- Models Overview

- License

## Installation

1. Clone the Repository:

    ```
    git clone https://github.com/ErwinSantiagooc/todoproject
    cd your-repository

2. Create a virtual environment

    ```
    python -m venv env
    source env/bin/activate  # In Linux/Mac
    .\env\Scripts\activate  # In Windows

3. Install the dependencies:

    ```
    pip install -r requirements.txt

4. Perform the migrations:

    ```
    python manage.py migrate

5. Create a superuser (optional but recommended for admin access)

    ```
    python manage.py createsuperuser

6. Run the development server:

    ```
    python manage.py runserver

Now you can access the application at http://127.0.0.1:8000/.

## Usage

After running the development server, you can access the Django admin panel at http://127.0.0.1:8000/admin/. Here, you can manage ProductType, Product, Client, Credit, and Payment models, as well as create, update, and delete records.

## Models Overview

### ProductType

- Fields:

    - name: The name of the product type.
    - status: The current status (active or inactive).

- Relaitonships:

    - One-to-Many relationship with Product (a product belongs to one ProductType).

### Product

- Fields:

    - name: The name of the product.
    - description: A detailed description of the product.
    - price: The price of the product
    - product_type: Foreign key to ProductType.

- Relationships:

    - Many-to-Many relationship with Credit.

### Client

- Fields:

    - name: The full name of the client.
    - email: The client's email address.
    - phone: The contact number of the client.

- Relationships:

    - One-to-Many relationship with Credit.
    - One-to-Many relationship with Payment.

### Credit

- Fields:

    - client: Foreign key to Client.
    - products: Many-to-Many relationship with Product.
    - Total amount: The number of products in the credit.
    - start_date: Date of creation of the credit.
    - end_date: Limit date of the credit.

- Relationships:

    - One-to-Many relationship with Payment.

### Payment

- Fields:

    - credit: Foreign key to Credit.
    - client: Foreign key to Client.
    - amount: The amount paid.
    - payment_date: Date in which the payment was made.

## License

This project is open-source
