# Product CRUD Handler

This project is a simple CRUD (Create, Read, Update, Delete) application for handling product information. It consists of a React frontend for the user interface and a Django backend for managing product data.

## Getting Started

### Prerequisites

Make sure you have the following software installed:

- Node.js and npm for React development
- Python and Django for the backend

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/product-crud-handler.git
   ```

2. Install dependencies:

   ```bash
   # Navigate to the React app directory
   cd product-crud-handler/frontend
   npm install


    # Navigate to the Django app directory

    cd ../backend
    pip install -r requirements.txt
   ```

3. Run the Django development server:

   ```bash
   # Inside the backend directory
   python manage.py runserver
   ```

4. Run the React app:
   ```bash
   # Inside the frontend directory
   npm start
   ```

### Usage

- Access the React app at http://localhost:3000 in your browser.
- The app allows you to add, view, update, and delete products.
- Products are managed through the Django backend at http://127.0.0.1:8000/products/.

### React App Structure

- App.js: The main React component containing the CRUD functionality.
- App.css: Stylesheet for the React app.

### Django Backend Structure

- views.py: Contains the Django views for handling product data.
- models.py: Defines the Product model.

### API Endpoints

- GET /products/: Retrieve all products.
- GET /products/{id}/: Retrieve a specific product by ID.
- POST /products/: Add a new product.
- DELETE /products/{id}/: Delete a product by ID.
- PUT /products/{id}/: Update a product by ID.

### Contributing
Feel free to contribute to the project by opening issues or pull requests. Follow the Contribution Guidelines for more details.

### License
This project is licensed under the MIT License - see the LICENSE file for details.