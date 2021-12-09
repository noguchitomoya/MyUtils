import subprocess
import os
import re

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

# モデルを指定している、test.yamlの場所
test_yaml_path = "/home/noguchi/WorkDir/GCN_Classification_with_CAM/st-gcn-master/config/st_gcn/misasagikai/test.yaml"


for epo in range(1,76):#モデルの数分実行する
    print("start     evaluating epoch is ----------------------------------------", epo)
    os.chdir('/home/noguchi/WorkDir/MyUtils')
    # 読み込み
    with open(test_yaml_path) as reader:
        content = reader.read()

    # 置換
    #実行したいepochのモデルに、文字列を置換する
    content = re.sub('epoch\d+_model', 'epoch'+str(epo)+'_model', content)


    # 保存
    with open(test_yaml_path, 'w') as writer:
        writer.write(content)

    #実行したいプロジェクトにカレントディレクトリを変更する
    os.chdir('/home/noguchi/WorkDir/GCN_Classification_with_CAM/')

    #テストを実行する。　参考：https://ohke.hateblo.jp/entry/2020/01/18/131500
    subprocess.run(["/home/noguchi/anaconda3/envs/test/bin/python", "-u",
                    "/home/noguchi/WorkDir/GCN_Classification_with_CAM/st-gcn-master/main.py", "recognition", "-c",
                    "/home/noguchi/WorkDir/GCN_Classification_with_CAM/st-gcn-master/config/st_gcn/misasagikai/test.yaml"])

    print("end     evaluated epoch is ----------------------------------------", epo)

