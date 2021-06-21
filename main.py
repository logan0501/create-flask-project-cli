import argparse
import os
import shutil
  

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("create-flask-app",help="create flask app with default filenames")
    parser.add_argument("-pyfn","-pyfilename",help="Flask python file name",default="app")
    # parser.add_argument("-htfn","-htmlfilename",help="Html file name",default="index")
    # parser.add_argument("-cssfn","-cssfilename",help="css file name",default="style")
    args = parser.parse_args()
    pythonfilename = args.pyfn.split(".")[0]
    # htmlfilename = args.htfn.split(".")[0]
    # cssfilename = args.cssfn.split(".")[0]
    pythonfile = open(pythonfilename+".py","w")
    os.mkdir("templates")
    os.mkdir("static")
    # htmlbasefile = open(os.path.join("templates","base.html"),"w")
    # htmlindexfile = open(os.path.join("templates","index.html"),"w")
    # cssfile = open(os.path.join("static","style.css"),"w")

    shutil.copyfile('./flask-files/index.html',"./templates/index.html")
    shutil.copyfile('./flask-files/base.html',"./templates/base.html")
    shutil.copyfile('./flask-files/style.css',"./static/style.css")
    shutil.copyfile('./flask-files/app.py',"app.py")
    print('sucessfully created')
if __name__ == "__main__":
    main()
