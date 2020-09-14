#!/usr/bin/env python3
# coding=utf-8

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








