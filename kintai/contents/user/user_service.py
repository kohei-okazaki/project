from kintai.models import UserData


def get_user(seq_user_id: int) -> UserData:
    '''
    USER_DATAをSEQ_USER_IDをキーに検索する
    '''
    return UserData.objects.get(seq_user_id=seq_user_id)


def get_user_by_id_and_password(seq_user_id: int, password: str) -> list:
    '''
    USER_DATAをSEQ_USER_IDとパスワードをキーに検索する
    '''
    return UserData.objects.filter(seq_user_id=seq_user_id, password=password)
