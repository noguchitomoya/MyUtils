import subprocess
import os
import re

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

# モデルを指定している、test.yamlの場所
test_yaml_path = "/home/noguchi/WorkDir/GCN_Classification_with_CAM/st-gcn-master/config/st_gcn/misasagikai/test.yaml"


for epo in range(1,200):
    print("start     evaluating epoch is ----------------------------------------", epo)
    os.chdir('/home/noguchi/WorkDir/MyUtils')
    # 読み込み
    with open(test_yaml_path) as reader:
        content = reader.read()

    # 置換

    content = re.sub('epoch\d+_model', 'epoch'+str(epo)+'_model', content)


    # 書き出し
    with open(test_yaml_path, 'w') as writer:
        writer.write(content)

    os.chdir('/home/noguchi/WorkDir/GCN_Classification_with_CAM/')

    subprocess.run(["/home/noguchi/anaconda3/envs/test/bin/python", "-u",
                    "/home/noguchi/WorkDir/GCN_Classification_with_CAM/st-gcn-master/main.py", "recognition", "-c",
                    "/home/noguchi/WorkDir/GCN_Classification_with_CAM/st-gcn-master/config/st_gcn/misasagikai/test.yaml"])

    print("end     evaluated epoch is ----------------------------------------", epo)

