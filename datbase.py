from sqlalchemy import create_engine, text

connection_string = "mysql+mysqlconnector://llklwysiap3fdn6g21ju:pscale_pw_kR0UUXCD2Gc4SDbYToPj4Ebmdlh6MAdjyMgh8Y3geOT@aws.connect.psdb.cloud:3306/myfirst_database"
engine = create_engine(connection_string, echo=True)


def insert_to_table(name, addresss, email):
  with engine.connect() as conn:
    name = name
    addresss = addresss
    email = email
    query = text(
      f"INSERT INTO People (fullname, address, email) VALUES ('{name}','{addresss}','{email}')"
    )
    conn.execute(query)
    conn.commit()
 