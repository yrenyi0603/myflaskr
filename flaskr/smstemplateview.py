from flask import (
    Blueprint, request, jsonify
)
from .databases import SmsSign, SmsTemplate
from flaskr import db
import uuid

tp = Blueprint('smstemplateview', __name__)


# tp = Blueprint('smstemplate', __name__, url_prefix='/smstemplate')


@tp.route("/<action>")
def index(action):
    # action = request.headers['xxx']
    # add
    if action == '1':
        template = SmsTemplate(templateName="123", templateContent="321", smsType=1, international=1, remark="1234321")
        db.session.add(template)
        db.session.commit()
        return {"uuid": uuid.uuid4(), 'id': template.templateId}
    # update
    if action == '2':
        template = SmsTemplate.query.filter_by(templateId=1).first()
        template.templateName = "xxoo"
        template.statusCode = 0
        template.reviewReply = "xxoo"
        db.session.commit()
        return {"uuid": uuid.uuid4(), 'id': template.templateId}
    # query
    if action == '3':
        templates = SmsTemplate.query.filter(SmsTemplate.templateId.in_([1, 2, 4, 61])).all()
        return jsonify([i.to_json() for i in templates])
