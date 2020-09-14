#!/usr/bin/env python3
# coding=utf-8

import sys

from calc_damage import MateriaOpt
from dataset import *

# equips = ["arm", "head", "body", "hands", "waist", "legs", "feet",
# 		"earrings", "necklace", "bracelets", "ring1", "ring2"]

def get_selected_dataset(dataset, choice_eq):
	rtn = {}
	for i in zip(dataset.keys(), choice_eq):
		rtn[i[0]] = (dataset[i[0]][i[1]],)
	return rtn


if __name__ == "__main__":

	######## BRD ########
	choice_eq = [0, 0, 0, 1, 1, 1, 0,
				0, 0, 1, 0, 0]			#  ***brd最適装備*** 1.35058◎

	# choice_eq = [0, 1, 1, 0, 0, 0, 1,
	# 			1, 1, 0, 0, 0]			#  ***brd最弱装備*** 1.33031×××

	# choice_eq = [0, 0, 0, 1, 1, 1, 1,
	# 			1, 0, 1, 0, 0]			# feetクリスタリウム 1.34890×, 周辺max: 1.34950×

	# choice_eq = [0, 0, 0, 1, 1, 1, 0,
	# 			1, 1, 1, 0, 0]			# neckクリスタリウム,feetコーラス 1.34850× 周辺max 1.34907×

	# choice_eq = [0, 0, 0, 1, 1, 1, 1,
	# 			1, 1, 1, 0, 0]			# feetクリスタリウム,neckクリスタリウム 1.34794×, 周辺max: 1.34904 ×

	# choice_eq = [0, 0, 0, 0, 0, 0, 0,	# 全部エデンコーラス
	# 			0, 0, 0, 0, 0]

	# choice_eq = [0, 1, 1, 1, 1, 1, 1,	# 全部クリスタリウム
	# 			1, 1, 1, 0, 0]


	####### WHM ########
	# choice_eq = [0, 0, 1, 0, 1, 0, 1,
	# 			0, 1, 0, 0, 0]			# CH優先		 1.31658

	# choice_eq = [0, 1, 0, 1, 0, 1, 0,
	# 			1, 0, 1, 0, 0]			#


	######## DRK ########
	# choice_eq = [0, 0, 1, 0, 0, 0, 1,	#	1.34167〇(2.43)		2.42: 1.34261◎
	# 			1, 0, 1, 0, 0]

	# choice_eq = [0, 1, 1, 0, 0, 0, 1,	#	1.34224〇	2.43: 1.34424〇	2.42: 1.34228〇
	# 			1, 0, 1, 0, 0]

	# choice_eq = [0, 0, 0, 0, 0, 0, 0,	# 全部エデンコーラス
	# 			0, 0, 0, 0, 0]

	# choice_eq = [0, 1, 1, 1, 1, 1, 1,	# 全部クリスタリウム
	# 			1, 1, 1, 0, 0]


	######## SMN ########
	# choice_eq = [0, 1, 0, 0, 1, 1, 0,	#  ***smn最適装備*** 1.35161◎
	# 			1, 0, 0, 0, 0]


	dataset = get_dataset_brd_il500()	#	http://ff14a.net/equip-520-brd
	# dataset = get_dataset_brd_il480()
	# dataset = get_dataset_whm_il500()
	# dataset = get_dataset_drk_il500()	#	http://ff14a.net/equip-520-drk
	# dataset = get_dataset_smn_il500() #	http://ff14a.net/equip-520-smn
	###	https://game8.jp/ff14/291095	###

	dataset = get_selected_dataset(dataset, choice_eq)


	### 準備 ###
	obj = MateriaOpt(dataset)

	obj.set_rate_dmgsrc(aa=0.1259, dot=0.1272, ss=0.4175)	# BRD
	# obj.set_rate_dmgsrc(aa=0.0, dot=0.1562, ss=0.6799)	# WHM
	# obj.set_rate_dmgsrc(aa=0.1232, dot=0.0, ss=0.6855)	# DRK	https://www.fflogs.com/reports/mYhw7TdrxF9jQWyB#fight=25&type=damage-done
	# obj.set_rate_dmgsrc(aa=0.0, dot=0.15, ss=0.6)			# SMN

	#### GCD 条件 ####	http://allaganstudies.akhmorning.com/stats/speed/
	obj.set_ss_condition(127)	# 制約条件: GCDが少なくとも 2.48 以下
	# obj.set_ss_condition(432)	# 制約条件: GCDが少なくとも 2.45 以下
	# obj.set_ss_condition(534)	# 制約条件: GCDが少なくとも 2.44 以下
	# obj.set_ss_condition(635)	# 制約条件: GCDが少なくとも 2.43 以下
	# obj.set_ss_condition(737)	# 制約条件: GCDが少なくとも 2.42 以下
	# obj.set_ss_condition(838)	# 制約条件: GCDが少なくとも 2.41 以下
	# obj.set_ss_condition(940)	# 制約条件: GCDが少なくとも 2.40 以下
	# obj.set_ss_condition(1041)	# 制約条件: GCDが少なくとも 2.39 以下
	# obj.set_ss_condition(1143)	# 制約条件: GCDが少なくとも 2.39 以下
	# obj.set_ss_condition(1244)	# 制約条件: GCDが少なくとも 2.38 以下

	#### 信仰 条件 #### 作成中
	# obj.set_pi_condition(462)	# 制約条件: 信仰が少なくとも 0 以上
	# obj.set_pi_condition(1000)	# 制約条件: 信仰が少なくとも 0 以上


	#### 最適化問題を解く ####
	obj.calc_damage()

	# BRD
	# obj.show_eff(*obj.calc_exact_dmg_multiplier(2322, 3488, 1439, 180))			#	1.34976
	# obj.show_eff(*obj.calc_exact_dmg_multiplier(2322+24, 3488, 1439-60, 180))
	# obj.show_eff(*obj.calc_exact_dmg_multiplier(2322-60, 3488, 1439+60, 180))	#	1.35051◎

	# [print(i, obj.show_eff(*obj.calc_exact_dmg_multiplier(2322-180, 3488-i, 1439+180+i, 180))) for i in range(0, 600, 60)]

	#	BRD
	# obj.show_eff(*obj.calc_exact_dmg_multiplier(2653, 3400, 1228, 148))			#	1.35058
	# [print(i, obj.show_eff(*obj.calc_exact_dmg_multiplier(2653-i, 3400, 1228+i, 148))) for i in range(0, 360, 60)]


	#	DRK
	# obj.show_eff(*obj.calc_exact_dmg_multiplier(1140, 3333, 2034, 774, 148, 0))			#	1.34261◎
	# [print(i, obj.show_eff(*obj.calc_exact_dmg_multiplier(1140+i, 3333-i, 2034, 774, 148, 0))) for i in [0,60,120,180,240]]
	

	#	SMN
	# obj.show_eff(*obj.calc_exact_dmg_multiplier(2697, 3400, 1332, 0, 0, 0))			#	1.35161
	# obj.show_eff(*obj.calc_exact_dmg_multiplier(2697+60*4, 3400, 1332-60*4, 0, 0, 0))	#	1.35209
	# [print(i, obj.show_eff(*obj.calc_exact_dmg_multiplier(2697+i, 3400-60, 1332-i+60, 0, 0, 0))) for i in range(-420, 420, 60)]

