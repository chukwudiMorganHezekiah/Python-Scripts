import os
import shutil


def run():
    current_dir =input('Enter the directory where the files can be found \n')
    current_dir = current_dir.replace("\\",'/')
    location = input('Enter the directory where the files should be copied to \n')
    location = location.replace("\\",'/')
    checking = input('What is the file name category to be used to copy your files \n')
    copy_or_cut = input('Do You want to  cut the files, Please Y for yes \n')
    
    os.chdir(current_dir)
    if os.path.isdir(os.getcwd()):
        for f in os.listdir():
            if len(f) >= len(checking):
                if (f[0:len(checking)]).strip() ==checking:
                    if copy_or_cut =='Y':
                        shutil.move(os.path.join(os.getcwd(),f),os.path.join(location, f))   
                    else:
                        shutil.copyfile(os.path.join(os.getcwd(),f),os.path.join(location, f))   
                           
run()
   
print('Files moved, successfully')   
exit()  
          
          
