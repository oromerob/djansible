from django import forms
from django.core.validators import *
from django.core.exceptions import ObjectDoesNotExist

from .models import Var


class VarModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(VarModelForm, self).__init__(*args, **kwargs)
        try:
            if self.instance.var_def.pk is not None:
                if self.instance.var_def.var_type is not None:
                    if self.instance.var_def.var_type.validator or self.instance.var_def.var_type.validator != "":
                        self.fields['value'].validators.append(
                            eval(self.instance.var_def.var_type.validator)
                        )
        except ObjectDoesNotExist:
            pass
        except Exception, e:
            raise e

    class Meta:
        model = Var
        fields = '__all__'
