# test_all_epoch.py

epoch1~200のテストを実行する。logはGCN_Classification_with_CAM/work_dir/tmp/log.txtに出力される 。guava上で実行すること前提であるため、他のマシンに移行するのは面倒くさいかも。


# analyze_log.py
GCN_Classificationのテストを実行した際に出力されるlog.txtから、ほしい部分だけを抽出しanalyzed_log.txtに書き込む
