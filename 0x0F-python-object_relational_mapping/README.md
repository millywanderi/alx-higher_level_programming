# 0x0F. Python - Object-relational mapping

Project done during **Full Stack Software Engineering Studies at ALX Africa**. It aims to teach about how to connect to a MySQL database from a python script, what ORM means and how to map a Python Class to a MySQL table.

## Technologies
* MySQL 8.0.32-0ubuntu.20.04.2
* MySQLdb, version 2.1.1
* sqlalchemy, version 2.0.9
* Python Scripts written with Python 3.8.10
* Tested on Ubuntu 20.04.5 LTS

## Files
The following files are python scripts for MySQL:

| Filename | Description |

| -------- | ----------- |

| 0-select_states.py | A script that lists all states from the database hbtn_0e_0_usa |
| 1-filter_states.py | A script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa |
| 2-my_filter_states.py | A script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. |
| 3-my_safe_filter_states.py | A script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. |
| 4-cities_by_state.py | A script that lists all cities from the database hbtn_0e_4_usa. |
| 5-filter_cities.py | A script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa. |
| model_state.py | A python file that contains the class definition of a State and an instance Base = declarative_base(). |
| 7-model_state_fetch_all.py | A script that lists all State objects from the database hbtn_0e_6_usa. |
| 8-model_state_fetch_first.py | A script that prints the first State object from the database hbtn_0e_6_usa. |
| 9-model_state_filter_a.py | A script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa. |
| 10-model_state_my_get.py | A script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa. |
| 11-model_state_insert.py | A script that adds the State object “Louisiana” to the database hbtn_0e_6_usa. |
| 12-model_state_update_id_2.py | A script that changes the name of a State object from the database hbtn_0e_6_usa. |
| 13-model_state_delete_a.py | A script that deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa. |
| model_city.py | Contains the class definition of a City, which inherits from Base. |
| 14-model_city_fetch_by_state.py | A Python file similar to model_state.py named model_city.py that contains the class definition of a City. |
| relationship_city.py | Same as model_city.py |
| relationship_state.py | Contains the class definition of a State with a relationship with the class City. |
| 101-relationship_states_cities_list.py | A script that lists all State objects, and corresponding City objects, contained in the database hbtn_0e_101_usa. |
| 102-relationship_cities_states_list.py | A script that lists all City objects from the database hbtn_0e_101_usa. |
