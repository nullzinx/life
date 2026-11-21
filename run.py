from setup import app,db
from services.diary import diary
from services.public import public_bp
from services.habits import habits_bp
from services.wish_list import wish_list_bp


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.register_blueprint(public_bp)
    app.register_blueprint(wish_list_bp,url_prefix="/wishlist")
    app.register_blueprint(diary,url_prefix="/diary") 
    app.register_blueprint(habits_bp,url_prefix="/habits") 
    app.run(debug=True)

