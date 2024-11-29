from django.forms import ModelForm
from .models import SweetPost

class SweetPostForm(ModelForm):
    '''ModelFormのサブクラス
    '''
    class Meta:
        '''ModelFormのインナークラス
        
        Attributes:
          model: モデルのクラス
          fields: フォームで使用するモデルのフィールドを指定
        '''
        model = SweetPost
        fields = ['category', 'title', 'comment', 'image1', 'image2']
