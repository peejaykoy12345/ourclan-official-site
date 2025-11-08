from OurClan import app, db

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    print("Registered routes:", app.url_map) 
    app.run(debug=False)
