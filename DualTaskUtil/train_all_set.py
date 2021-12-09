import subprocess
import os
import re

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

# モデルを指定している、train.yamlの場所
test_yaml_path = "/home/noguchi/WorkDir/STA_GCN_Classification/st-gcn-master/config/st_gcn/misasagikai/train.yaml"


for data_set_n in range(1,5):#モデルの数分実行する
    print("start     training data set  is ----------------------------------------", data_set_n)
    os.chdir('/home/noguchi/WorkDir/MyUtils')
    # 読み込み
    with open(test_yaml_path) as reader:
        content = reader.read()

    # 置換
    #実行したいepochのモデルに、文字列を置換する
    content = re.sub('data_0\d', 'data_0'+str(data_set_n), content)
    content = re.sub('label_0\d', 'label_0' + str(data_set_n), content)


    # 保存
    with open(test_yaml_path, 'w') as writer:
        writer.write(content)

    #実行したいプロジェクトにカレントディレクトリを変更する
    os.chdir('/home/noguchi/WorkDir/STA_GCN_Classification/')

    #テストを実行する。　参考：https://ohke.hateblo.jp/entry/2020/01/18/131500
    subprocess.run(["/home/noguchi/anaconda3/envs/test/bin/python", "-u",
                    "/home/noguchi/WorkDir/STA_GCN_Classification/st-gcn-master/main.py", "recognition", "-c",
                    "/home/noguchi/WorkDir/STA_GCN_Classification/st-gcn-master/config/st_gcn/misasagikai/train.yaml"])

    print("end     training  data-set is ----------------------------------------", data_set_n)

