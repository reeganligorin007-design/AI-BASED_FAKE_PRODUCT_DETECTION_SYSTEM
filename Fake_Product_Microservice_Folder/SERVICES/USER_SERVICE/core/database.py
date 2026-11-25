from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker , declarative_base

DATABASE_URL = "mysql+pymysql://root:Vishva%40123@localhost/auth_db"

engine = create_engine(DATABASE_URL,echo=True)
sessionlocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
base = declarative_base()