# Random-Name-Generator
<h3>Instructions to run:</br></h3>
if you don't have python installed, go ahead and do it.

install pyinstaller and pysimplegui from pip using this command:</br>
<code>pip install pyinstaller pysimplegui</code>

Open a cmd window (or terminal if you're on Mac) and cd into this projects' directory
<code>cd PATH/TO/PROJECT/DIRECTORY</code></br>
Now run this command:</br>
<code>pyinstaller --onefile --add-data "./names.txt;." --windowed --icon=bmc.ico name_generator.py</code>
</br>if you're on mac run this command:</br>
<code>pyinstaller --onefile --add-data "./names.txt:." --windowed --icon=bmc.ico name_generator.py</code>
</br>It should run for a few minutes.</br>
Next, open File Explorer (Finder if you're on Mac) to the projects directory and inside the <i>dist</i> directory you should find your executable.</br>
<bold>In the same directory as the executable</bold> create file called "names.txt" and write names in it (each name in a new line).</br>
Double click the executable and you're done!
<h4>NOTE: The txt file must be in same directory as the executable</h4>
