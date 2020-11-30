from flask_sqlalchemy import SQLAlchemy
from flaskr import db, create_app
import datetime
import time
from flask_admin.model import typefmt

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username



class SmsTemplate(db.Model):
    __tablename__ = "smsTemplate"
    templateId = db.Column(db.Integer, primary_key=True)
    templateName = db.Column(db.String(200))
    templateContent = db.Column(db.String(500))
    smsType = db.Column(db.Integer)
    international = db.Column(db.Integer)
    remark = db.Column(db.String(500))
    statusCode = db.Column(db.Integer, default=0)
    reviewReply = db.Column(db.String(500))
    createTime = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, templateName, templateContent, smsType, international, remark):
        self.templateName = templateName
        self.templateContent = templateContent
        self.smsType = smsType
        self.international = international
        self.remark = remark
        self.statusCode = 0

    def to_json(self):
        return {
            "TemplateId": self.templateId,
            "TemplateName": self.templateName,
            "International": self.international,
            "CreateTime": self.createTime.strftime('%Y-%m-%d %H:%M:%S'),
            "ReviewReply": self.reviewReply,
            "StatusCode": self.statusCode
        }


class SmsSign(db.Model):
    __tablename__ = "smsSign"
    signId = db.Column(db.Integer, primary_key=True)
    signApplyId = db.Column(db.Integer)
    signName = db.Column(db.String(200))
    signType = db.Column(db.Integer)
    documentType = db.Column(db.Integer)
    international = db.Column(db.Integer)
    usedMethod = db.Column(db.Integer)
    proofImage = db.Column(db.String(1000))
    commissionImage = db.Column(db.String(1000))
    remark = db.Column(db.String(500))
    statusCode = db.Column(db.Integer, default=0)
    reviewReply = db.Column(db.String(500))
    createTime = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, signName, signType, documentType, international, usedMethod, proofImage, commissionImage,
                 remark):
        self.signName = signName
        self.signType = signType
        self.documentType = documentType
        self.international = international
        self.usedMethod = usedMethod
        self.proofImage = proofImage
        self.commissionImage = commissionImage
        self.remark = remark

    def to_json(self):
        return {
            "SignId": self.signId,
            "SignName": self.signName,
            "International": self.international,
            "CreateTime": self.createTime.strftime('%Y-%m-%d %H:%M:%S'),
            "ReviewReply": self.reviewReply,
            "StatusCode": self.statusCode
        }
