from kintai.models import UserData

# USER_DATAをSEQ_USER_IDをキーに検索する
def get_user(seq_user_id):
    return UserData.objects.get(seq_user_id=seq_user_id)