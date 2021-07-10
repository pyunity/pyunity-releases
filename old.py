import urllib
import wget, os, glob

if os.path.exists("0.7.0"):
    for file in glob.glob(os.path.join("0.7.0", "pyunity*.whl")):
        os.remove(file)
else:
    os.mkdir("0.7.0")

for platform, plat_name in zip(
        ["Visual%20Studio%202019", "Visual%20Studio%202019", "Ubuntu", "macos"],
        ["win_amd64", "win32", "linux_x86_64", "macosx_10_15_x86_64"]):
    for version, name in zip(
            ["3.6", "3.7", "3.8", "3.9"],
            ["cp36-cp36m-", "cp37-cp37m-", "cp38-cp38-", "cp39-cp39-"]):
        venv = "../../venv" + version
        windows_location = "C:\\Python" + version[::2] + "-x64\\python"
        windows_location2 = "C:\\Python" + version[::2] + "\\python"
        job_name = "Image:%20" + platform + ";%20Environment:%20version=" + version + ",%20venv=" + venv + ",%20windows_location=" + windows_location + ",%20windows_location2=" + windows_location2
        #print("https://ci.appveyor.com/api/projects/pyunity/pyunity/artifacts/dist/pyunity-0.7.0-" + name + plat_name + ".whl?job=" + job_name)
        try:
            wget.download("https://ci.appveyor.com/api/projects/pyunity/pyunity/artifacts/dist/pyunity-0.7.0-" + name + plat_name + ".whl?job=" + job_name, "0.7.0/pyunity-0.7.0-" + name + plat_name + ".whl")
        except urllib.error.HTTPError:
            print("Couldnt download pyunity-0.7.0-" + name + plat_name + ".whl", end="")
        print()

linux_builds = glob.glob("0.7.0/pyunity-0.7.0*linux*.whl")
for file in linux_builds:
    os.rename(file, file.replace("linux", "manylinux1"))
