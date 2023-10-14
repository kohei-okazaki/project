from kintai.contents.util.dto import OntimeMtDto
from kintai.models import OntimeMt


def get_dto_list(orderby: str) -> list:
    """定時マスタDtoのリストを返す

    Args:
        orderby (str): ORDER BY句

    Returns:
        list: 定時マスタDtoのリスト
    """
    mt_list: list = list()
    if orderby is None or orderby == "":
        mt_list = OntimeMt.objects.filter(
            del_flg=False)
    else:
        mt_list = OntimeMt.objects.filter(
            del_flg=False).order_by(orderby)

    dto_list: list = list(OntimeMtDto(mt) for mt in mt_list)

    return dto_list
