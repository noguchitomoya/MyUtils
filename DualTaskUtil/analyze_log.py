import re

#入出力ファイルのpth
log_path = 'log.txt'
analyzed_log_path='analyzed_log.txt'

output_file = open(analyzed_log_path, 'w')
with open(log_path) as f:
    for line in f:
        if ('Top1' in line) or ('Weights: ./result/data_04/epoch' in line) or ('mean_loss:' in line):
            line = re.sub(r"\[.+\]", '', line).lstrip()  # 戦闘からタイムスタンプと空白文字を削除する
            output_file.write(line)#文字列の書き込み

output_file.close()
