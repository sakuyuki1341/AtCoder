#!/bin/sh

# $1=cource name
# $2=number

make_files () {
	# 引数が指定されているか確認
	if [ -z "$1" ] || [ -z "$2" ]
	then
		# 何も指定していない場合終了
		echo "「コンテスト名」->「コンテスト番号」の順で指定してください"
		echo "指定できるコンテスト名は以下の通り"
		echo "\"abc\""
		exit
	fi
}

make_files $1 $2