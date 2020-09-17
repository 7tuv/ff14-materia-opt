# ff14-materia-opt

* サブステータスによるダメージ倍率が最大となるようなマテリアの組み合わせを求めます。
	* 同一部位に複数の同IL装備を指定することで、装備の組み合わせも加味して最適解を求められます。
* GCD、信仰等の条件を付けて最適な組み合わせを求めることも可能です。
	* GCD条件のみ実装済み。

# 環境
* Ubuntu 18.04.1 LTS (WLS)
* Python 3.6.9
* SCIP 6.0.2
* PySCIPOpt 2.3.3


# SCIP導入方法

## 1. scipoptsuiteダウンロード

下記ページから SCIP Optimization Suite をダウンロードし、適当なフォルダ（ここでは"/var/tmp"）に置く。

https://www.scipopt.org/index.php

Download -> Version: 6.0.2 -> Linux -> scipoptsuite-6.0.2.tgz

```
cd /var/tmp
tar xzf scipoptsuite-6.0.2.tgz
```


## 2. SCIPコンパイル/インストール

SCIPのコンパイルに必要なパッケージをインストールする。

```sh
apt update
apt install -y cmake build-essential zlib1g-dev libgmp3-dev
```

SCIPのコンパイルとインストールをする。

```sh
cd scipoptsuite-6.0.2
mkdir build
cd build
cmake ..
make
make install path='/usr/local'
```

参考: "https://scip.zib.de/doc/html/CMAKE.php"


## 3. 環境変数の設定

```
export SCIPOPTDIR=<path_to_install_dir>
# <path_to_install_dir> は、SCIPのインストールパス（上では '/usr/local' ）を指定する。
```

参考: "https://github.com/SCIP-Interfaces/PySCIPOpt/blob/master/INSTALL.md"


## 4. pipモジュールなどインストール

以下のモジュールをインストールする。

* パッケージ
	* python3-dev
* pipモジュール
	* cython
	* pyscipopt (2.3.3)

```sh
apt install python3-dev
pip3 install cython pyscipopt==2.2.3
```

# 使い方（作成中）

```sh
python3 main.py
```

# 参考
* PuLPでSCIPソルバーを使用する (MacOS)
	* https://qiita.com/nariaki3551/items/94fa74abe8a268372874
* Introduction to SCIP
	* https://imi.kyushu-u.ac.jp/~3rd_imi_ism_zib_ws/SCIP.pdf
* 整数計画法メモ
	* http://web.tuat.ac.jp/~miya/ipmemo.html
