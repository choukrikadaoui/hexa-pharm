# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

PharmApp is a comprehensive Django-based Pharmacy Management System with PostgreSQL backend and Bootstrap 5 frontend.

## Common Development Commands

### Setup and Installation
```bash
# Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Database setup
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py seed_roles

# Run development server
python manage.py runserver
```

### Data Management
```bash
# Import medicines from CSV
python manage.py import_medicines path/to/medicines.csv

# Create database migrations
python manage.py makemigrations [app_name]

# Apply migrations
python manage.py migrate
```

## Architecture

### App Structure
- **core**: User roles and authentication management
- **inventory**: Medicine catalog, batch/lot tracking, stock movements
- **suppliers**: Supplier CRUD operations
- **purchases**: Purchase orders with automatic stock receiving
- **sales**: Point of sale with FIFO stock consumption
- **reports**: Analytics and reporting (low stock, near expiry)

### Key Models
- `Medicine`: Core product catalog with pricing and stock thresholds
- `Batch`: Lot tracking with expiry dates and FIFO stock management
- `StockMove`: All inventory movements (IN/OUT) with references
- `Purchase`/`PurchaseItem`: Purchase orders that auto-create stock
- `Sale`/`SaleItem`: Sales that auto-consume stock using FIFO
- `Supplier`: Vendor management
- `Customer`: Optional customer tracking

### FIFO Implementation
Stock consumption follows First-In-First-Out logic in `sales/models.py:SaleItem._consume_fifo()`. Batches are consumed by earliest expiry date, then by creation order.

### Database Configuration
PostgreSQL database required. Update credentials in `pharmapp/settings.py` before running migrations.