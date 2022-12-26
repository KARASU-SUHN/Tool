 
#find username
echo $USER
#check version
echo $ZSH_VERSION
#active work enviroment (base)
source /Users/User_name/opt/anaconda3/bin/activate

#Check working:
conda list

#listing the environments with:
conda env list 
#removing unused ones: 
conda env remove --name <yourenvironmentname>.

#deactivate
conda deactivate
source deactivate
