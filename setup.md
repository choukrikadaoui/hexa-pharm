# PharmApp - Pharmacy Management System Setup

## Installation Instructions

### 1. Prerequisites
- Python 3.9+
- PostgreSQL database

### 2. Setup Virtual Environment
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Configuration
1. Create a PostgreSQL database named `pharmacy_db`
2. Update database credentials in `pharmapp/settings.py`:
   - NAME: "pharmacy_db"
   - USER: "postgres"
   - PASSWORD: "yourpassword"
   - HOST: "localhost"
   - PORT: "5432"

### 5. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser
```bash
python manage.py createsuperuser
```

### 7. Create Default Roles
```bash
python manage.py seed_roles
```

### 8. Run Development Server
```bash
python manage.py runserver
```

The application will be available at http://127.0.0.1:8000/

## Features
- **Authentication & Roles**: Admin, Pharmacist, Cashier roles
- **Inventory Management**: Medicines with batch/lot tracking
- **FIFO Stock Management**: Automatic first-in-first-out stock consumption
- **Supplier Management**: Complete supplier CRUD operations
- **Purchase Orders**: Stock receiving with automatic batch creation
- **Point of Sale**: Fast sales with automatic stock deduction
- **Reports**: Low stock alerts, near expiry notifications
- **Bootstrap UI**: Responsive design for all devices

## Import Data
To import medicines from CSV file:
```bash
python manage.py import_medicines path/to/medicines.csv
```

CSV format: name,barcode,form,strength,manufacturer,tax_rate,unit_price,min_stock

## Admin Access
Visit http://127.0.0.1:8000/admin/ to access the Django admin interface.

## Navigation
- **Dashboard**: Overview with key metrics
- **Inventory**: Manage medicines and stock
- **Suppliers**: Manage supplier information
- **Purchases**: Create purchase orders and receive stock
- **Sales**: Point of sale and sales history
- **Reports**: Low stock and near expiry reports