import os
dirs = os.listdir("./raw_data")
for path in dirs:
    try:
        files = [f for f in os.listdir(os.path.join("raw_data", path)) if os.path.isfile(os.path.join("raw_data", path, f))]
        cmd = "cp '{0}' '../backoffice/extensions/static/txt'".format(os.path.join("raw_data", path, files[0]))
        os.system(cmd)
    except Exception as wrong:
        print(wrong)
