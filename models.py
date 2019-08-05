from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.mysql import TEXT, INTEGER
from sqlalchemy.orm import relationship
from connections import Base


class Product(Base):
    # 表的名字:
    __tablename__ = 'product'

    # 表的结构:
    id = Column(INTEGER, primary_key=True, autoincrement=True)  # ID
    updated_at = Column(INTEGER)  # 最后一次更新时间

    gp_icon = Column(TEXT)   # 图标
    gp_name = Column(TEXT)  # GP名称


class GPReview(Base):
    # 表的名字:
    __tablename__ = 'gp_review'

    # 表的结构:
    id = Column(INTEGER, primary_key=True, autoincrement=True)  # ID
    product_id = Column(INTEGER, ForeignKey(Product.id))
    avatar_url = Column(TEXT)   # 头像链接
    user_name = Column(TEXT)  # 用户名称