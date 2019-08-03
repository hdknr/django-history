from django.forms.models import model_to_dict
from django.db.models import Model
from django.db.models.fields.files import FieldFile
from datetime import datetime
from enum import Enum
from decimal import Decimal
from rest_framework.utils import encoders
from io import IOBase
import json
import yaml

IGNORES = (IOBase, )


class JSONEncoder(encoders.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, IGNORES):
            return None
        if isinstance(obj, Model):
            return model_to_dict(obj)
        try:
            return super(JSONEncoder, self).default(obj)
        except:
            pass

    @classmethod
    def to_json(cls, obj, *args, **kwargs):
        return json.dumps(obj, cls=cls, *args, **kwargs)

    @classmethod
    def from_json(cls, jsonstr,  *args, **kwargs):
        return json.loads(jsonstr, *args, **kwargs)

    @classmethod
    def to_yaml(cls, obj, *args, **kwargs):
        if isinstance(obj, Model):
            obj = model_to_dict(obj)
        return yaml.safe_dump(obj, *args, **kwargs)

to_json = JSONEncoder.to_json
from_json = JSONEncoder.from_json
to_yaml = JSONEncoder.to_yaml
