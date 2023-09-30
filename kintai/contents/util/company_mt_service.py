from kintai.models import CompanyMt


def get_company_mt_list(orderby: str):
    if (orderby == None or  orderby == ""):
        return CompanyMt.objects.filter(
            del_flg=False)
    return CompanyMt.objects.filter(
            del_flg=False).order_by(orderby)