import os
import sys
             
pathname = os.path.abspath(sys.argv[0])         
base_path = os.path.abspath(os.path.dirname(os.path.dirname(pathname)))
print(os.path.join(base_path,"data\\training_images"))