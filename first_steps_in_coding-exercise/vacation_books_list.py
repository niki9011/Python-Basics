number_of_page = int(input())
page_for_hourse = int(input())
number_of_days = int(input())

all_time = ( number_of_page / page_for_hourse )
need_time_for_day =  round ( all_time / number_of_days )

print(need_time_for_day)