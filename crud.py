from sqlalchemy import create_engine

engine = create_engine(DATABASE_URI)

Base.metadata.create_all(engine)