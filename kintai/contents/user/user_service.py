from kintai.contents.user.user_data_dto import UserDataDto
from kintai.models import UserData


def get_user(seq_user_id: int) -> UserData:
    '''
    USER_DATAをSEQ_USER_IDをキーに検索する
    '''
    return UserData.objects.get(seq_user_id=seq_user_id)


def get_user_by_id_and_password(dto: UserDataDto) -> list:
    """USER_DATAをSEQ_USER_IDとパスワードをキーに検索する

    Args:
        dto (UserDataDto): ユーザ情報Dto

    Returns:
        list: ユーザ情報Dtoリスト
    """

    user_data_list: list = UserData.objects.filter(
        seq_user_id=dto.seq_user_id, password=dto.password)
    dto_list: list = list()

    for user_data in user_data_list:

        dto: UserDataDto = UserDataDto()
        dto.seq_user_id = user_data.seq_user_id
        dto.password = user_data.password
        dto.company_cd = user_data.company_cd
        dto.division_cd = user_data.division_cd
        dto.del_flg = user_data.del_flg
        dto.reg_date = user_data.reg_date
        dto.update_date = user_data.update_date

        dto_list.append(dto)

    return dto_list


def regist_user(dto: UserDataDto) -> bool:
    """ユーザ情報登録処理

    Args:
        dto (UserDataDto): ユーザ情報Dto

    Returns:
        bool: 登録処理成功の場合True、それ以外の場合False
    """

    user_data: UserData = UserData(
        password=dto.password,
        company_cd=dto.company_cd,
        division_cd=dto.division_cd,
    )

    user_data.save()

    return True
