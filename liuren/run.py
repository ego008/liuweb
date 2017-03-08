# -*- coding: utf-8 -*- 
from generate_result import generate_result
from output_results import output_results
from datetime import datetime, timedelta
from earthbranch import earthbranch
from gettodayse import todayse
import sys

reload(sys)
sys.setdefaultencoding('utf8')
def run(fortell_time_str, fortell_zone_str, fortell_index_str ):
	fortell_time = datetime.strptime(fortell_time_str, '%Y-%m-%d %H:%M:%S')
	fortell_zone = int(fortell_zone_str)
	fortell_index = int(fortell_index_str)
	gt = todayse(fortell_time, fortell_zone)
	if fortell_index != None:
		gt.set_fortell_hour(fortell_index)
	tmptoday = gt.get_day()
	tmptodayst = tmptoday[0:3]
	tmptodayeb = tmptoday[3:]
	tmphour = gt.get_hour()
	tmphoureb = tmphour[3:]
	tmpgeneral = gt.get_month_general()
	'''
	print "tmptoday "+tmptoday
	print "tmptodayst "+tmptodayst
	print "tmptodayeb "+tmptodayeb
	print "tmphour"+tmphour
	print "tmphoureb "+tmphoureb	
	'''
	#fortell_time_str = fortell_time.strftime('%Y-%m-%d %H:%M:%S')
	tmpline = "<p>起课时间："+	fortell_time_str+"</p>"
	tmpline = tmpline+"<p>占时: "+gt.get_year()+"年 "+gt.get_month()+"月 "+tmptoday+"日 "+tmphour+ "时 " + " 月将"+ tmpgeneral+"</p>"
	
	gs = generate_result(tmptodayst,tmptodayeb,tmpgeneral,tmphoureb)
	gs.generate_skyplate()
	gs.generate_four()
	gs.generate_skygeneral()
	gs.generate_trishift()	
	output11 = output_results(gs.st, gs.eb, gs.month_general, gs.foretell_hour, gs.skyplate, gs.skygeneral, gs.bottom_four, gs.upper_four, gs.triline)
	return tmpline+output11.output()
