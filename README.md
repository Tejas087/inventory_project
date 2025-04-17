# Mini Inventory Management System (API-based)

## Objective
Build a basic inventory management REST API using Django and Django REST Framework that allows users to:
- Add and view products
- Update stock
- Track low stock items

## Tech Stack
- **Language:** Python 3
- **Framework:** Django, Django REST Framework  
- **Database:** SQLite  
- **Tools:** Postman, Git/GitHub  

## Features
- Add Product (`POST`)
- View Products (`GET`)
- Update Stock (`PATCH/PUT`)
- Delete Product (`DELETE`)
- Filter products by name
- Track low stock items
  
## Permissions
- Public users: Read-only access
- Admin users: Full CRUD access
  
## Setup Instructions
Clone the repository:
```
git clone https://github.com/Tejas087/inventory_project.git
cd inventory
```
Create and activate virtual environment:
```
python -m venv venv
venv/bin/activate
```
Install dependencies:
```
pip install -r requirements.txt
```
Run migrations:
```
python manage.py migrate
```
Create superuser:
```
python manage.py createsuperuser
```
Run server:
```
python manage.py runserver
```
Access:

Admin Panel: http://127.0.0.1:8000/admin/

API Base URL: http://127.0.0.1:8000/api/

To see all list, 
http://127.0.0.1:8000/admin/api/products/



## Screenshots


![Screenshot_20250417_143947](https://github.com/user-attachments/assets/b19c65e1-7909-4963-aac6-763848cb2530)

![Screenshot_20250417_150705](https://github.com/user-attachments/assets/17fbad37-803f-4604-aa96-321e16ac1f9e)

