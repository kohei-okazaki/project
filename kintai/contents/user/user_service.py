from kintai.contents.user.user_data_dto import UserDataDto
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


def regist_user(dto: UserDataDto) -> bool:
    """ユーザ情報登録処理

    Args:
        dto (UserDataDto): ユーザ情報Dto

    Returns:
        bool: 登録処理成功の場合True、それ以外の場合False
    """

    user_date: UserData = UserData(
        password=dto.password,
        company_cd=dto.company_cd,
        division_cd=dto.division_cd,
    )

    user_date.save()

    return True
