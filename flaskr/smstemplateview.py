from flask import (
    Blueprint, request, jsonify
)
from .databases import SmsSign, SmsTemplate
from flaskr import db
import uuid
# import json
from sqlalchemy import and_, or_

tp = Blueprint('smstemplateview', __name__)


# tp = Blueprint('smstemplate', __name__, url_prefix='/smstemplate')


# @tp.route("/<action>", methods=['POST', 'GET'])
@tp.route("/", methods=['POST', 'GET'])
def index():
    action = request.headers['X-Tc-Action']
    req = request.json
    if action == 'AddSmsTemplate':
        template = SmsTemplate(templateName=req['TemplateName'],
                               templateContent=req['TemplateContent'],
                               smsType=req['SmsType'],
                               international=req['International'],
                               remark=req['Remark'])
        db.session.add(template)
        db.session.commit()
        return {
            "Response": {
                "AddTemplateStatus": {
                    "TemplateId": template.templateId,
                    "RequestStatus": 'return successfully!'
                },
                "RequestId": uuid.uuid4()
            }
        }
        # return {"uuid": uuid.uuid4(), 'id': template.templateId}
    # update
    if action == 'ModifySmsTemplate':
        template = SmsTemplate.query.filter_by(templateId=req['TemplateId']).first()
        template.templateName = req['TemplateName']
        template.templateContent = req['TemplateContent']
        template.smsType = req['SmsType']
        template.international = req['International']
        template.remark = req['Remark']
        template.statusCode = 0

        db.session.commit()
        return {
            "Response": {
                "ModifyTemplateStatus": {
                    "TemplateId": template.templateId
                },
                "RequestId": uuid.uuid4()
            }
        }
    # query
    if action == 'DescribeSmsTemplateList':
        templates = SmsTemplate.query.filter(SmsTemplate.templateId.in_(req['TemplateIdSet'])).all()
        print([i.to_json() for i in templates])
        return {
            "Response": {
                "DescribeTemplateStatusSet": [i.to_json() for i in templates],
                "RequestId": uuid.uuid4()
            }
        }

    if action == 'AddSmsSign':
        smsSign = SmsSign(signName=req['SignName'],
                          signType=req['SignType'],
                          documentType=req['DocumentType'],
                          international=req['International'],
                          usedMethod=req['UsedMethod'],
                          proofImage=req['ProofImage'],
                          commissionImage=req['CommissionImage'],
                          remark=req['Remark'],
                          )
        db.session.add(smsSign)
        db.session.commit()
        return {
            "Response": {
                "AddSignStatus": {
                    "SignId": smsSign.signId,
                    "SignApplyId": smsSign.signApplyId
                },
                "RequestId": uuid.uuid4()
            }
        }
    if action == 'ModifySmsSign':
        smsSign = SmsSign.query.filter_by(signId=req['SignId']).first()
        smsSign.signName = req['SignName'],
        smsSign.signType = req['SignType'],
        smsSign.documentType = req['DocumentType'],
        smsSign.international = req['International'],
        smsSign.usedMethod = req['UsedMethod'],
        smsSign.proofImage = req['ProofImage'],
        smsSign.commissionImage = req['CommissionImage'],
        smsSign.remark = req['Remark'],
        smsSign.statusCode = 0
        db.session.commit()
        print(smsSign.to_json())
        return {
            "Response": {
                "ModifySignStatus": {
                    "SignId": smsSign.signId,
                    "SignApplyId": smsSign.signApplyId
                },
                "RequestId": uuid.uuid4()
            }
        }

    if action == 'DescribeSmsSignList':
        ssmsSigns = SmsSign.query.filter(and_(SmsSign.signId.in_(req['SignIdSet']),
                                              SmsSign.international == req['International']
                                              )).all()
        # print(json.dumps([i.to_json() for i in ssmsSigns]))
        return {
            "Response": {
                "DescribeSignListStatusSet": [i.to_json() for i in ssmsSigns],
                "RequestId": uuid.uuid4()
            }
        }
