create_table = """create table rank(id uuid primary key,name varchar(100), start_dt timestamp, end_dt timestamp, attemps integer);"""
select_attemps_top5 = """select name, attemps from rank order by attemps desc limit 5;"""
select_time_top5 = """select name, min(end_dt - start_dt) as takes_time from rank group by name order by takes_time limit 5;"""
