#!/usr/bin/env python3
# coding=utf-8

from pyscipopt import Model, quicksum
from math import floor

class MateriaOpt:

	data = {}
	meshi = {}

	def __init__(self, dataset):
		self.data = self.translate_data(dataset)

		# ダメージソースの割合。ジョブや状況によって変動。
		self.rate_aa = 0.125	# aaのダメージソースの割合
		self.rate_dot = 0.125	# dotのダメージソースの割合
		self.rate_ss = 0.300	# GCD短縮に影響するダメージソースの割合

		self.ss_lower = 0
		self.pi_lower = 0

		for i in ["dh", "ch", "dt", "ss", "tn", "pi"]:
			self.meshi[i] = 0

	def translate_data(self, dataset):
		data = {}

		for eq in dataset:

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


	def set_rate_dmgsrc(self, aa, dot, ss):

		b = any([val < 0.0 or 1.0 < val for val in [aa, dot, ss]])
		if b:		# aa, dot, ssの値が"割合"でないとき(0.0~1.0に収まっていないとき)
			raise ValuError("引数の値は 0.0~1.0 の範囲にしてください。")

		self.rate_aa = aa
		self.rate_dot = dot
		self.rate_ss = ss

	def set_ss_condition(self, ss):
		self.ss_lower = ss

	def set_pi_condition(self, pi):
		self.pi_lower = pi

	def set_meshi(self, dh=0, ch=0, dt=0, ss=0, tn=0, pi=0):
		self.meshi["dh"] = dh
		self.meshi["ch"] = ch
		self.meshi["dt"] = dt
		self.meshi["ss"] = ss
		self.meshi["tn"] = tn
		self.meshi["pi"] = pi

	def set_calcset(self, version="6.0"):
		# 各サブステ x とダメージ倍率 f(x) の関係式を2次関数で近似。パラメータa,b,cは要調整。
		# 係数: 	# f(x) = ax^2 + bx + c
		# scipを使う関係上、連続な関数を使用せざるを得ない。下記参照リンクの計算式の床関数もガン無視。なので多少誤差が出る（コンマ％くらい？）。
		# reference: http://allaganstudies.akhmorning.com/guide/damage/

		if version == "6.0" :
			print("calcset: 6.0")
			##############
			# after 6.0  #
			##############
			self.lmd_fdh = lambda x: 7.24e-5*x + 1

			self.lmd_fch = lambda x: (1.11e-8*x + 4.73e-5)*x + 0.02 + 1
			
			self.lmd_fdt = lambda x: 7.37e-05 * x + 1

			self.lmd_fss_gdc = lambda x: (2.63e-9*x + 2.65e-5)*x + 1
			self.lmd_fss_dot_aa = lambda x: 7.37e-05 * x + 1

			self.lmd_fss =  lambda x: self.rate_ss * self.lmd_fss_gdc(x) \
									+ (self.rate_aa+self.rate_dot) * self.lmd_fss_dot_aa(x) \
									+ (1-(self.rate_ss+self.rate_aa+self.rate_dot)) * 1

			self.lmd_ftn = lambda x: 5.26e-5*x + 1

			self.materia01 = 36		# アルテマ
			self.materia02 = 12		# オメガ

		else:
			print("calcset: 5.x")
			##############
			# before 5.5 #
			##############
			self.lmd_fdh = lambda x: 4.1667e-5*x + 1

			self.lmd_fch = lambda x: (3.6732e-9*x + 2.7271e-5)*x + 0.02 + 1
			
			self.lmd_fdt = lambda x: 3.9394e-05 * x + 1
			
			self.lmd_fss_gdc = lambda x: (2.13073e-9*x + 3.81069e-5)*x + 1
			self.lmd_fss_dot_aa = lambda x: 3.9394e-05 * x + 1

			self.lmd_fss =  lambda x: self.rate_ss * self.lmd_fss_gdc(x) \
									+ (self.rate_aa+self.rate_dot) * self.lmd_fss_dot_aa(x) \
									+ (1-(self.rate_ss+self.rate_aa+self.rate_dot)) * 1

			self.lmd_ftn = lambda x: 3.0303e-5*x + 1

			self.materia01 = 60		# エクス
			self.materia02 = 20		# メガ

		self.lmd_fpi = lambda x: 1	# 信仰値はダメージ倍率に影響なし

		self.expr_min = lambda x,y: (x+y)/2 - abs(x-y)/2	# min関数をscipが読める形に置き換える。
															# サブステの装備内での上限値を考慮するために必要。


	def calc_damage(self):
		data = self.data

		model = Model("calc_damage_multiplier")
		objvar = model.addVar("objvar", lb=1.0, ub=None, vtype= "C")
		model.setObjective(objvar, "maximize")

		#### def variables for SCIP ####
		_is_chosen = {}
		# ex_m = {}
		ex_m_dh = {}
		ex_m_ch = {}
		ex_m_dt = {}
		ex_m_ss = {}
		ex_m_tn = {}
		ex_m_pi = {}
		# mg_m = {}
		mg_m_dh = {}
		mg_m_ch = {}
		mg_m_dt = {}
		mg_m_ss = {}
		mg_m_tn = {}
		mg_m_pi = {}
		# subst = {}
		dh = {}
		ch = {}
		dt = {}
		ss = {}
		tn = {}
		pi = {}

		for eq in data:
			# 各装備に対するエクス装着数
			ex_m_dh[eq] = model.addVar(name="ex_m_dh_"+eq, vtype="I", lb=0)
			ex_m_ch[eq] = model.addVar(name="ex_m_ch_"+eq, vtype="I", lb=0)
			ex_m_dt[eq] = model.addVar(name="ex_m_dt_"+eq, vtype="I", lb=0)
			ex_m_ss[eq] = model.addVar(name="ex_m_ss_"+eq, vtype="I", lb=0)
			ex_m_tn[eq] = model.addVar(name="ex_m_tn_"+eq, vtype="I", lb=0)
			ex_m_pi[eq] = model.addVar(name="ex_m_pi_"+eq, vtype="I", lb=0)
			# 制約条件：1装備当たりのエクス装着数が、装着可能な個数の上限を超えない
			model.addCons(ex_m_dh[eq] + ex_m_ch[eq] + ex_m_dt[eq] + ex_m_ss[eq] + ex_m_tn[eq] + ex_m_pi[eq] <= data[eq]["ex_m"])

			# 各装備に対するメガ装着数
			mg_m_dh[eq] = model.addVar(name="mg_m_dh_"+eq, vtype="I", lb=0)
			mg_m_ch[eq] = model.addVar(name="mg_m_ch_"+eq, vtype="I", lb=0)
			mg_m_dt[eq] = model.addVar(name="mg_m_dt_"+eq, vtype="I", lb=0)
			mg_m_ss[eq] = model.addVar(name="mg_m_ss_"+eq, vtype="I", lb=0)
			mg_m_tn[eq] = model.addVar(name="mg_m_tn_"+eq, vtype="I", lb=0)
			mg_m_pi[eq] = model.addVar(name="mg_m_pi_"+eq, vtype="I", lb=0)
			# 制約条件：1装備当たりのメガ装着数が、装着可能な個数の上限を超えない
			model.addCons(mg_m_dh[eq] + mg_m_ch[eq] + mg_m_dt[eq] + mg_m_ss[eq] + mg_m_tn[eq] + mg_m_pi[eq] <= data[eq]["mg_m"])


			######## どちらの装備を選択したほうがよいかを変数にして解いてみる。
			_is_chosen[eq] = []
			if len(data[eq]["dh"]) == 1:
				_is_chosen[eq].append(model.addVar(name=eq+"_0", vtype="B", lb=0, ub=1))
				model.addCons(_is_chosen[eq][0] == 1)	# 選択すべき装備が1個の場合は 1 で決め打ち
			else:
				_is_chosen[eq].append(model.addVar(name=eq+"_0", vtype="B", lb=0, ub=1))	# 要修正。3以上の時。
				_is_chosen[eq].append(model.addVar(name=eq+"_1", vtype="B", lb=0, ub=1))
				model.addCons(_is_chosen[eq][0] + _is_chosen[eq][1] <= 1)
				# model.addCons(quicksum(_is_chosen[eq][i] for i in range(len(_is_chosen[eq]))) <= 1)
			########

			# tmp_dh = 60*ex_m_dh[eq] + 20*mg_m_dh[eq] + data[eq]["dh"][0]
			# tmp_ch = 60*ex_m_ch[eq] + 20*mg_m_ch[eq] + data[eq]["ch"][0]
			# tmp_dt = 60*ex_m_dt[eq] + 20*mg_m_dt[eq] + data[eq]["dt"][0]
			# tmp_ss = 60*ex_m_ss[eq] + 20*mg_m_ss[eq] + data[eq]["ss"][0]

			########
			tmp_dh = self.materia01*ex_m_dh[eq] + self.materia02*mg_m_dh[eq] \
					+ quicksum( data[eq]["dh"][i][0]*_is_chosen[eq][i] for i in range(len(_is_chosen[eq])) )	
			tmp_ch = self.materia01*ex_m_ch[eq] + self.materia02*mg_m_ch[eq] \
					+ quicksum( data[eq]["ch"][i][0]*_is_chosen[eq][i] for i in range(len(_is_chosen[eq])) )
			tmp_dt = self.materia01*ex_m_dt[eq] + self.materia02*mg_m_dt[eq] \
					+ quicksum( data[eq]["dt"][i][0]*_is_chosen[eq][i] for i in range(len(_is_chosen[eq])) )
			tmp_ss = self.materia01*ex_m_ss[eq] + self.materia02*mg_m_ss[eq] \
					+ quicksum( data[eq]["ss"][i][0]*_is_chosen[eq][i] for i in range(len(_is_chosen[eq])) )
			tmp_tn = self.materia01*ex_m_tn[eq] + self.materia02*mg_m_tn[eq] \
					+ quicksum( data[eq]["tn"][i][0]*_is_chosen[eq][i] for i in range(len(_is_chosen[eq])) )
			tmp_pi = self.materia01*ex_m_pi[eq] + self.materia02*mg_m_pi[eq] \
					+ quicksum( data[eq]["pi"][i][0]*_is_chosen[eq][i] for i in range(len(_is_chosen[eq])) )

			# マテリアにより上昇するサブステが、サブステ上限値を超えないようにする
			dh[eq] = self.expr_min(tmp_dh, data[eq]["dh"][0][1])
			ch[eq] = self.expr_min(tmp_ch, data[eq]["ch"][0][1])
			dt[eq] = self.expr_min(tmp_dt, data[eq]["dt"][0][1])
			ss[eq] = self.expr_min(tmp_ss, data[eq]["ss"][0][1])
			tn[eq] = self.expr_min(tmp_tn, data[eq]["tn"][0][1])
			pi[eq] = self.expr_min(tmp_pi, data[eq]["pi"][0][1])

		dh_sum = quicksum(dh[eq] for eq in data) + self.meshi["dh"]
		ch_sum = quicksum(ch[eq] for eq in data) + self.meshi["ch"]
		dt_sum = quicksum(dt[eq] for eq in data) + self.meshi["dt"]
		ss_sum = quicksum(ss[eq] for eq in data) + self.meshi["ss"]
		tn_sum = quicksum(tn[eq] for eq in data) + self.meshi["tn"]
		pi_sum = quicksum(pi[eq] for eq in data) + self.meshi["pi"]


		#### damage efficiency in each substatuses ####
		fdh = self.lmd_fdh(dh_sum)
		fch = self.lmd_fch(ch_sum)
		fdt = self.lmd_fdt(dt_sum)
		fss = self.lmd_fss(ss_sum)
		ftn = self.lmd_ftn(tn_sum)
		fpi = self.lmd_fpi(pi_sum)
		model.addCons(objvar <= fdh * fch * fdt * fss * ftn * fpi)	# 制約条件（目的関数）：ダメージ効率を最大化する


		#### SS調整 ####
		model.addCons(ss_sum >= self.ss_lower)	# 制約条件: SSが少なくとも X 以上

		## 信仰調整 ##
		model.addCons(pi_sum >= self.pi_lower)	# 制約条件: 信仰が少なくとも X 以上


		#### optimize ####
		model.optimize()
		sol = model.getBestSol()


		#### show result ####
		## 注意：	addVar()で vtype="I" や "B" として宣言した変数（整数変数、バイナリ変数）は、
		##			解を取得するために getVal() を呼ぶと、値が float 型で返ってくるので気を付けること。
		num_eq = {}
		result = {}
		for eq in data:
			########
			print(_is_chosen[eq])

			num_eq[eq] = [ round(model.getVal(v)) for v in _is_chosen[eq] ].index(1)
			########
			result[eq] = {}
			result[eq]["dh"] = (
				min(self.materia01*round(model.getVal(ex_m_dh[eq])) + self.materia02*round(model.getVal(mg_m_dh[eq])) + data[eq]["dh"][num_eq[eq]][0], data[eq]["dh"][num_eq[eq]][1]),
				data[eq]["dh"][num_eq[eq]][1],
				)
			result[eq]["ch"] = (
				min(self.materia01*round(model.getVal(ex_m_ch[eq])) + self.materia02*round(model.getVal(mg_m_ch[eq])) + data[eq]["ch"][num_eq[eq]][0], data[eq]["ch"][num_eq[eq]][1]),
				data[eq]["ch"][num_eq[eq]][1],
				)
			result[eq]["dt"] = (
				min(self.materia01*round(model.getVal(ex_m_dt[eq])) + self.materia02*round(model.getVal(mg_m_dt[eq])) + data[eq]["dt"][num_eq[eq]][0], data[eq]["dt"][num_eq[eq]][1]),
				data[eq]["dt"][num_eq[eq]][1],
				)
			result[eq]["ss"] = (
				min(self.materia01*round(model.getVal(ex_m_ss[eq])) + self.materia02*round(model.getVal(mg_m_ss[eq])) + data[eq]["ss"][num_eq[eq]][0], data[eq]["ss"][num_eq[eq]][1]),
				data[eq]["ss"][num_eq[eq]][1],
				)
			result[eq]["tn"] = (
				min(self.materia01*round(model.getVal(ex_m_tn[eq])) + self.materia02*round(model.getVal(mg_m_tn[eq])) + data[eq]["tn"][num_eq[eq]][0], data[eq]["tn"][num_eq[eq]][1]),
				data[eq]["tn"][num_eq[eq]][1],
				)
			result[eq]["pi"] = (
				min(self.materia01*round(model.getVal(ex_m_pi[eq])) + self.materia02*round(model.getVal(mg_m_pi[eq])) + data[eq]["pi"][num_eq[eq]][0], data[eq]["pi"][num_eq[eq]][1]),
				data[eq]["pi"][num_eq[eq]][1],
				)

		# 装備品のみのサブステ
		equip_dh = sum([data[eq]["dh"][num_eq[eq]][0] for eq in data])
		equip_ch = sum([data[eq]["ch"][num_eq[eq]][0] for eq in data])
		equip_dt = sum([data[eq]["dt"][num_eq[eq]][0] for eq in data])
		equip_ss = sum([data[eq]["ss"][num_eq[eq]][0] for eq in data])
		equip_tn = sum([data[eq]["tn"][num_eq[eq]][0] for eq in data])
		equip_pi = sum([data[eq]["pi"][num_eq[eq]][0] for eq in data])
		subst_init = equip_dh + equip_ch + equip_dt + equip_ss + equip_tn + equip_pi

		# マテリアのみのサブステ
		subst_materia_dh = sum([result[eq]["dh"][0] for eq in result]) - equip_dh
		subst_materia_ch = sum([result[eq]["ch"][0] for eq in result]) - equip_ch
		subst_materia_dt = sum([result[eq]["dt"][0] for eq in result]) - equip_dt
		subst_materia_ss = sum([result[eq]["ss"][0] for eq in result]) - equip_ss
		subst_materia_tn = sum([result[eq]["tn"][0] for eq in result]) - equip_tn
		subst_materia_pi = sum([result[eq]["pi"][0] for eq in result]) - equip_pi
		subst_materia = subst_materia_dh + subst_materia_ch + subst_materia_dt + subst_materia_ss + subst_materia_tn + subst_materia_pi

		fdh_sol = self.lmd_fdh(equip_dh + subst_materia_dh + self.meshi["dh"])
		fch_sol = self.lmd_fch(equip_ch + subst_materia_ch + self.meshi["ch"])
		fdt_sol = self.lmd_fdt(equip_dt + subst_materia_dt + self.meshi["dt"])
		fss_sol = self.lmd_fss(equip_ss + subst_materia_ss + self.meshi["ss"])
		fss_dot_aa_sol = self.lmd_fss_dot_aa(equip_ss + subst_materia_ss + self.meshi["ss"])
		fss_gdc_sol = self.lmd_fss_gdc(equip_ss + subst_materia_ss + self.meshi["ss"])
		ftn_sol = self.lmd_ftn(equip_tn + subst_materia_tn + self.meshi["tn"])
		fpi_sol = self.lmd_fpi(equip_pi + subst_materia_pi + self.meshi["pi"])

		print(sol)
		print("Optimal value:", model.getObjVal())
		print("")
		print("")
		print("            ｴｸｽ              |ﾒｶﾞ              | ｻﾌﾞｽﾃ")
		print("            dh ch dt ss tn pi|dh ch dt ss tn pi|     dh           ch           dt           ss           tn           pi")
		for eq in data:
			ex_m_dh_num = round(model.getVal(ex_m_dh[eq]))
			ex_m_ch_num = round(model.getVal(ex_m_ch[eq]))
			ex_m_dt_num = round(model.getVal(ex_m_dt[eq]))
			ex_m_ss_num = round(model.getVal(ex_m_ss[eq]))
			ex_m_tn_num = round(model.getVal(ex_m_tn[eq]))
			ex_m_pi_num = round(model.getVal(ex_m_pi[eq]))

			mg_m_dh_num = round(model.getVal(mg_m_dh[eq]))
			mg_m_ch_num = round(model.getVal(mg_m_ch[eq]))
			mg_m_dt_num = round(model.getVal(mg_m_dt[eq]))
			mg_m_ss_num = round(model.getVal(mg_m_ss[eq]))
			mg_m_tn_num = round(model.getVal(mg_m_tn[eq]))
			mg_m_pi_num = round(model.getVal(mg_m_pi[eq]))

			tmp_form = lambda x: str(x) if x > 0 else "-"

			string = "{0:10s}: {1}  {2}  {3}  {4}  {5}  {6} |{7}  {8}  {9}  {10}  {11}  {12} |{13:4d}  +{14:3d}   {15:4d}  +{16:3d}   {17:4d}  +{18:3d}   {19:4d}  +{20:3d}   {21:4d}  +{22:3d}   {23:4d}  +{24:3d}"
			print(string.format(eq, tmp_form(ex_m_dh_num), tmp_form(ex_m_ch_num), tmp_form(ex_m_dt_num), tmp_form(ex_m_ss_num), tmp_form(ex_m_tn_num), tmp_form(ex_m_pi_num),
									tmp_form(mg_m_dh_num), tmp_form(mg_m_ch_num), tmp_form(mg_m_dt_num), tmp_form(mg_m_ss_num), tmp_form(mg_m_tn_num), tmp_form(mg_m_pi_num),
									data[eq]["dh"][num_eq[eq]][0], round(result[eq]["dh"][0]) - data[eq]["dh"][num_eq[eq]][0],
									data[eq]["ch"][num_eq[eq]][0], round(result[eq]["ch"][0]) - data[eq]["ch"][num_eq[eq]][0],
									data[eq]["dt"][num_eq[eq]][0], round(result[eq]["dt"][0]) - data[eq]["dt"][num_eq[eq]][0],
									data[eq]["ss"][num_eq[eq]][0], round(result[eq]["ss"][0]) - data[eq]["ss"][num_eq[eq]][0],
									data[eq]["tn"][num_eq[eq]][0], round(result[eq]["tn"][0]) - data[eq]["tn"][num_eq[eq]][0],
									data[eq]["pi"][num_eq[eq]][0], round(result[eq]["pi"][0]) - data[eq]["pi"][num_eq[eq]][0],
								))

		print("")
		print(num_eq)
		print("")
		print("サブステ 装備	: {0:4.0f}".format(subst_init))
		print("サブステ ﾏﾃﾘｱ	: {0:4.0f}".format(subst_materia))
		print("サブステ 総数	: {0:4.0f}".format(subst_init + subst_materia))
		print("")
		print("                       Equip  Materia  Meshi")
		print("dh(ﾀﾞｲﾚｸﾄﾋｯﾄ)	: {0:4.0f} ({1:4.0f} +  {2:4.0f}  + {3:4.0f})".format(equip_dh + subst_materia_dh + self.meshi["dh"], equip_dh, subst_materia_dh, self.meshi["dh"]))
		print("ch(ｸﾘﾃｨｶﾙﾋｯﾄ)	: {0:4.0f} ({1:4.0f} +  {2:4.0f}  + {3:4.0f})".format(equip_ch + subst_materia_ch + self.meshi["ch"], equip_ch, subst_materia_ch, self.meshi["ch"]))
		print("dt(意思力)	: {0:4.0f} ({1:4.0f} +  {2:4.0f}  + {3:4.0f})".format(equip_dt + subst_materia_dt + self.meshi["dt"], equip_dt, subst_materia_dt, self.meshi["dt"]))
		print("ss(ｽｷﾙｽﾋﾟｰﾄﾞ)	: {0:4.0f} ({1:4.0f} +  {2:4.0f}  + {3:4.0f})".format(equip_ss + subst_materia_ss + self.meshi["ss"], equip_ss, subst_materia_ss, self.meshi["ss"]))
		print("tn(不屈)	: {0:4.0f} ({1:4.0f} +  {2:4.0f}  + {3:4.0f})".format(equip_tn + subst_materia_tn + self.meshi["tn"], equip_tn, subst_materia_tn, self.meshi["tn"]))
		print("pi(信仰)	: {0:4.0f} ({1:4.0f} +  {2:4.0f}  + {3:4.0f})".format(equip_pi + subst_materia_pi + self.meshi["pi"], equip_pi, subst_materia_pi, self.meshi["pi"]))
		print("")
		print("rate_aa  : {0}".format(self.rate_aa))
		print("rate_dot : {0}".format(self.rate_dot))
		print("rate_ss  : {0}".format(self.rate_ss))
		print("")
		self.show_eff(fdh_sol, fch_sol, fdt_sol, fss_sol, fss_gdc_sol, fss_dot_aa_sol, ftn_sol, fpi_sol)

		# memo
		# 解に対する変数の値が知りたい場合
		# print(sol[dh])
		# print(model.getSolVal(sol, dh))
		# print(model.getVal(dh))

		# 解に対する式の値が知りたい場合
		# print(model.getSolVal(sol, fdh))
		# print(model.getVal(fdh))

		print("******** 厳密解 ********")
		rtn = self.calc_exact_dmg_multiplier(equip_dh + subst_materia_dh + self.meshi["dh"],
											equip_ch + subst_materia_ch + self.meshi["ch"],
											equip_dt + subst_materia_dt + self.meshi["dt"],
											equip_ss + subst_materia_ss + self.meshi["ss"],
											equip_tn + subst_materia_tn + self.meshi["tn"],
											equip_pi + subst_materia_pi + self.meshi["pi"],
											"6.0")
		self.show_eff(*rtn)


		# tmp = sum([60*data[eq]["ex_m"] + 20*data[eq]["mg_m"] for eq in data])
		# self.kenzan(tmp, equip_dh, equip_ch, equip_dt, equip_ss, equip_tn, equip_pi)

	def calc_exact_dmg_multiplier(self, subst_dh, subst_ch, subst_dt, subst_ss, subst_tn, subst_pi, version="6.0"):
		# reference: http://allaganstudies.akhmorning.com/guide/damage/

		if version == "6.0":
			lmd_exact_fdh_prob = lambda x: floor(550/1900*x) / 1000
			lmd_exact_fdh = lambda x: lmd_exact_fdh_prob(x) * 0.25 + 1

			lmd_exact_fch_bonus = lambda x: floor(200/1900*x + 1400) / 1000
			lmd_exact_fch_prob = lambda x: floor(200/1900*x + 50) / 1000
			lmd_exact_fch = lambda x: (lmd_exact_fch_bonus(x) - 1) * lmd_exact_fch_prob(x) + 1

			lmd_exact_fdt_bonus = lambda x: floor(140/1900*x + 1000) / 1000
			lmd_exact_fdt = lambda x: lmd_exact_fdt_bonus(x)

			lmd_exact_gdcm = lambda x: floor((1000-floor(130/1900*x)) * 2500/1000)
			lmd_exact_gdc = lambda x: floor(lmd_exact_gdcm(x)/10)/100
			lmd_exact_fss_gdc = lambda x: 2.5 / lmd_exact_gdc(x)
			lmd_exact_fss_dot_aa =  lambda x: floor(130/1900*x + 1000) / 1000
			lmd_exact_fss = \
				lambda x: self.rate_ss * lmd_exact_fss_gdc(x) \
						+ (self.rate_aa+self.rate_dot) * lmd_exact_fss_dot_aa(x) \
						+ 1-(self.rate_ss+self.rate_aa+self.rate_dot) * 1

			lmd_exact_ftn_bonus = lambda x: floor(100/1900*x + 1000) / 1000
			lmd_exact_ftn = lambda x: lmd_exact_ftn_bonus(x)

		else:	# 5.x以前
			lmd_exact_fdh_prob = lambda x: floor(550/3300*x) / 1000
			lmd_exact_fdh = lambda x: lmd_exact_fdh_prob(x) * 0.25 + 1

			lmd_exact_fch_bonus = lambda x: floor(200/3300*x + 1400) / 1000
			lmd_exact_fch_prob = lambda x: floor(200/3300*x + 50) / 1000
			lmd_exact_fch = lambda x: (lmd_exact_fch_bonus(x) - 1) * lmd_exact_fch_prob(x) + 1

			lmd_exact_fdt_bonus = lambda x: floor(130/3300*x + 1000) / 1000
			lmd_exact_fdt = lambda x: lmd_exact_fdt_bonus(x)

			lmd_exact_gdcm = lambda x: floor((1000-floor(130/3300*x)) * 2500/1000)
			lmd_exact_gdc = lambda x: floor(lmd_exact_gdcm(x)/10)/100
			lmd_exact_fss_gdc = lambda x: 2.5 / lmd_exact_gdc(x)
			lmd_exact_fss_dot_aa =  lambda x: floor(130/3300*x + 1000) / 1000
			lmd_exact_fss = \
				lambda x: self.rate_ss * lmd_exact_fss_gdc(x) \
						+ (self.rate_aa+self.rate_dot) * lmd_exact_fss_dot_aa(x) \
						+ 1-(self.rate_ss+self.rate_aa+self.rate_dot) * 1

			lmd_exact_ftn_bonus = lambda x: floor(100/3300*x + 1000) / 1000
			lmd_exact_ftn = lambda x: lmd_exact_ftn_bonus(x)

		lmd_exact_fpi = lambda x: 1

		exact_fdh_sol = lmd_exact_fdh(subst_dh)
		exact_fch_sol = lmd_exact_fch(subst_ch)
		exact_fdt_sol = lmd_exact_fdt(subst_dt)
		exact_fss_sol = lmd_exact_fss(subst_ss)
		exact_fss_gdc_sol = lmd_exact_fss_gdc(subst_ss)
		exact_fss_dot_aa_sol = lmd_exact_fss_dot_aa(subst_ss)
		exact_ftn_sol = lmd_exact_ftn(subst_tn)
		exact_fpi_sol = lmd_exact_fpi(subst_pi)

		return (exact_fdh_sol, exact_fch_sol, exact_fdt_sol, exact_fss_sol, exact_fss_gdc_sol, exact_fss_dot_aa_sol, exact_ftn_sol, exact_fpi_sol)

	def show_eff(self, fdh_sol, fch_sol, fdt_sol, fss_sol, fss_gdc_sol, fss_dot_aa_sol, ftn_sol, fpi_sol):
		print("ﾀﾞﾒｰｼﾞ倍率 (= fdh * fch * fdt * fss * ftn * fpi) = {0:2.5f}".format(fdh_sol*fch_sol*fdt_sol*fss_sol*ftn_sol*fpi_sol))
		print("fdh = {0:2.5f}".format(fdh_sol))
		print("fch = {0:2.5f}".format(fch_sol))
		print("fdt = {0:2.5f}".format(fdt_sol))
		print("fss = {0:2.5f}".format(fss_sol))
		print("(fss_gdc    = {0:2.5f})".format(fss_gdc_sol))
		print("(fss_dot_aa = {0:2.5f})".format(fss_dot_aa_sol))
		print("ftn = {0:2.5f}".format(ftn_sol))
		print("fpi = {0:2.5f}".format(fpi_sol))
		print()
		return fdh_sol*fch_sol*fdt_sol*fss_sol*ftn_sol*fpi_sol

	def kenzan(self, num_mtr_emp, equip_dh, equip_ch, equip_dt, equip_ss):
		print("")
		print("** 検算(ｻﾌﾞｽﾃ上限無視) **")
		print("ﾏﾃﾘｱなし  : {0:2.5f}".format(self.lmd_fdh(equip_dh) \
											*self.lmd_fch(equip_ch) \
											*self.lmd_fdt(equip_dt) \
											*self.lmd_fss(equip_ss)))
		print("dhｶﾞﾝ積み : {0:2.5f}".format(self.lmd_fdh(equip_dh + num_mtr_emp) \
											*self.lmd_fch(equip_ch) \
											*self.lmd_fdt(equip_dt) \
											*self.lmd_fss(equip_ss)))
		print("chｶﾞﾝ積み : {0:2.5f}".format(self.lmd_fdh(equip_dh) \
											*self.lmd_fch(equip_ch + num_mtr_emp) \
											*self.lmd_fdt(equip_dt) \
											*self.lmd_fss(equip_ss)))
		print("dtｶﾞﾝ積み : {0:2.5f}".format(self.lmd_fdh(equip_dh) \
											*self.lmd_fch(equip_ch) \
											*self.lmd_fdt(equip_dt + num_mtr_emp) \
											*self.lmd_fss(equip_ss)))
		print("ssｶﾞﾝ積み : {0:2.5f}".format(self.lmd_fdh(equip_dh) \
											*self.lmd_fch(equip_ch) \
											*self.lmd_fdt(equip_dt) \
											*self.lmd_fss(equip_ss + num_mtr_emp)))
		print("")
