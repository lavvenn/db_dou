from db.requests import add_child, create_all_tables, get_child_by_id
from models import Child


# create_all_tables()

add_child(Child(name="Иван", surname="Сергеевич", lastname="Петров", birthday="01/01/2016", groupa="A"))
add_child(Child(name="Петр", surname="Иванович", lastname="Сергеев", birthday="01/01/2017", groupa="A"))
add_child(Child(name="Сергей", surname="Петрович", lastname="Иванов", birthday="01/01/2016", groupa="A"))
