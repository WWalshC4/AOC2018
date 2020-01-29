import re

with open ('./day4_input.txt') as f:
	inputData = f.read ()

times = inputData.splitlines ()

list.sort (times)

guards = {}

re_guard = re.compile (r"\[(\d+)\-(\d+)\-(\d+) (\d+)\:(\d+)\] Guard \#(\d+) begins shift")
re_asleep = re.compile (r"\[(\d+)\-(\d+)\-(\d+) (\d+)\:(\d+)\] falls asleep")
re_awake = re.compile (r"\[(\d+)\-(\d+)\-(\d+) (\d+)\:(\d+)\] wakes up")

onshiftGuard = 0
lastSleepTime = 0

for time in times:
	guard = re_guard.match (time)
	asleep = re_asleep.match (time)
	awake = re_awake.match (time)

	if (guard):
		year, month, day, hour, minute, guardId = guard.groups ()

		onshiftGuard = int (guardId)
		if (onshiftGuard in guards):
			pass
		else:
			guards [onshiftGuard] = {
				'totalMins' : 0,
			}

	if (asleep):
		year, month, day, hour, minute = asleep.groups ()

		minute = int (minute)
		lastSleepTime = minute


	if (awake):
		year, month, day, hour, minute = awake.groups ()

		minute = int (minute)
		lastWakeTime = minute

		for thisMinute in range (lastSleepTime, lastWakeTime):
			if (thisMinute in guards [onshiftGuard]):
				guards [onshiftGuard] [thisMinute] += 1
			else:
				guards [onshiftGuard] [thisMinute] = 1

			guards [onshiftGuard] ['totalMins'] += 1

longestGuard = 0
longestGuardTime = 0

for guardId in guards:
	if (guards [guardId] ['totalMins'] > longestGuardTime):
		longestGuardTime = guards [guardId] ['totalMins']
		longestGuard = guardId

longestMin = 0
longestMinCount = 0

for thisMinute in guards [longestGuard]:
	if (thisMinute == 'totalMins'):
		pass
	else:
		if (guards [longestGuard] [thisMinute] > longestMinCount):
			longestMinCount = guards [longestGuard] [thisMinute]
			longestMin = thisMinute

print (longestGuard * longestMin) #	125444