from kintai.contents.user.user_data_dto import UserDataDto
from kintai.models import UserData


def get_user_data_dto(seq_user_id: int) -> UserDataDto:
    """USER_DATAをSEQ_USER_IDをキーに検索する

    Args:
        seq_user_id (int): ユーザID

    Returns:
        UserDataDto: ユーザ情報Dto
    """

    user_data: UserData = UserData.objects.get(seq_user_id=seq_user_id)
    dto: UserDataDto = to_dto(user_data)

    return dto


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
        dto: UserDataDto = to_dto(user_data)
        dto_list.append(dto)

    return dto_list


def to_user_data(dto: UserDataDto) -> UserData:
    """ユーザ情報Dtoをユーザ情報に変換する

    Args:
        dto (UserDataDto): ユーザ情報Dto

    Returns:
        UserData: ユーザ情報
    """

    user_data: UserData = UserData()

    user_data.seq_user_id = dto.seq_user_id
    user_data.password = dto.password
    user_data.company_cd = dto.company_cd
    user_data.division_cd = dto.division_cd
    user_data.del_flg = dto.del_flg
    user_data.reg_date = dto.reg_date
    user_data.update_date = dto.update_date

    return user_data


def to_dto(user_data: UserData) -> UserDataDto:
    """ユーザ情報をユーザ情報Dtoに変換する

    Args:
        user_data (UserData): ユーザ情報

    Returns:
        UserDataDto: ユーザ情報Dto
    """

    dto: UserDataDto = UserDataDto()

    dto.seq_user_id = user_data.seq_user_id
    dto.password = user_data.password
    dto.company_cd = user_data.company_cd
    dto.division_cd = user_data.division_cd
    dto.del_flg = user_data.del_flg
    dto.reg_date = user_data.reg_date
    dto.update_date = user_data.update_date

    return dto


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


def update_user(dto: UserDataDto) -> bool:
    """ユーザ情報更新処理

    Args:
        dto (UserDataDto): ユーザ情報Dto

    Returns:
        bool: 登録処理成功の場合True、それ以外の場合False
    """

    user_data: UserData = to_user_data(dto)

    user_data.save()

    return True
