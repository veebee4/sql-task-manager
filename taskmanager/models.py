from taskmanager import db # db = declarative base


# Previously had to import each column type at the top of the page but Flask-SQLAlchemy db variable contains all of them so can just use dot notation as per below
class Category(db.Model):
    # schema for the Category model
    id = db.Column(db.Integer, primary_key=True) # column variable, auto increments
    category_name = db.Column(db.String(25), unique=True, nullable=False) # max char's 25 can be bigger/smaller, unique ensures each new category is unique, nullable = required field
    tasks = db.relationship("Task", backref="category", cascade="all, delete", lazy=True) # this is to link the foreign key in the task table, backref establishes bidirectional rel reverses one to many to many to one
    #it needs to back reference itself (Category) but in lowercase, cascade finds all tasks linked and deletes, lazy means when querying db for categories it can identify any task linked to it
    
    def __repr__(self): # 'represent' class objects as a string, __repr__ represents itself in form of string
        return self.category_name




class Task(db.Model):
    # schema for the Task model
    id = db.Column(db.Integer, primary_key=True) # column variable, auto increments
    task_name = db.Column(db.String(50), unique=True, nullable=False)
    task_description = db.Column(db.Text, nullable=False)
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False) # this column uses ForeignKey to access primary key "id" in category tabl
    # ondelete="CASCADE" means if one category is deleted, it will perform a cascading effect to also delete any tasks linked to that category

    def __repr__(self): # 'represent' class objects as a string, __repr__ represents itself in form of string
        return "#{0} - Task: {1} | Urgent: {2}".format(
            self.id, self.task_name, self.is_urgent
        ) # utilising python formatting
        #alt could use fstring, e.g - f"#{self.id} - Task: {self.task_name} | Urgent: {self.is_urgent}"
