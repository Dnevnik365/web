from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class UserModel(Base):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str | None]
    login: Mapped[str]
    password: Mapped[str]
    role: Mapped[str]
    service: Mapped[str]
