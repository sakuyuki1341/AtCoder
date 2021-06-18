#!/bin/sh

# $1=cource name
# $2=number

check_files () {
	# 引数が指定されているか確認
	if [ -z "$1" ] || [ -z "$2" ]
	then
		# 何も指定していない場合終了
		echo "Usage: ${0} [corce name] [number]"
		exit
	fi

	# cource nameを大文字に変換
	dir_l=`echo $1 | tr '[a-z]' '[A-Z]'`
	dir_s=`echo $1 | tr '[A-Z]' '[a-z]'`
	# numberを0付き3桁に変換
	number=`printf %03d $2`

#正常に変換されたか確認	
#	echo ${dir}
#	echo ${number}

	# 指定されたコンテスト名のディレクトリ生成
	if [ ! -d ${dir_l} ]
	then
		mkdir ${dir_l}
	fi

	# 指定されたnumberのフォルダがあれば終了
	if [ -d ${dir_l}/"${dir_s}${number}" ]
	then
		exit
	else
		mkdir ${dir_l}/"${dir_s}${number}"
	fi

	# ABCコンテストについての特殊割当
	if [ ${dir_l} = "ABC" ]; then
		if [[ ${2} -lt 126 ]]; then
			L=(A B C D)
		else
			L=(A B C D E F)
		fi

	# ARCコンテストについての特殊割当
	elif [ ${dir_l} = "ARC" ]; then
		if [[ ${number} -lt 58 ]]; then
			L=(A B C D)
		elif [[ ${number} -lt 104 ]]; then
			L=(C D E F)
		else
			L=(A B C D E F)
		fi

	elif [ ${dir_l} = "AGC" ]; then
		L=(A B C D E F)

	else
		exit
	fi

	for var in ${L[@]}
	do
		touch "${dir_l}/${dir_s}${number}/${dir_s}${number}_${var}.py"
	done
}

check_files $1 $2