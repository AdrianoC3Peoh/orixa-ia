from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, Text, JSON, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./orixa.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    senha_hash = Column(String, nullable=True)
    google_id = Column(String, unique=True, nullable=True, index=True)
    is_premium = Column(Boolean, default=False)
    disclaimer_aceito = Column(Boolean, default=False)
    criado_em = Column(DateTime, default=datetime.utcnow)


class Resultado(Base):
    __tablename__ = "resultados"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True, nullable=False)
    primario = Column(String, nullable=False)
    secundario = Column(String, nullable=False)
    scores = Column(JSON, nullable=False)
    percentuais = Column(JSON, nullable=False)
    respostas = Column(JSON, nullable=False)
    criado_em = Column(DateTime, default=datetime.utcnow)


class MensagemChat(Base):
    __tablename__ = "mensagens_chat"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True, nullable=False)
    role = Column(String, nullable=False)
    conteudo = Column(Text, nullable=False)
    criado_em = Column(DateTime, default=datetime.utcnow)


class Centro(Base):
    __tablename__ = "centros"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    tradicao = Column(String, nullable=False)  # Candomblé, Umbanda, etc.
    endereco = Column(String, nullable=False)
    cidade = Column(String, nullable=False)
    estado = Column(String, nullable=False)
    cep = Column(String, nullable=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    telefone = Column(String, nullable=True)
    site = Column(String, nullable=True)
    ativo = Column(Boolean, default=True)
    criado_em = Column(DateTime, default=datetime.utcnow)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


CENTROS_INICIAIS = [
    {
        "nome": "Ilê Axé Opô Afonjá",
        "tradicao": "Candomblé Ketu",
        "endereco": "Rua Manoel Vitorino, 71 — Itapuã",
        "cidade": "Salvador",
        "estado": "BA",
        "latitude": -12.9285,
        "longitude": -38.3395,
        "telefone": "(71) 3384-2160",
        "site": "https://www.ileopoafonja.com.br",
    },
    {
        "nome": "Terreiro de Candomblé Ilê Omolu Oxum",
        "tradicao": "Candomblé",
        "endereco": "Av. Sapopemba, 4567",
        "cidade": "São Paulo",
        "estado": "SP",
        "latitude": -23.5896,
        "longitude": -46.4631,
        "telefone": None,
        "site": None,
    },
    {
        "nome": "Centro Espírita de Umbanda Estrela do Oriente",
        "tradicao": "Umbanda",
        "endereco": "Rua das Flores, 234 — Vila Mariana",
        "cidade": "São Paulo",
        "estado": "SP",
        "latitude": -23.5897,
        "longitude": -46.6336,
        "telefone": None,
        "site": None,
    },
    {
        "nome": "Terreiro Ilê Axé Xangô e Oxum",
        "tradicao": "Candomblé Ketu",
        "endereco": "Estrada do Alvarenga, 890",
        "cidade": "São Bernardo do Campo",
        "estado": "SP",
        "latitude": -23.7231,
        "longitude": -46.5597,
        "telefone": None,
        "site": None,
    },
    {
        "nome": "Tenda Espírita Nossa Senhora da Conceição",
        "tradicao": "Umbanda",
        "endereco": "Rua Voluntários da Pátria, 1200 — Santana",
        "cidade": "São Paulo",
        "estado": "SP",
        "latitude": -23.4931,
        "longitude": -46.6278,
        "telefone": None,
        "site": None,
    },
    {
        "nome": "Ilê Axé Ogum Meji",
        "tradicao": "Candomblé Angola",
        "endereco": "Estrada da Cachoeira, 340",
        "cidade": "Rio de Janeiro",
        "estado": "RJ",
        "latitude": -22.9068,
        "longitude": -43.1729,
        "telefone": None,
        "site": None,
    },
    {
        "nome": "Centro de Umbanda Pai Oxalá",
        "tradicao": "Umbanda",
        "endereco": "Rua Conde de Bonfim, 800 — Tijuca",
        "cidade": "Rio de Janeiro",
        "estado": "RJ",
        "latitude": -22.9249,
        "longitude": -43.2480,
        "telefone": None,
        "site": None,
    },
    {
        "nome": "Terreiro Ilê Asé Omim Yemonjá",
        "tradicao": "Candomblé Ketu",
        "endereco": "Av. Brasil, 15000 — Penha",
        "cidade": "Rio de Janeiro",
        "estado": "RJ",
        "latitude": -22.8567,
        "longitude": -43.2812,
        "telefone": None,
        "site": None,
    },
]


def init_db():
    Base.metadata.create_all(bind=engine)
    _popular_centros()


def _popular_centros():
    db = SessionLocal()
    try:
        if db.query(Centro).count() == 0:
            for c in CENTROS_INICIAIS:
                db.add(Centro(**c))
            db.commit()
    finally:
        db.close()
