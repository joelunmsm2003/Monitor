git init
git add README.md
git commit -m "first commit"
git remote add origin git@github.com:joelunmsm2003/Monitor.git
git push -u origin master


#Si nos sale este error:

#Código :
fatal: remote origin already exists

La solución es teclear, y repetir el paso anterior:

#Código :
git remote rm origin