from kintai.models import DivisionMt


def get_division_mt_dto_list(orderby: str) -> list:
    """_summary_

    Args:
        orderby (str): ORDER BY句

    Returns:
        list: 部署マスタDtoのリスト
    """

    mt_list: list = list()
    if (orderby == None or orderby == ""):
        mt_list = DivisionMt.objects.filter(
            del_flg=False)
    else:
        mt_list = DivisionMt.objects.filter(
            del_flg=False).order_by(orderby)

    dto_list: list = list()

    for mt in mt_list:

        dto: DivisionMt = DivisionMt()
        dto.division_cd = mt.division_cd
        dto.name = mt.name
        dto.del_flg = mt.del_flg
        dto.reg_date = mt.reg_date
        dto.update_date = mt.update_date

        dto_list.append(dto)
    return dto_list