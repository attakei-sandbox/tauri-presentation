============================
Demo presentation from Tauri
============================

Introduction
============

なによりはじめに
----------------

これは、 ``@attakei`` がお試しで作った Tauriのビルドデモです。

主に以下の点の挙動確認に注力しています。

* ローカルでの開発がWSL+VcXsrvでも支障がないか
* この環境下で、日本語を適切に利用できるか
* 最低限のリアクティブ処理を組み込めるか
* GitHub Actions等でWindows向けビルドができるのか

なんでReveal.js？
-----------------

* 「UI設計はしないけどインタラクティブな動きだけ出したい」を考えると、HTMLプレゼンテーションで十分
* いつもの（ ``sphinx-revealjs`` のドッグフーディング ）

前提
----

ローカル環境について

* Windows 10
* ArchLinux WSL2
* Windowsネイティブのビルドではなく、VcXsrvを利用したXでの動作確認のみ

VcXsrvの準備
============

VcXsrvって？
------------

簡単に言うと、「Windows上で動作するX Server」

* 目的としてはWSL上のGUIアプリケーションをWindows側で表示出来るようにするためのもの
* X Serverの説明については略
* Windows 11の人はWSLgのほうが良いかもしれません

VcXsrvの準備
------------

``winget`` でインストール出来ます

.. code-block:: console

   winget install vcxsrv

.. revealjs-break::

インストール後は、 ``XLaunch`` でX Serverを起動させることが出来ます。

* ディスプレイ設定は「Multiple windows」を選択
* クライアントの起動設定は「Start no client」を選択
* 「Native opengl」のチェックを外す
* 「Disable access control」のチェックを入れる

WSL側での設定
-------------

GUIアプリ起動時にVcXsrvのサーバーで表示できるように環境変数を設定しましょう。

.. code-block:: shell

   export DISPLAY=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2; exit;}'):0.0

ローカル環境での動作確認まで
============================

アプリケーションセットアップ
----------------------------

`Tauriドキュメント <https://tauri.app/v1/guides/getting-started/prerequisites>`_ を読みつつ環境構築すれば良いです。

* Linuxも deb, rpm, pacmanの3種のPMS系統向けに案内が出ているのでかなり楽
* Rust自体のインストールはPacmanにある ``rust`` でも平気だった

CLI周り
-------

どっちみちHTMLのバンドル環境を整えたほうが後で楽なので、基本的にはNPMベースの方にしておきます。

=> つまり、 ``yarn`` さえインストールしておけば平気

.. code-block:: console

   yarn create tauri-app

このコマンドでいくつか質問事項に答えれば、
自動で各種JSライブラリをベースにしたフロントエンドを含む
Tauriアプリケーションのプロジェクトが作成されます。

Sphinxドキュメントの準備
------------------------

今回は、 ``sphinx-revealjs`` でフロントを作成するので、 ``yarn`` の出番はしばらくお預け。

.. code-block:: console

   pipenv install sphinx-revealjs
   pipenv run sphinx-quickstart

TauriプロジェクトとSphinxビルドの連携
-------------------------------------

ひとまずは ``make`` での成果物をバンドルしたいため、
``src-tauri/tauri.conf.json`` を編集しておきましょう。

.. code-block:: json

   {
     "$schema": "../node_modules/@tauri-apps/cli/schema.json",
     "build": {
       "beforeBuildCommand": "",
       "beforeDevCommand": "",
       "devPath": "../build/revealjs",
       "distDir": "../build/revealjs"
     }
   }

※ ``src-tauri/tauri.conf.json`` から見た相対パスであることに注意

動作確認
--------

.. code-block:: console

   yarn tauri dev

実行すると、Rustのコンパイルなどが実行され、最終的にビルドされたバイナリが起動します。
VcXsrvが起動しているなら、そのままWindowsアプリケーションっぽく起動します。

ビルドする
==========

公式で ``tauri-apps/tauri-action`` が提供されており、
クロスプラットフォームビルドは GitHub Actionsで実現可能です。

https://github.com/attakei-sandbox/tauri-presentation/blob/main/.github/workflows/main.yml

Conclusion
==========

(書き途中)
