import os
files = os.listdir("ClutteredFolder")
i = 1
for file in files:
    if file.endswith(".png"):
        print(file)
        os.rename(f"ClutteredFolder/{file}",f"ClutteredFolder/{i}.png")
        i = i + 1