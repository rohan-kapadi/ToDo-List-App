# run.py
from app import create_app, db

app = create_app()

if __name__ == "__main__":
    # Import models *inside* the app context
    with app.app_context():
        from app.models import Task   # ensures the model is registered
        db.create_all()               # creates tables if they don't exist

    app.run(debug=True)

    
