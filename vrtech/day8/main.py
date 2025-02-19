import defaults
import platform

# print(defaults.JENKINS_URL)

print(defaults.add(4, 5))

print(platform.machine())
print(platform.architecture())
print(platform.uname().node)
