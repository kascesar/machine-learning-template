"""
This module provides an Object-Relational Mapping (ORM) system for your 
database. It consists of two submodules: `database.py` and `tables.py`.

### Submodules

1. **database.py**: 
   This submodule manages the database connection and configuration. It 
   allows you to set up the connection string, connect to the database, 
   and handle any database-level operations such as creating or dropping 
   tables.

2. **tables.py**: 
   This submodule is responsible for defining the database schema. You can 
   create SQLAlchemy models or SQLModel tables here. Each model you define 
   will correspond to a table in the database. Upon execution, these tables 
   will be automatically created in the selected database based on the 
   models you define.

### Usage

- To define your database schema, import the required classes from 
  `tables.py` and define your models there.
- Ensure you configure your database connection in `database.py` 
  before running the application.

### Example

Here’s a simple example of defining a User model in `tables.py`:

```python
from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    email: str
```

### Notes

* Make sure the database server is running and accessible.
* Use migrations to manage schema changes in production environments effectively.
"""
