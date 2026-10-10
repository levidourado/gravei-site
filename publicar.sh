#!/bin/sh
# Regera as páginas e publica a pasta site/ no repo público levidourado/gravei-site (GitHub Pages).
# O código do app fica no repo privado; o plano Free só publica Pages de repo público.
set -e
cd "$(dirname "$0")/.."
python3 site/gerar_site.py site
git remote get-url site >/dev/null 2>&1 || git remote add site https://github.com/levidourado/gravei-site.git
git subtree split --prefix site -b site-publicar
git push site site-publicar:main --force
git branch -D site-publicar
