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


def get_dto(company_cd: str, division_cd: str) -> OntimeMtDto:
    """企業コードと部署コードより、定時マスタDtoを返す

    Args:
        company_cd (str): 企業コード
        division_cd (str): 部署コード

    Returns:
        OntimeMtDto: 定時マスタDto
    """
    # 有効な定時マスタを取得
    mt_list: list = OntimeMt.objects.filter(
        del_flg=False, company_cd=company_cd, division_cd=division_cd)

    dto_list: list = list(OntimeMtDto(mt) for mt in mt_list)

    if len(dto_list) > 0:
        return dto_list[0]

    return None
