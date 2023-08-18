echo '生成目录'
python3 ../python-utils/main.py

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

