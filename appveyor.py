import wget, os, glob, shutil

if os.path.exists("0.3.0"): shutil.rmtree("0.3.0")
os.mkdir("0.3.0")

for platform, plat_name in zip(
        ["Visual%20Studio%202019", "Ubuntu", "macos"],
        ["win_amd64", "linux_x86_64", "macosx_10_15_x86_64"]):
    for version, name in zip(
            ["3.6", "3.7", "3.8", "3.9"],
            ["cp36-cp36m-", "cp37-cp37m-", "cp38-cp38-", "cp39-cp39-"]):
        venv = "../../venv" + version
        windows_location = "C:\\Python" + version[::2] + "-x64\\python"
        job_name = "Image:%20" + platform + ";%20Environment:%20version=" + version + ",%20venv=" + venv + ",%20windows_location=" + windows_location
        #print("https://ci.appveyor.com/api/projects/rayzchen/pyunity/artifacts/dist/pyunity-0.3.0-" + name + plat_name + ".whl?job=" + job_name)
        wget.download("https://ci.appveyor.com/api/projects/rayzchen/pyunity/artifacts/dist/pyunity-0.3.0-" + name + plat_name + ".whl?job=" + job_name, "0.3.0/pyunity-0.3.0-" + name + plat_name + ".whl")
        print()

linux_builds = glob.glob("0.3.0/pyunity-0.3.0*linux*.whl")
for file in linux_builds:
    os.rename(file, file.replace("linux", "manylinux1"))
