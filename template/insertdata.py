rom PyQt5.QtSql import QSqlQuery, QSqlDatabase

con = QSqlDatabase.addDatabase("QSQLITE")
con.setDatabaseName("contacts.sqlite")
con.open()


name = "hghggkjhjggkjhghjgghj"
job = "Technical off"
email = "tomy@example.com"

query = QSqlQuery()
query.exec(
    f"""INSERT INTO contacts (name, job, email)
    VALUES ('{name}', '{job}', '{email}')"""
)
