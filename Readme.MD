This a tiny python code to get the diffusion coefficient by fitting the depth-concentration profile, such as the chloride diffusivities in cementitious materials.
The raw data is well prepared *.xlsx file, which in include the depth in mm, and concentration in any unit, like %, mol/l, etc. A model Data.xlsx is given in the example folder.
Edit the *.xlsx file to your raw data file with the correct file path, which in line13, before you run the code.
Put the demo-diff-batch.py and the well prepared raw data file in the same directory, then double click the demo-diff-batch.py file, you will get a depth_con_fit.png in the same folder when your python environment well installed. If it does not work, pls run it in any terminal using ¡°python demo-diff-batch.py¡±, then you will see the error information to be fixed.
You can modify this code to treat you data in depth-concentration pair in xlsx or any txt type file, or input some parameters to skip the unnecessary information, such as header part, column name, separators, etc. 
If you use this tiny tool to analyze your data for publications, it would be grateful if you cite this repository.
