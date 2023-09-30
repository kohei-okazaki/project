from kintai.models import DivisionMt


def get_division_mt_list(orderby: str):
    if (orderby == None or  orderby == ""):
        return DivisionMt.objects.filter(
            del_flg=False)
    return DivisionMt.objects.filter(
            del_flg=False).order_by(orderby)