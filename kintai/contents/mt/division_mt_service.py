from kintai.contents.util.dto import DivisionMtDto
from kintai.models import DivisionMt


def get_dto_list(orderby: str) -> list:
    """部署マスタDtoのリストを返す

    Args:
        orderby (str): ORDER BY句

    Returns:
        list: 部署マスタDtoのリスト
    """

    mt_list: list = list()
    if orderby is None or orderby == "":
        mt_list = DivisionMt.objects.filter(
            del_flg=False)
    else:
        mt_list = DivisionMt.objects.filter(
            del_flg=False).order_by(orderby)

    dto_list: list = list(DivisionMtDto(mt) for mt in mt_list)

    return dto_list
