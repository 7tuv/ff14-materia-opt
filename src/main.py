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

	dataset = get_dataset_brd_il600()
	# dataset = get_dataset_brd_il530()
	# dataset = get_dataset_whm_il530()
	# dataset = get_dataset_brd_il510()

	# choice_eq = [0, 1, 0, 0, 0, 1, 1,	#  6.0
	#			0, 1, 1, 0, 0]			#  brd最適装備(計算) https://etro.gg/gearset/865fc886-994f-4c28-8fc1-4379f160a916
	# dataset = get_selected_dataset(dataset, choice_eq)

	### 準備 ###
	obj = MateriaOpt(dataset)

	obj.set_rate_dmgsrc(aa=0.1259, dot=0.1272, ss=0.4175)	# BRD

	#### GCD 条件 ####	http://allaganstudies.akhmorning.com/stats/speed/
	# obj.set_ss_condition(26)	# 制約条件: GCDが少なくとも 2.49 以下
	# obj.set_ss_condition(127)	# 制約条件: GCDが少なくとも 2.48 以下
	# obj.set_ss_condition(432)	# 制約条件: GCDが少なくとも 2.45 以下
	# obj.set_ss_condition(534)	# 制約条件: GCDが少なくとも 2.44 以下
	# obj.set_ss_condition(635)	# 制約条件: GCDが少なくとも 2.43 以下
	# obj.set_ss_condition(737)	# 制約条件: GCDが少なくとも 2.42 以下
	# obj.set_ss_condition(838)	# 制約条件: GCDが少なくとも 2.41 以下
	# obj.set_ss_condition(940)	# 制約条件: GCDが少なくとも 2.40 以下
	# obj.set_ss_condition(1041)	# 制約条件: GCDが少なくとも 2.39 以下
	# obj.set_ss_condition(1143)	# 制約条件: GCDが少なくとも 2.39 以下
	# obj.set_ss_condition(1244)	# 制約条件: GCDが少なくとも 2.38 以下

	#### 信仰 条件 ####
	# obj.set_pi_condition(462)	# 制約条件: 信仰が少なくとも X 以上
	# obj.set_pi_condition(1000)	# 制約条件: 信仰が少なくとも X 以上

	#### 飯を含めたうえでの最適値を計算 ####
	obj.set_meshi(ch=90, ss=54)	# 6.0パンプキンラタトゥイユHQ◎
	# obj.set_meshi(ch=54, dt=90)	# 6.0パンプキンポタージュHQ
	# obj.set_meshi(ch=108, dt=179)	# 5.4スモークチキンHQ
	# obj.set_meshi(ch=179, ss=108)	# 5.4チキンフェットゥチーネHQ
	# obj.set_meshi(dt=108, dh=179)	# 5.4ピッツァHQ
	# obj.set_meshi(ch=101, dt=168)	# 5.2 高地風挽肉のキャベツ巻きHQ

	obj.set_calcset(version="6.0")
	# obj.set_calcset(version="5.5")

	#### 最適化問題を解く ####
	obj.calc_damage()
