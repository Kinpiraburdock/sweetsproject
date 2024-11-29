from django.db import models
# accountsアプリのmodelsモジュールからCustomUserをインポート
from accounts.models import CustomUser

class Category(models.Model):
    '''投稿する写真のカテゴリを管理するモデル
    '''
    # カテゴリ名のフィールド
    title = models.CharField(
        verbose_name='カテゴリ',
        max_length=20)
    
    def __str__(self):
        '''オブジェクトを文字列に変換して返す
        
        Returns(str):カテゴリ名
        '''
        return self.title

class SweetPost(models.Model):
    '''投稿されたデータを管理するモデル
    '''

    user = models.ForeignKey(
        CustomUser,
        # フィールドのタイトル
        verbose_name='ユーザー',
        on_delete=models.CASCADE
        )

    category = models.ForeignKey(
        Category,
        # フィールドのタイトル
        verbose_name='カテゴリ',

        on_delete=models.PROTECT
        )
    # タイトル用のフィールド
    title = models.CharField(
        verbose_name='タイトル', 
        max_length=200        
        )
    # コメント用のフィールド
    comment = models.TextField(
        verbose_name='コメント',  
        )
    # イメージのフィールド1
    image1 = models.ImageField(
        verbose_name='イメージ1',
        upload_to = 'photos'   
        )
    # イメージのフィールド2
    image2 = models.ImageField(
        verbose_name='イメージ2',
        upload_to = 'photos',  
        blank=True,            
        null=True             
        )

    posted_at = models.DateTimeField(
        verbose_name='投稿日時',
        auto_now_add=True    
        )
    
    def __str__(self):
        '''オブジェクトを文字列に変換して返す
        
        Returns(str):投稿記事のタイトル
        '''
        return self.title
