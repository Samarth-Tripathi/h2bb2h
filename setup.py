import setuptools
  

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='h2bb2h',
     version='0.1',
     scripts=['h2bb2h'] ,
     author="Samarth Tripathi",
     author_email="samarth.tripathi@gmail.com",
     description="Human to Byte , Byte to Human",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/Samarth-Tripathi/h2bb2h",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
