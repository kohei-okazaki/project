from kintai.contents.util.dto import CompanyMtDto
from kintai.models import CompanyMt


def get_dto_list(orderby: str) -> list:
    """企業マスタDtoのリストを返す

    Args:
        orderby (str): ORDER BY句

    Returns:
        list: 企業マスタDtoのリスト
    """

    mt_list: list = list()
    if (orderby == None or orderby == ""):
        mt_list = CompanyMt.objects.filter(
            del_flg=False)
    else:
        mt_list = CompanyMt.objects.filter(
            del_flg=False).order_by(orderby)

    dto_list: list = list(CompanyMtDto(mt) for mt in mt_list)

    return dto_list
