#!/bin/bash

# 获取脚本所在目录的绝对路径
SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)

# 切换到脚本目录
cd "$SCRIPT_DIR" || exit

echo "当前目录: $(pwd)"

echo '生成目录'
book sm

echo '构建gitbook'
gitbook build

echo '切换到gf530142771.github.io目录 切换分支到 gh-pages 删除所有数据'
cd ..
cd gf530142771.github.io
git checkout gh-pages
rm -r *
echo '复制新的_book信息'
cp -r ../markdown-notes/_book/* .
echo '更新分支 并上传'
git add .
git commit -m "update gitbook"
git push origin gh-pages

