from flaskr import db
import datetime

from flask_admin.model import typefmt
import time


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    secretId = db.Column(db.String(100), unique=True, nullable=False)
    status = db.Column(db.Boolean)

    def __repr__(self):
        return '<User %r>' % self.secretId


class SmsTemplate(db.Model):
    __tablename__ = "smsTemplate"
    templateId = db.Column(db.Integer, primary_key=True)
    templateName = db.Column(db.String(200))
    templateContent = db.Column(db.String(500))
    smsType = db.Column(db.Integer)
    international = db.Column(db.Integer)
    remark = db.Column(db.String(500))
    statusCode = db.Column(db.Integer, default=1)
    reviewReply = db.Column(db.String(500))
    createTime = db.Column(db.DateTime, default=datetime.datetime.now)
    secretId = db.Column(db.String(100))

    def __init__(self, templateName, templateContent, smsType, international, remark, secretId):
        self.templateName = templateName
        self.templateContent = templateContent
        self.smsType = smsType
        self.international = international
        self.remark = remark
        self.secretId = secretId

    def to_json(self):
        return {
            "TemplateId": self.templateId,
            "TemplateName": self.templateName,
            "International": self.international,
            "CreateTime": int(time.mktime(self.createTime.timetuple())),
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
    proofImage = db.Column(db.Text)
    commissionImage = db.Column(db.Text)
    # remark = db.Column(db.String(500))
    remark = db.Column(db.Text)
    statusCode = db.Column(db.Integer, default=1)
    reviewReply = db.Column(db.String(500))
    createTime = db.Column(db.DateTime, default=datetime.datetime.now)
    secretId = db.Column(db.String(100))

    def __init__(self, signName, signType, documentType, international, usedMethod, proofImage, commissionImage,
                 remark, secretId):
        self.signName = signName
        self.signType = signType
        self.documentType = documentType
        self.international = international
        self.usedMethod = usedMethod
        self.proofImage = proofImage
        self.commissionImage = commissionImage
        self.remark = remark
        self.secretId = secretId

    def to_json(self):
        return {
            "SignId": self.signId,
            "SignName": self.signName,
            "International": self.international,
            "CreateTime": int(time.mktime(self.createTime.timetuple())),
            "ReviewReply": self.reviewReply,
            "StatusCode": self.statusCode
        }
