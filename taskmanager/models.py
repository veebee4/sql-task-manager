from taskmanager import db # db = declarative base


# Previously had to import each column type at the top of the page but Flask-SQLAlchemy db variable contains all of them so can just use dot notation as per below
class Category(db.model):
    # schema for the Category model
    id = db.Column(db.Integer, primary_key=True) # column variable, auto increments
    category_name = db.Column(db.String(25), unique=True, nullable=False) # max char's 25 can be bigger/smaller, unique ensures each new category is unique, nullable = required field

    
    def __repr__(self): # 'represent' class objects as a string, __repr__ represents itself in form of string
        return self.category_name




class Task(db.model):
    # schema for the Task model
    id = db.Column(db.Integer, primary_key=True) # column variable, auto increments
    task_name = db.Column(db.String(50), unique=True, nullable=False)
    task_description = db.Column(db.text, nullable=False)
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False) # this column uses ForeignKey to access primary key "id" in category tabl


    def __repr__(self): # 'represent' class objects as a string, __repr__ represents itself in form of string
        return self
