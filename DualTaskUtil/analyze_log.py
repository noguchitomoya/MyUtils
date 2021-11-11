import re


log_path = 'log.txt'
analyzed_log_path='analyzed_log.txt'

new_f = open(analyzed_log_path, 'w')
with open(log_path) as f:
    for line in f:

        if ('Top1' in line) or ('Weights: ./result/epoch' in line) or ('mean_loss:' in line):
            line = re.sub(r"\[.+\]", '', line).lstrip()  # 戦闘からタイムスタンプと空白文字を削除する
            new_f.write(line)

new_f.close()
