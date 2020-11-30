from flask_admin.contrib.sqla import ModelView
from flaskr import admin, db
from . import databases
from flask import (
    Blueprint
)

modv = Blueprint('modelview', __name__, url_prefix='/admin')


class SmSModelView(ModelView):
    # can_delete = False  # disable model deletion
    page_size = 50
    column_display_pk = True
    # can_create = False
    # can_edit = False
    can_view_details = True
    create_modal = True
    edit_modal = True
    can_export = True
    column_editable_list = ('statusCode', 'reviewReply')


# column_searchable_list = ['name', 'email']
# column_filters = ['country']
# column_editable_list = ['name', 'last_name']


class SmSTemplateModelView(SmSModelView):
    form_choices = {
        'smsType': [
            ('1', '营销短信'),
            ('0', '普通短信'),
        ],
        'statusCode': [
            ('1', '审核通过'),
            ('0', '审核失败'),
        ],
        'international': [
            ('1', '国际/港澳台短信'),
            ('0', '国内短信'),
        ]

    }

    # column_formatters = dict(statusCode=lambda x: '审核成功')
    # column_choices = {
    #     'smsType': [
    #         ('1', '营销短信'),
    #         ('0', '普通短信'),
    #     ],
    #     'statusCode': [
    #         ('1', '审核通过'),
    #         ('0', '审核失败'),
    #     ],
    #     'international': [
    #         ('1', '国际/港澳台短信'),
    #         ('0', '国内短信'),
    #     ]
    # }
    # column_labels=dict(statusCode="审核状态")


class SmSSignModelView(SmSModelView):
    form_choices = {
        'signType': [
            ('0', '公司'),
            ('1', 'APP'),
            ('2', '网站'),
            ('3', '公众号或者小程序'),
            ('4', '商标'),
            ('5', '政府/机关事业单位/其他机构'),
        ],
        'documentType': [
            ('0', '三证合一'),
            ('1', '企业营业执照'),
            ('2', '组织机构代码证书'),
            ('3', '社会信用代码证书'),
            ('4', '应用后台管理截图'),
            ('5', '网站备案后台截图'),
            ('6', '小程序设置页面截图'),
            ('7', '商标注册书'),
        ],
        'usedMethod': [
            ('0', '自用'),
            ('1', '他用'),
        ],
        'statusCode': [
            ('1', '审核通过'),
            ('0', '审核失败'),
        ],
        'international': [
            ('1', '国际/港澳台短信'),
            ('0', '国内短信'),
        ]

    }


admin.add_view(SmSTemplateModelView(databases.SmsTemplate, db.session, name="模板"))
admin.add_view(SmSSignModelView(databases.SmsSign, db.session, name="签名"))
