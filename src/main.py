import sys

from calc_damage import MateriaOpt

equips = ["arm", "head", "body", "hands", "waist", "legs", "feet",
		"earrings", "necklace", "bracelets", "ring1", "ring2"]

def get_dataset_brd_il500():
	# コーラス(上) vs クリスタリウム(下)
	# 'vt', 'vt_lim', 'dh', 'ch', 'dt', 'ss', 'tn', 'pi', 'subst_lm', 'ex_m', 'mg_m'
	dataset = {}
	dataset["arm"] = (
		(707, 707, 349, 498, 0, 0, 0, 0, 498, 2, 0),
		)
				
	dataset["head"] = (
		(391, 391, 0, 281, 197, 0, 0, 0, 281, 2, 0),	#	コーラス
		(391, 391, 281, 0, 0, 197, 0, 0, 281, 2, 0),	#	
		)

	dataset["body"] = (
		(636, 636, 320, 457, 0, 0, 0, 0, 457, 2, 0),	#	コーラス
		(636, 636, 320, 0, 457, 0, 0, 0, 457, 2, 0),	#	
		)
		
	dataset["hands"] = (
		(391, 391, 0, 0, 281, 197, 0, 0, 281, 2, 0),	#	
		(391, 391, 197, 281, 0, 0, 0, 0, 281, 2, 0),	#	クリスタリウム
		)

	dataset["waist"] = (
		(293, 293, 211, 0, 0, 148, 0, 0, 211, 2, 0),	#	
		(293, 293, 0, 148, 211, 0, 0, 0, 211, 2, 0),	#	クリスタリウム
		)

	dataset["legs"] = (
		(636, 636, 457, 0, 320, 0, 0, 0, 457, 2, 0),	#	
		(636, 636, 320, 457, 0, 0, 0, 0, 457, 2, 0),	#	クリスタリウム
		)

	dataset["feet"] = (
		(391, 391, 0, 197, 281, 0, 0, 0, 281, 2, 0),	#	
		(391, 391, 0, 281, 0, 197, 0, 0, 281, 2, 0),	#	クリスタリウム
		)

	dataset["earrings"] = (
		(293, 293, 211, 0, 0, 148, 0, 0, 211, 2, 0),	#	
		(293, 293, 0, 148, 211, 0, 0, 0, 211, 2, 0),	#	クリスタリウム
		)

	dataset["necklace"] = (
		(293, 293, 0, 211, 148, 0, 0, 0, 211, 2, 0),	#	コーラス
		(293, 293, 211, 0, 148, 0, 0, 0, 211, 2, 0),	#	
		)

	dataset["bracelets"] = (
		(293, 293, 0, 0, 211, 148, 0, 0, 211, 2, 0),	#	
		(293, 293, 148, 211, 0, 0, 0, 0, 211, 2, 0),	#	クリスタリウム
		)

	dataset["ring1"] = (
		(293, 293, 148, 211, 0, 0, 0, 0, 211, 2, 0),	#	コーラス
		# (293, 293, 0, 148, 211, 0, 0, 0, 211, 2, 0),	#	クリスタリウム
		)

	dataset["ring2"] = (
		# (293, 293, 148, 211, 0, 0, 0, 0, 211, 2, 0),	#	コーラス
		(293, 293, 0, 148, 211, 0, 0, 0, 211, 2, 0),	#	クリスタリウム
		)

	return dataset


def get_dataset_brd_il480():
	# コーラス(上) vs クリスタリウム(下)
	# 'vt', 'vt_lim', 'dh', 'ch', 'dt', 'ss', 'tn', 'pi', 'subst_lm', 'ex_m', 'mg_m'
	dataset = {}
	dataset["arm"] = (
		(603, 603, 0, 472, 330, 0, 0, 0, 472, 3, 2),
		)
	dataset["head"] = (
		(345, 345, 270, 0, 189, 0, 0, 0, 270, 3, 2),
		)
	dataset["body"] = (
		(560, 560, 307, 438, 0, 0, 0, 0, 438, 3, 2),
		)
	dataset["hands"] = (
		(345, 345, 189, 0, 0, 270, 0, 0, 270, 3, 2),
		)
	dataset["waist"] = (
		(258, 258, 0, 202, 142, 0, 0, 0, 202, 2, 3),
		)
	dataset["legs"] = (
		(560, 560, 438, 0, 307, 0, 0, 0, 438, 3, 2),
		)
	dataset["feet"] = (
		(345, 345, 0, 189, 270, 0, 0, 0, 270, 3, 2),
		)
	dataset["earrings"] = (
		(258, 258, 142, 202, 0, 0, 0, 0, 202, 2, 3),
		)
	dataset["necklace"] = (
		(258, 258, 0, 0, 202, 142, 0, 0, 202, 2, 3),
		)
	dataset["bracelets"] = (
		(258, 258, 0, 202, 0, 142, 0, 0, 202, 2, 3),
		)
	dataset["ring1"] = (
		(258, 258, 202, 0, 142, 0, 0, 0, 202, 2, 3),
		)
	dataset["ring2"] = (
		(258, 258, 202, 0, 142, 0, 0, 0, 202, 2, 3),
		)

	return dataset


def get_dataset_whm_il500():
	# コーラス(上) vs クリスタリウム(下)
	# 'vt', 'vt_lim', 'dh', 'ch', 'dt', 'ss', 'tn', 'pi', 'subst_lm', 'ex_m', 'mg_m'
	dataset = {}
	dataset["arm"] = (
		(637, 637, 0, 0, 349, 0, 0, 498, 498, 2, 0),
		)
				
	dataset["head"] = (
		(352, 352, 0, 281, 197, 0, 0, 0, 281, 2, 0),	#	コーラス
		(352, 352, 0, 197, 0, 0, 0, 281, 281, 2, 0),	#	
		)

	dataset["body"] = (
		(572, 572, 0, 0, 320, 0, 0, 457, 457, 2, 0),	#	
		(572, 572, 0, 320, 457, 0, 0, 0, 457, 2, 0),	#	クリスタリウム
		)
		
	dataset["hands"] = (
		(352, 352, 0, 281, 197, 0, 0, 0, 281, 2, 0),	#	コーラス
		(352, 352, 0, 0, 197, 0, 0, 281, 281, 2, 0),	#	
		)

	dataset["waist"] = (
		(264, 264, 0, 0, 0, 211, 0, 148, 211, 2, 0),	#	
		(264, 264, 0, 211, 148, 0, 0, 0, 211, 2, 0),	#	クリスタリウム
		)

	dataset["legs"] = (
		(572, 572, 0, 320, 0, 457, 0, 0, 457, 2, 0),	#	コーラス
		(572, 572, 0, 0, 320, 0, 0, 457, 457, 2, 0),	#	
		)

	dataset["feet"] = (
		(352, 352, 0, 0, 281, 0, 0, 197, 281, 2, 0),	#	
		(352, 352, 0, 281, 0, 197, 0, 0, 281, 2, 0),	#	クリスタリウム
		)

	dataset["earrings"] = (
		(264, 264, 0, 211, 148, 0, 0, 0, 211, 2, 0),	#	コーラス
		(264, 264, 0, 0, 211, 148, 0, 0, 211, 2, 0),	#	
		)

	dataset["necklace"] = (
		(264, 264, 0, 0, 0, 148, 0, 211, 211, 2, 0),	#	
		(264, 264, 0, 148, 211, 0, 0, 0, 211, 2, 0),	#	クリスタリウム
		)

	dataset["bracelets"] = (
		(264, 264, 0, 211, 148, 0, 0, 0, 211, 2, 0),	#	コーラス
		(264, 264, 0, 148, 0, 0, 0, 211, 211, 2, 0),	#	
		)

	dataset["ring1"] = (
		(264, 264, 0, 211, 0, 148, 0, 0, 211, 2, 0),	#
		# (264, 264, 0, 148, 211, 0, 0, 0, 211, 2, 0),	#
		)

	dataset["ring2"] = (
		# (264, 264, 0, 211, 0, 148, 0, 0, 211, 2, 0),	#
		(264, 264, 0, 148, 211, 0, 0, 0, 211, 2, 0),	#
		)

	return dataset

def get_dataset_drk_il500():
	# コーラス(上) vs クリスタリウム(下)
	# 'vt', 'vt_lim', 'dh', 'ch', 'dt', 'ss', 'tn', 'pi', 'subst_lm', 'ex_m', 'mg_m'
	dataset = {}
	dataset["arm"] = (
		(707, 707, 0, 498, 349, 0, 0, 0, 498, 2, 0),
		)

	dataset["head"] = (
		(391, 391, 0, 0, 281, 197, 0, 0, 281, 2, 0),	#
		(391, 391, 0, 197, 0, 0, 281, 0, 281, 2, 0),	#	クリスタリウム？？
		)

	dataset["body"] = (
		(636, 636, 0, 0, 320, 0, 457, 0, 457, 2, 0),	#	
		(636, 636, 0, 457, 320, 0, 0, 0, 457, 2, 0),	#	クリスタリウム？？
		)

	dataset["hands"] = (
		(391, 391, 0, 197, 281, 0, 0, 0, 281, 2, 0),	#	コーラス？？
		(391, 391, 0, 0, 0, 197, 281, 0, 281, 2, 0),	#	
		)

	dataset["waist"] = (
		(293, 293, 0, 211, 148, 0, 0, 0, 211, 2, 0),	#	コーラス？？
		(293, 293, 0, 0, 0, 148, 211, 0, 211, 2, 0),	#
		)

	dataset["legs"] = (
		(636, 636, 0, 457, 0, 320, 0, 0, 457, 2, 0),	#	コーラス？？
		(636, 636, 0, 0, 457, 0, 320, 0, 457, 2, 0),	#	
		)

	dataset["feet"] = (
		(391, 391, 0, 0, 281, 0, 197, 0, 281, 2, 0),	#	
		(391, 391, 0, 281, 0, 197, 0, 0, 281, 2, 0),	#	クリスタリウム？？
		)

	dataset["earrings"] = (
		(293, 293, 0, 0, 0, 148, 211, 0, 211, 2, 0),	#
		(293, 293, 0, 211, 148, 0, 0, 0, 211, 2, 0),	#	クリスタリウム？？
		)

	dataset["necklace"] = (
		(293, 293, 0, 211, 148, 0, 0, 0, 211, 2, 0),	#	コーラス？？
		(293, 293, 0, 0, 0, 148, 211, 0, 211, 2, 0),	#
		)

	dataset["bracelets"] = (
		(293, 293, 0, 0, 0, 148, 211, 0, 211, 2, 0),	#
		(293, 293, 0, 211, 148, 0, 0, 0, 211, 2, 0),	#	クリスタリウム？？
		)

	dataset["ring1"] = (
		(293, 293, 0, 211, 0, 0, 148, 0, 211, 2, 0),	#
		# (293, 293, 0, 148, 211, 0, 0, 0, 211, 2, 0),	#	
		)

	dataset["ring2"] = (
		# (293, 293, 0, 211, 0, 0, 148, 0, 211, 2, 0),	#
		(293, 293, 0, 148, 211, 0, 0, 0, 211, 2, 0),	#	
		)

	return dataset


def get_dataset_smn_il500():
	# コーラス(上) vs クリスタリウム(下)
	# 'vt', 'vt_lim', 'dh', 'ch', 'dt', 'ss', 'tn', 'pi', 'subst_lm', 'ex_m', 'mg_m'
	dataset = {}
	dataset["arm"] = (
		(637, 637, 349, 498, 0, 0, 0, 0, 498, 2, 0),
		)

	dataset["head"] = (
		(352, 352, 197, 0, 0, 281, 0, 0, 281, 2, 0),	#	
		(352, 352, 197, 281, 0, 0, 0, 0, 281, 2, 0),	#	クリスタリウム
		)

	dataset["body"] = (
		(572, 572, 320, 457, 0, 0, 0, 0, 457, 2, 0),	#	コーラス
		(572, 572, 320, 0, 0, 457, 0, 0, 457, 2, 0),	#	
		)

	dataset["hands"] = (
		(352, 352, 0, 281, 197, 0, 0, 0, 281, 2, 0),	#	コーラス
		(352, 352, 0, 0, 197, 281, 0, 0, 281, 2, 0),	#	
		)

	dataset["waist"] = (
		(264, 264, 0, 0, 148, 211, 0, 0, 211, 2, 0),	#	
		(264, 264, 148, 211, 0, 0, 0, 0, 211, 2, 0),	#	クリスタリウム
		)

	dataset["legs"] = (
		(572, 572, 320, 0, 0, 457, 0, 0, 457, 2, 0),	#	
		(572, 572, 320, 457, 0, 0, 0, 0, 457, 2, 0),	#	クリスタリウム
		)

	dataset["feet"] = (
		(352, 352, 281, 197, 0, 0, 0, 0, 281, 2, 0),	#	コーラス
		(352, 352, 197, 0, 0, 281, 0, 0, 281, 2, 0),	#	
		)

	dataset["earrings"] = (
		(264, 264, 148, 0, 0, 211, 0, 0, 211, 2, 0),	#	
		(264, 264, 0, 211, 148, 0, 0, 0, 211, 2, 0),	#	クリスタリウム
		)

	dataset["necklace"] = (
		(264, 264, 0, 211, 148, 0, 0, 0, 211, 2, 0),	#	コーラス
		(264, 264, 211, 0, 0, 148, 0, 0, 211, 2, 0),	#	
		)

	dataset["bracelets"] = (
		(264, 264, 211, 148, 0, 0, 0, 0, 211, 2, 0),	#	コーラス
		(264, 264, 0, 0, 211, 148, 0, 0, 211, 2, 0),	#	
		)

	dataset["ring1"] = (
		(264, 264, 211, 0, 148, 0, 0, 0, 211, 2, 0),	#	
		# (264, 264, 0, 148, 211, 0, 0, 0, 211, 2, 0),	#	
		)

	dataset["ring2"] = (
		# (264, 264, 211, 0, 148, 0, 0, 0, 211, 2, 0),	#	
		(264, 264, 0, 148, 211, 0, 0, 0, 211, 2, 0),	#	
		)

	return dataset


def get_dataset_sam_il500():
	# コーラス(上) vs クリスタリウム(下)
	# 'vt', 'vt_lim', 'dh', 'ch', 'dt', 'ss', 'tn', 'pi', 'subst_lm', 'ex_m', 'mg_m'
	dataset = {}
	return dataset

def get_dataset_drg_il500():
	# コーラス(上) vs クリスタリウム(下)
	# 'vt', 'vt_lim', 'dh', 'ch', 'dt', 'ss', 'tn', 'pi', 'subst_lm', 'ex_m', 'mg_m'
	dataset = {}
	return dataset

def get_dataset_nin_il500():
	# コーラス(上) vs クリスタリウム(下)
	# 'vt', 'vt_lim', 'dh', 'ch', 'dt', 'ss', 'tn', 'pi', 'subst_lm', 'ex_m', 'mg_m'
	dataset = {}
	return dataset


def get_selected_dataset(dataset, choice_eq):
	rtn = {}
	for i in zip(dataset.keys(), choice_eq):
		rtn[i[0]] = (dataset[i[0]][i[1]],)
	return rtn


def output(vals):
	# dataset内の["arm"]などの要素数が1の時のみ有効（各部位の装備データが一つしかないとき）
	string = "{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}"
	print(string.format(
		vals[0], vals[1],
		vals[2], vals[7],
		vals[3], vals[7],
		vals[4], vals[7],
		vals[5], vals[7],
		vals[8], vals[9])
	)


def gen_data(dataset):
	data = {}
	for eq in equips:

		b = all([ len(i)==len(['vt', 'vt_lim', 'dh', 'ch', 'dt', 'ss', 'tn', 'pi', 'subst_lm', 'ex_m', 'mg_m']) for i in dataset[eq]])
		if b is False:
			raise ValuError("与えられたtupleのサイズが想定と異なります。")

		tmp = {}
		# tmp["vt"] = [ (v[0], v[1]) for v in dataset[eq] ]
		tmp["dh"] = [ (v[2], v[8]) for v in dataset[eq] ]
		tmp["ch"] = [ (v[3], v[8]) for v in dataset[eq] ]
		tmp["dt"] = [ (v[4], v[8]) for v in dataset[eq] ]
		tmp["ss"] = [ (v[5], v[8]) for v in dataset[eq] ]
		tmp["tn"] = [ (v[6], v[8]) for v in dataset[eq] ]
		tmp["pi"] = [ (v[7], v[8]) for v in dataset[eq] ]
		tmp["ex_m"] = dataset[eq][0][9]		# 同じ部位で複数の装備が与えられたとき、今の実装だと0番目の装備の
		tmp["mg_m"] = dataset[eq][0][10]	# 空きパターンにしか対応していないので注意すること。
		data[eq] = tmp

		# print(tmp)

	return data


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


	#### 変換する ####
	data = gen_data(dataset)


	### 準備 ###
	obj = MateriaOpt(data)

	obj.set_rate_dmgsrc(aa=0.1259, dot=0.1272, ss=0.4175)	# BRD
	# obj.set_rate_dmgsrc(aa=0.0, dot=0.1562, ss=0.6799)	# WHM
	# obj.set_rate_dmgsrc(aa=0.1232, dot=0.0, ss=0.6855)	# DRK	https://www.fflogs.com/reports/mYhw7TdrxF9jQWyB#fight=25&type=damage-done
	# obj.set_rate_dmgsrc(aa=0.0, dot=0.15, ss=0.6)	# SMN

	#### GCD 条件 ####	http://allaganstudies.akhmorning.com/stats/speed/
	# obj.set_ss_condition(127)	# 制約条件: GCDが少なくとも 2.48 以上
	# obj.set_ss_condition(432)	# 制約条件: GCDが少なくとも 2.45 以上
	# obj.set_ss_condition(534)	# 制約条件: GCDが少なくとも 2.44 以上
	# obj.set_ss_condition(635)	# 制約条件: GCDが少なくとも 2.43 以上
	# obj.set_ss_condition(737)	# 制約条件: GCDが少なくとも 2.42 以上
	# obj.set_ss_condition(838)	# 制約条件: GCDが少なくとも 2.41 以上
	# obj.set_ss_condition(940)	# 制約条件: GCDが少なくとも 2.40 以上
	# obj.set_ss_condition(1041)	# 制約条件: GCDが少なくとも 2.39 以上
	# obj.set_ss_condition(1143)	# 制約条件: GCDが少なくとも 2.39 以上
	# obj.set_ss_condition(1244)	# 制約条件: GCDが少なくとも 2.38 以上

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

