# 1. Check modified files

git status

# 2. Add all updated documentation files

git add .

# 3. Commit changes

git commit -m "Update Delphos documentation"

# 4. Push changes to main repository

git push

# 5. Rebuild and deploy MkDocs site

mkdocs gh-deploy --force
