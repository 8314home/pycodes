import time

print("local time value:{}".format(time.localtime()))
start_time =time.time()


print("------------challenge---------------")
print("time clock info: {}".format(time.get_clock_info('clock')))
print("time time.time() info: {}".format(time.get_clock_info('time')))
print("time time.monotonic info: {}".format(time.get_clock_info('monotonic')))
print("time perf_counter info: {}".format(time.get_clock_info('perf_counter')))



print("The epoch on this system starts at " + time.strftime('%c', time.gmtime(0)))

print("The current timezone is {0} with an offset of {1}".format(time.tzname[0], time.timezone))

if time.daylight != 0:
    print("\tDaylight Saving Time (DST) is defined for this location")
    print("\tThe DST timezone name is " + time.tzname[1])

print("Local time is " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
print("UTC is " + time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))
import datetime

print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())

end_time =time.time()
print("Started at " + time.strftime("%X", time.localtime(start_time)))
print("Ended at " + time.strftime("%X", time.localtime(end_time)))
print("Total run time {}".format(end_time - start_time))