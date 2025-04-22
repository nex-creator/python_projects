# def format_name(f_name, l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"
#
#
# print(format_name("AnGEla", "YU"))
def is_leap_year(year):
    if year % 100 == 0:
        if year % 400 == 0:
            if year % 4 == 0:
                return True
            else:
                return False
        else:
            return False
    elif year % 4== 0:
        return True
    else:
        return False
print(is_leap_year(2100))
